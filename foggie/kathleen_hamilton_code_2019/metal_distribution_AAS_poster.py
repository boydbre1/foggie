#metal_distribution.py
#Summary: Plot metal mass, total mass, and metallicity over time for stars, ISM, CGM as a whole, and CGM regions divided by temperature.
#Author: Kathleen Hamilton-Campos, SASP intern at STScI, summer 2019 - kahamil@umd.edu

#Import library
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['ytick.major.size'] = 10
#Close all open plots to avoid accidentally overwriting them
plt.close("all")

#Matching colors to the Tumlinson, Peeples, Werk ARAA plots
star_color = '#d73027'
ism_color = '#4575b4'
cool_cgm_color = '#984ea3'
metal_color = "tab:gray"
pink_color = "lightcoral"
purple_color = "blueviolet"
green_color = "forestgreen"
yellow_color = "gold"

#Allowing the metallicity scatter to be translucent
scatter_alpha = 0.25

#halo_008508_arrays.py
if True:
    #Simulations
    simulations = [250, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1300, 1400, 1700]

    #Analysis
    virial_radius = [35., 44., 60., 73., 88., 102., 114., 124., 135., 151., 159., 167., 186.]
    redshift = [3.1634027198484, 2.8317499287854, 2.327015122116, 1.9572822784565, 1.67203864, 1.44355343, 1.25523385, 1.09649559, 0.96024456, 0.73680431, 0.64341981, 0.55938858, 0.34961832640547]
    lookbacks = [11.674, 11.406, 10.870, 10.334, 9.798, 9.262, 8.725, 8.189, 7.653, 6.580, 6.043, 5.506, 3.896]
    density_cut = [7.5e-24, 10.e-25, 1.e-25, 7.5e-25, 7.5e-25, 7.5e-25, 7.5e-25, 1.e-25, 1.e-25, 1.e-25, 2.5e-26, 2.5e-26, 5.e-27]
    central_radius_cut = [4., 4., 4., 4., 6., 4., 4., 8., 10., 10., 20., 20., 30.]
    satellite_distance_limit = [2., 2., 1., 2., 2., 2., 2., 2., 2., 2., 2., 2., 12.]

    #Metal Mass
    log_star_metal_mass = [7.43121824, 7.48120158, 8.31624128, 8.65219409, 8.75613115, 8.90493106, 8.97880156, 9.01590204, 9.03431259, 9.07707769, 9.09095877, 9.0989926, 9.13019357]
    log_ism_metal_mass = [6.99714912, 7.0761338, 7.55292066, 7.12274372, 7.41610945, 7.01884864, 7.22399948, 7.34495633, 7.62640389, 7.90247196, 7.95563369, 7.97245207, 8.13887159]
    log_cgm_metal_mass = [6.60796935, 6.66992534, 6.83262931, 6.92871495, 6.96129056, 7.21389993, 7.16571149, 6.960262, 6.93344747, 6.88127286, 6.70369428, 6.72991688, 6.61793625]
    # log_pink_metal_mass = [6.34797857, 6.35719255, 5.99509999, 6.1281016, 6.42264011, 6.79510715, 6.58298529, 6.01051374, 5.92205321, 5.76084686, 5.10499359, 5.37331619, 5.13140503]
    # log_purple_metal_mass = [6.07516598, 6.2086143, 6.34281394, 6.47144242, 6.30830197, 6.57219856, 6.6217368, 6.56151396, 6.38860369, 6.24905933, 6.26831868, 6.23935507, 6.02109504]
    # log_green_metal_mass = [5.58142714, 5.79417283, 6.32039906, 6.41072798, 6.42147444, 6.53451834, 6.69423788, 6.64148014, 6.57539623, 6.65215261, 6.46032455, 6.45545263, 6.45361668]
    # log_yellow_metal_mass = [5.40836993, 5.17269258, 6.18146326, 6.20612897, 6.23788467, 6.44667773, 6.22615504, 4.88659956, 6.18598284, 5.88536981, 5.27000911, 5.73545304, 5.07618744]

    #Metals Returned
    log_metals_returned = [7.61392046, 7.66834363, 8.40945534, 8.70150105, 8.80915847, 8.94573277, 9.01935911, 9.05387849, 9.07721023, 9.12616953, 9.14387134, 9.15165251, 9.1913927]

    #Total Mass
    log_star_total_mass = [9.13116955, 9.18642182, 9.90770785, 10.18853024, 10.29722092, 10.43045056, 10.50401991, 10.53781784, 10.56252562, 10.61318673, 10.63192447, 10.63963946, 10.68165432]
    log_ism_total_mass = [8.84376327, 8.91760662, 9.34775906, 9.02633363, 9.11001965, 8.98071814, 9.23518941, 9.6813505, 9.87878766, 9.91896161, 10.02418574, 10.08030778, 10.24605476]
    log_cgm_total_mass = [9.37511989, 9.58513522, 9.71643101, 9.83398883, 9.9224015, 10.00454427, 10.02347962, 9.94589795, 9.94444685, 9.96049841, 9.92833352, 9.96914984, 9.92151206]
    # log_pink_total_mass = [8.9280656, 8.91797054, 8.35530319, 8.81103599, 9.05796593, 9.0728697, 8.96851864, 8.40568938, 8.22681277, 8.39579674, 7.50616937, 7.74316116, 7.15325512]
    # log_purple_total_mass = [9.13572313, 9.44118599, 9.62239667, 9.7071033, 9.76319086, 9.84856084, 9.87171705, 9.8203237, 9.79942426, 9.73414711, 9.76129191, 9.78848361, 9.65198902]
    # log_green_total_mass = [8.10362025, 8.36866033, 8.80655537, 8.96337051, 9.08459454, 9.17492063, 9.29628956, 9.28774726, 9.31396042, 9.52426397, 9.42077554, 9.47766643, 9.57993238]
    # log_yellow_total_mass = [7.48953008, 7.3656677, 8.16428112, 8.21052821, 8.30490154, 8.56170041, 8.31070213, 7.34861815, 8.4293867, 8.06439883, 7.59941348, 8.04383945, 7.55635207]

    #Metallicity
    log_star_metallicity = [0.18777892, 0.18250999, 0.29626366, 0.35139408, 0.34664047, 0.36221073, 0.36251189, 0.36581443, 0.3595172, 0.3516212, 0.34676453, 0.34708337, 0.33626948]
    log_ism_metallicity = [0.04111608, 0.04625742, 0.09289183, -0.01585967, 0.19382003, -0.07413927, -0.12345969, -0.44866394, -0.36465354, -0.12875942, -0.18082181, -0.22012547, -0.21945294]
    log_cgm_metallicity = [-0.87942031, -1.02747964, -0.99607146, -1.01754364, -1.07338071, -0.90291412, -0.9700379, -1.09790571, -1.12326916, -1.19149532, -1.33690901, -1.35150273, -1.41584558]
    # log_pink_metallicity = [-0.69235679, -0.67304776, -0.47247297, -0.79520416, -0.74759559, -0.39003232, -0.49780312, -0.50744541, -0.41702933, -0.74721965, -0.51344555, -0.48211474, -0.13411985]
    # log_purple_metallicity = [-1.17282692, -1.34484146, -1.3918525, -1.34793065, -1.56715866, -1.38863205, -1.36225003, -1.37107951, -1.52309034, -1.59735754, -1.605243, -1.66139831, -1.74316375]
    # log_green_metallicity = [-0.63446288, -0.68675727, -0.59842608, -0.6649123, -0.77538986, -0.75267205, -0.71432145, -0.7585369, -0.85083396, -0.98438113, -1.07272076, -1.13448357, -1.23858547]
    # log_yellow_metallicity = [-0.19342991, -0.30524488, -0.09508762, -0.116669, -0.17928663, -0.22729246, -0.19681686, -0.57428835, -0.35567363, -0.29129879, -0.44167413, -0.42065618, -0.5924344]

    #Metallicity Scatter
    star_above_avg = [0.4258857, 0.41477733, 0.52653738, 0.57111221, 0.55433248, 0.56024463, 0.55303596, 0.55282943, 0.55087418, 0.5472402 , 0.54247595, 0.5409719, 0.52993782]
    star_below_avg = [-0.19890496, -0.18738902, -0.08768771, 0.00075179, 0.02717052, 0.06617214, 0.08230201, 0.09301548, 0.07755932, 0.05813121, 0.05176889, 0.05600171, 0.04241433]
    ism_above_avg = [0.12965704, 0.16203462, 0.28270069, 0.16285468, 0.38546582,  0.10261412,  0.04352738, -0.25387694, -0.18070932, 0.08769022,  0.11404643,  0.07332398, 0.03681575]
    ism_below_avg = [-0.07018089, -0.10188138, -0.20938902, -0.29305589, -0.08314182, -0.37300153, -0.43350158, -0.87829904, -0.76536607, -0.54628381, -0.89091468, -1.07389127, -1.11220268]
    cgm_above_avg = [-0.69048149, -0.81650855, -0.91738959, -0.8287334, -0.9251934 , -0.77780706, -0.80729691, -0.92058695, -0.96053067, -0.94194043, -1.10535983, -1.0861565, -1.13350629]
    cgm_below_avg = [-2.21385901, -2.80896338, -2.68514364, -2.40564863, -2.47887251, -2.70707491, -2.68641952, -2.63861884, -2.67774697, -2.49657654, -2.52120572, -2.63578073, -2.49443093]
    # pink_above_avg = [-0.48745911, -0.43971926, -0.14732756, -0.51566303, -0.52669418,  0.0109657 , -0.13167021, -0.25709479, -0.11785395, -0.49672121, -0.19709807, -0.1645786, 0.25069198]
    # pink_below_avg = [-1.75803835, -2.0247443, -1.69096653, -1.4725618, -1.76299288, -1.4438627 , -1.49683293, -1.39289017, -1.25354003, -1.4588543 , -1.19449295, -1.71464562, -0.81249839]
    # purple_above_avg = [-1.01514491, -1.12535442, -1.29859655, -1.16153545, -1.36388222, -1.33220844, -1.2839254 , -1.27928819, -1.42027794, -1.3794305 , -1.44164538, -1.41830124, -1.54725029]
    # purple_below_avg = [-2.46033919, -3.03481769, -2.79927485, -2.56671375, -2.65307067, -2.94154968, -2.91530981, -2.82387858, -2.87247583, -2.79522841, -2.72492237, -2.88990756, -2.83945443]
    # green_above_avg = [-0.38499272, -0.44693262, -0.32013754, -0.38645198, -0.51010363, -0.53585434, -0.42278747, -0.46685428, -0.53784839, -0.71658536, -0.80754616, -0.87721567, -1.00103731]
    # green_below_avg = [-1.3281163, -1.26934096, -1.38052043, -1.4570574, -1.47768456, -1.51671746, -1.58872672, -1.51199499, -1.61955669, -1.72127415, -1.69460371, -1.77089699, -1.76304542]
    # yellow_above_avg = [0.00071011, -0.14631235, 0.13166812, 0.08524327, 0.03782155,  0.01271684,  0.01202342, -0.3258607 , -0.13297435, -0.05795236, -0.26776021, -0.18813011, -0.38456845]
    # yellow_below_avg = [-0.59937852, -0.5896761, -0.59851372, -0.66450495, -0.79755886, -0.83139605, -0.65441034, -1.21310098, -0.93744487, -0.99958113, -1.28577526, -1.05028427, -1.11730288]

