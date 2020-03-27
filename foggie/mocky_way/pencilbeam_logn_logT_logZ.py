import numpy as np
import yt
from yt.utilities.math_utils import ortho_find
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'stixgeneral'

def pencilbeam_logn_logT_logZ(ds, los_rs, los_re, field, f_min, f_max,
                    f_cmap = plt.cm.Reds_r, clabel = r'log n(cm-3)',
                    tick_fontsize=16, save_file = './temp/pencilbeam_.pdf'):
    """
    Plot the baryon number density distribution along a pencil from observer
    through the halo.

    Input:
    ds: from yt.load()
    los_rs: ray start, code_length
    los_re: ray_end, code_length
    field: the number density field of the ion of interest
    No outputs.
    """

    los_vector = los_re - los_rs
    los_unit_vec = los_vector/np.linalg.norm(los_vector)
    north_vector, normal, zzz = ortho_find(los_unit_vec)
    los_center = (los_re+los_rs)/2.
    ray_length = np.linalg.norm(los_vector.in_units("kpc"))

    # colormap; need more entries here for other ions
    from yztools.yz_colormap import discrete_map
    f_cmap, val2color, norm, bounds = discrete_map(f_cmap, np.log10(f_min), \
                                                   np.log10(f_max), 10)
    slice = yt.OffAxisSlicePlot(ds, normal, field,
                                center=los_center,
                                width=((4, 'kpc'), (ray_length, 'kpc')),
                                north_vector=north_vector)
    slice.set_cmap(field, cmap=f_cmap)
    slice.set_zlim(field, zmin=f_min, zmax=f_max)
    slice.hide_axes()
    slice.hide_colorbar()
    slice_file = './temp/junk_pencile_beam.png'
    slice.save(slice_file)

    image_add_axes(slice_file, ray_length, f_cmap, bounds, norm, clabel,
                   tick_fontsize=tick_fontsize, save_file=save_file)


def image_add_axes(slice_file, ray_length, f_cmap, bounds, norm, clabel,
                   tick_fontsize=16, save_file='./temp/junk.pdf'):

    newimage = plt.imread(slice_file)
    nax0 = newimage.shape[0]
    nax1 = newimage.shape[1]

    fig = plt.figure(figsize=(2.5, 10))
    ax = fig.add_axes([0.04, 0.05, 0.8, 0.9])
    ax.imshow(newimage)

    # set ticks from pixel units to real world units
    r_min, r_max = 0, ray_length

    # xticks
    ax.set_xticks([0, nax1/2., nax1-1])
    ax.set_xticklabels(['-2', '0', '2'], fontsize=tick_fontsize)

    # yticks
    if ray_length<=10:
        r_step = 1
    else:
        r_step = 10
    yticks_realunit = np.mgrid[r_min:r_max:r_step]
    yticks = nax0*(1-yticks_realunit/(r_max-r_min))
    yticklabels = [str(int(ii)) for ii in yticks_realunit]
    # print(yticklabels)
    if len(yticklabels)>8: # if too crowded
        for j in range(len(yticklabels)):
                if j % 2 == 1:
                    yticklabels[j] = ''
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels, fontsize=tick_fontsize)

    # a line in the center
    ax.vlines(nax1/2., 0, nax0-1, color='w', lw=2)
    ax.set_ylabel('Line-of-Sight Position from Observer (kpc)',
                  fontsize=tick_fontsize)

    # a trick to set up color map
    fxax = fig.add_axes([0.9, 0.9, 0.1, 0.1])
    fximg = fxax.imshow(np.zeros((2, 2))+np.nan,
                    norm=norm,interpolation='nearest', cmap=f_cmap)
    fxax.set_axis_off()
    cax = fig.add_axes([0.58, 0.05, 0.08, 0.3])
    cb = fig.colorbar(fximg, cax=cax, orientation='vertical', format='%d',
             spacing='proportional', ticks=bounds[::2], boundaries=bounds)
    cb.set_label(clabel, fontsize=tick_fontsize-2)
    cb.ax.tick_params(labelsize=tick_fontsize-4)
    fig.savefig(save_file)
