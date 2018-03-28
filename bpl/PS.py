
# function PM = defaultps
class PS:

    # Library to use
    libname = 'library'

    # Model parameters
    K = 5 # number of particles to use in search algorithm image model parameters
    ink_ncon = 2 # number of convolutions
    imsize = (105, 105) # image size
    ink_pp = 2 # amount of ink per point
    ink_max_dist = 2 # distance between points to which you get full ink
    ink_a = 0.5 # ink parameter 1
    ink_b = 6 # ink parameter 2

    # Creating a trajectory from a spline
    spline_max_neval = 200 # maxmium number of evaluations
    spline_min_neval = 10 #minimum
    spline_grain = 1.5 # 1 traj.point for every this many units pixel distance)

    # Max / min noise parameters for image model
    max_blur_sigma = 16 # blur kernel width
    min_blur_sigma = 0.5
    max_epsilon = 0.5 # pixel flipping
    min_epsilon = 1e-4

    # search parameters
    max_affine_scale_change = 2 # scale changes must be less than a factor of 2
    max_affine_shift_change = 50 # shift changes must less than this

    # MCMC PARAMETERS

    # details about the chain
    mcmc_samp_type_chain = 200 # number of samples to take in the MCMC chain ( for classif.)
    mcmc_nsamp_type_store = 10 # number of samples to store from this chain ( for classif.)
    mcmc_nsamp_token_chain = 25 # for completion (we take last sample in this chain)

    # mcmc proposal parameters (Note these are based on lib.tokenvar
    # parameters, although here they are hard - coded for convenience)
    mcmc_prop_gpos_sd = 1 # global position move
    mcmc_prop_shape_sd = 3 / 2 # shape move
    mcmc_prop_scale_sd = 0.0235 # scale move
    mcmc_prop_relmid_sd = 0.2168 # attach relation move
    mcmc_prop_relpos_mlty = 2 # multiply the sd of the standard position noise by this to propose new positions from prior

#    end