#Plot available metals
if False:
    plt.plot(redshift, log_metals_returned, '*')
    plt.title('Total Available Metals')
    plt.xlabel('Redshift (z)')
    plt.ylabel('Log Available Metals (Zsun)')
    plt.savefig("AvailableMetals.png")

#Plot metallicity, metal mass, and total mass for stars, ISM, and CGM
if True:
    #fig, axes = plt.subplots(1,2, figsize = (25,8))
    fig, axes = plt.subplots(2,1, figsize = (9, 13.5), sharex = True)

    #fig.suptitle('Metal Mass, Total Mass, and Metallicity over Time')
    lw = 3
    axes[0].plot(redshift, log_star_metal_mass, '-', linewidth = lw, color = star_color, label = 'Star Metal Mass')
    axes[0].plot(redshift, log_ism_metal_mass, '-',  linewidth = lw, color = ism_color, label = 'ISM Metal Mass')
    axes[0].plot(redshift, log_cgm_metal_mass, '-',  linewidth = lw, color = cool_cgm_color, label = 'CGM Metal Mass')
    #axes[0].plot(redshift, log_pink_metal_mass, '-', color = pink_color, label = r'T < $10^4$ K Metal Mass')
    #axes[0].plot(redshift, log_purple_metal_mass, '-', color = purple_color, label = r'$10^4$ < T < $10^5$ K Metal Mass')
    #axes[0].plot(redshift, log_green_metal_mass, '-', color = green_color, label = r'$10^5$ < T < $10^6$ K Metal Mass')
    #axes[0].plot(redshift, log_yellow_metal_mass, '-', color = yellow_color, label = r'T > $10^6$ K Metal Mass')
    # axes[0].plot(redshift, log_metals_returned, '-.', color = metal_color, label = 'Available Metals')

    axes[0].plot(redshift, log_star_total_mass, '--', linewidth = lw, color = star_color, label = 'Star Total Mass')
    axes[0].plot(redshift, log_ism_total_mass, '--',  linewidth = lw, color = ism_color, label = 'ISM Total Mass')
    axes[0].plot(redshift, log_cgm_total_mass, '--',  linewidth = lw, color = cool_cgm_color, label = 'CGM Total Mass')
    #axes[1].plot(redshift, log_pink_total_mass, '--', color = pink_color, label = r'T < $10^4$ K Total Mass')
    #axes[1].plot(redshift, log_purple_total_mass, '--', color = purple_color, label = r'$10^4$ < T < $10^5$ K Total Mass')
    #axes[1].plot(redshift, log_green_total_mass, '--', color = green_color, label = r'$10^5$ < T < $10^6$ K Total Mass')
    #axes[1].plot(redshift, log_yellow_total_mass, '--', color =yellow_color, label = r'T > $10^6$ K Total Mass')

    axes[1].plot(redshift, log_star_metallicity, ':', linewidth = lw,color = star_color, label = 'Star Metallicity')
    axes[1].fill_between(redshift, star_above_avg, star_below_avg, alpha = scatter_alpha, color = star_color, label = 'Star Scatter')

    axes[1].plot(redshift, log_ism_metallicity, ':',linewidth = lw, color = ism_color, label = 'ISM Metallicity')
    axes[1].fill_between(redshift, ism_above_avg, ism_below_avg, alpha = scatter_alpha, color = ism_color, label = 'ISM Scatter')

    axes[1].plot(redshift, log_cgm_metallicity, ':', linewidth = lw,color = cool_cgm_color, label = 'CGM Metallicity')
    axes[1].fill_between(redshift, cgm_above_avg, cgm_below_avg, alpha = scatter_alpha, color = cool_cgm_color, label = 'CGM Scatter')

    #axes[2].plot(redshift, log_pink_metallicity, ':', color = pink_color, label = r'T < $10^4$ K Metallicity')
    #axes[2].fill_between(redshift, pink_above_avg, pink_below_avg, alpha = scatter_alpha, color = pink_color, label = r'T < $10^4$ K Scatter')

    #axes[2].plot(redshift, log_purple_metallicity, ':', color = purple_color, label = r'$10^4$ < T < $10^5$ K Metallicity')
    #axes[2].fill_between(redshift, purple_above_avg, purple_below_avg, alpha = scatter_alpha, color = purple_color, label = r'$10^4$ < T < $10^5$ K Scatter')

    #axes[2].plot(redshift, log_green_metallicity, ':', color = green_color, label = r'$10^5$ < T < $10^6$ K Metallicity')
    #axes[2].fill_between(redshift, green_above_avg, green_below_avg, alpha = scatter_alpha, color = green_color, label = r'$10^5$ < T < $10^6$ K Scatter')

    #axes[2].plot(redshift, log_yellow_metallicity, ':', color = yellow_color, label = r'T > $10^6$ K Metallicity')
    #axes[2].fill_between(redshift, yellow_above_avg, yellow_below_avg, alpha = scatter_alpha, color = yellow_color, label = r'T > $10^6$ K Scatter')
    fs = 30
    axes[0].set_ylabel(r'$\log$ Mass (M${\odot}$)', fontsize = fs)
    ax2 = axes[0].twiny()

    from astropy.cosmology import Planck15 as cosmo
    import scipy
    from scipy.interpolate import interp1d
    from numpy import *
    zs_interp = linspace(0, 10, 1000)
    intp = interp1d(cosmo.lookback_time(zs_interp), zs_interp)
    xtcks = arange(2., 12., 1.)
    #xtcks = [11.5, 10, 8.5]
    xticks_use = [intp(xtck) for xtck in xtcks]
    xticks_lbl = [r'%i'%xtck for xtck in xtcks]
    ax2.set_xticks(xticks_use)
    ax2.set_xticklabels(xticks_lbl)
    print (xticks_use)
    print (xticks_lbl)
    ax2.set_xlabel('Lookback Time (Gyr)', fontsize = fs, labelpad = 15)


    #axes[0].set_xlabel('Redshift (z)', fontsize = fs)
    axes[1].set_ylabel(r'$\log$ Metallicity (Z$_{\odot}$)', fontsize = fs)
    axes[1].set_xlabel('Redshift (z)', fontsize = fs)
    #axes[1].yaxis.set_label_position("right")
    for ax in axes:
        ax.set_xlim(3.2, 0.3)
    ax2.set_xlim(3.2, 0.3)
    #axes[0].legend(loc='lower left', prop={'size': 10}, bbox_to_anchor= (0.0, 1.01), ncol=3, borderaxespad=0, frameon=False)
    #axes[1].legend(loc='lower left', prop={'size': 10}, bbox_to_anchor= (0.0, 1.01), ncol=3, borderaxespad=0, frameon=False)
    # axes[2].legend(loc='lower left', prop={'size': 10}, bbox_to_anchor= (0.0, 1.01), ncol=3, borderaxespad=0, frameon=False)
    fig.tight_layout()
    fig.subplots_adjust(left = 0.15)
    fig.savefig('MetalDistributionFullPoster.png', dpi = 500)