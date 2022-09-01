import numpy as np

def GBM1(S0, mu, sigma, T, Ndt, Nsims=10):
    #GBM1 Generate Geometric Brownian Motion Paths
    #   Input arguments:
    #   S0: initial price (required)
    #   mu: drift (required)
    #   sigma: volatility (required)
    #   T: Terminal time (required)
    #   Ndt: number of steps (required)
    #   Nsims: number of simulations (optional, default value=10)
    #   
    #   Output arguments:
    #   time: Time grid
    #   S: Paths

    # Throw an error manually
    if Nsims < 1:
        raise ValueError('Error. Number of simulations needs to be strictly positive.')

    # Create the time grid
    dt = T / Ndt
    time = np.linspace(0, T, Ndt)

    # Initialize the paths
    S = np.zeros((Ndt, Nsims))
    S[0,:] = S0

    # loop for every time step
    for ii in range(Ndt-1):
        S[ii+1,:] = S[ii,:] * np.exp( (mu + (sigma**2)/2) * dt \
                        + sigma * np.sqrt(dt) * np.random.normal(0.0, 1.0, size=(1,Nsims)))

    return time, S