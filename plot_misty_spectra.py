from __future__ import print_function

import numpy as np
import MISTY
import logging
import sys
import os
import glob

import matplotlib as mpl
import seaborn as sns
sns.set_style("whitegrid", {'axes.grid' : False})
mpl.rcParams['font.family'] = 'stixgeneral'
mpl.rcParams['font.size'] = 10.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

from astropy.table import Table
from astropy.io import fits
from astropy.convolution import Gaussian1DKernel, convolve
import astropy.units as u

from spectacle.analysis import Resample
from spectacle.core.spectrum import Spectrum1DModel

# from consistency import *

def plot_misty_spectra(hdulist, **kwargs):
    outname = kwargs.get('outname', 'test.png')
    overplot = kwargs.get('overplot', False)

    ## how many lines are there?
    Nlines = np.int(hdulist[0].header['Nlines'])
    Nlines = 6
    print("there are ", Nlines, ' lines')
    # start by setting up plots
    fig = plt.figure(dpi=300)
    fig.set_figheight(11)
    fig.set_figwidth(5)
    # creates grid on which the figure will be plotted
    gs = gridspec.GridSpec(Nlines, 1)

    zsnap = hdulist[0].header['REDSHIFT']
    zmin, zmax = (zsnap-0.004), (zsnap+0.004)
    vmin, vmax = -300, 300


    for line in range(Nlines):
        ## fig.add_subplot(gs[line, 0])
        height = 1./Nlines - 0.01
        ax_spec = fig.add_axes([0.11, 0.05+ (Nlines-line -1)*height, 0.86, height],xlim=(vmin, vmax), ylim=(-0.05,1.05))
        try:
            # Construct spectacle spectrum
            # spectrum = Spectrum1DModel(redshift=0.0)
            ext = hdulist[line+2]
            name = ext.header['LINENAME']
            lambda_0 = ext.header['RESTWAVE'] * u.AA
            f_value = ext.header['F_VALUE']
            gamma = ext.header['GAMMA']
            tot_column = ext.header['TOT_COLUMN']
            # spectrum = Spectrum1DModel(redshift=0.0, lambda_0=lambda_0, f_value=f_value, gamma=gamma )
            spectrum = Spectrum1DModel(redshift=0.0, ion_name=name )
            print(line, name)
            try:
                redshift = hdulist[name].data['redshift']
                flux = hdulist[name].data['flux']
                wavelength_obs = hdulist[name].data['disp'] * u.AA
            except:
                redshift = hdulist[name].data['redshift_obs']
                flux = hdulist[name].data['flux_obs']
                wavelength_obs = hdulist[name].data['disp_obs'] * u.AA
            with u.set_enabled_equivalencies(u.equivalencies.doppler_relativistic(lambda_0*(1+zsnap))):
                velocity = (wavelength_obs).to('km/s')

            if False:
#            if 'NCOMP' in ext.header.keys():
                Ncomp = ext.header['NCOMP']
                for i in range(Ncomp):
                    delta_v = ext.header['FITVCEN{}'.format(i)] * u.Unit('km/s')
                    col_dens = ext.header['FITCOL{}'.format(i)]
                    v_dop = ext.header['FITB{}'.format(i)] * u.Unit('km/s')
                    print('i:',i,delta_v, col_dens, v_dop)
                    spectrum.add_line(column_density=col_dens, v_doppler=v_dop, delta_v=delta_v)
                    ax_spec.plot([delta_v.value, delta_v.value], [1.05, 0.95], color='k')
            #         ### plot component here
            #         this_comp = Spectrum1DModel(redshift=redshift)
            #         this_comp.add_line(lambda_0=lambda_0, f_value=f_value,
            #                           gamma=gamma, column_density=col_dens, v_doppler=v_dop,
            #                           delta_v=delta_v)
            #         this_flux = this_comp.flux(velocity)
            #         ax_spec.step(velocity, this_flux, color='darkorange', ls="--", dashes=(5,2), alpha=0.5)
            #         print('ok?')


            ### _lsf.fits files have '_obs' while _los.fits files don't
            # ax_spec.step(redshift, flux, color='darkorange',lw=1)
            ax_spec.plot(velocity, np.ones(len(velocity)),color='k',lw=1, ls=":")
            ax_spec.step(velocity, flux, color='#984ea3')
            if overplot:
                ax_spec.step(velocity, spectrum.flux(velocity), color='darkorange', lw=1, ls="--", dashes=(5, 2))
            ax_spec.text(vmin + 50, 0.15, name, fontsize=12.)
            coldens = "N = " + "{:4.2f}".format(tot_column)
            ax_spec.text(vmin + 50, 0, coldens, fontsize=12.)
        except Exception as e:
            logging.error("Plotting failed because: \n%s", e)
        if line < (Nlines-1):
            ax_spec.xaxis.set_major_locator(ticker.NullLocator())
        else:
            plt.xlabel('velocity [km/s]',fontsize=16.)
        #plt.xlim(vmin, vmax)
        #plt.ylim(-0.05, 1.05)
        #plt.subplots_adjust(wspace=None, hspace=None)
    print("                   ")
    print("before fig commands")
    print("                   ")
    fig.text(0.02, 0.5, 'normalized flux', fontsize=16., va='center', rotation='vertical')
    #fig.tight_layout()
    plt.savefig(outname)
    plt.close(fig)


if __name__ == "__main__":

    long_dataset_list = glob.glob(os.path.join(".", 'hlsp*rd00*ax*v6*lsf.fits.gz'))
    dataset_list = long_dataset_list

    for filename in dataset_list:
        plotname = '.' + filename.strip('lsf.fits.gz') + 'lsf.png'
        print('plotting spectra in ', filename, ' and saving as ', plotname)
        hdulist = fits.open(filename)
        plot_misty_spectra(hdulist, overplot=True, outname=plotname)
        hdulist.close()
