# Simulation parameters

yearinsec = 365.25*24*60*60        # 
A = 4.6e-25*yearinsec*1.0e18       # Ice fluidity
alpha = 1e10                       # Cylinder friction coefficient
rhoi = 900.0/(1.0e6*yearinsec**2)  # Ice density
rhow = 1000.0/(1.0e6*yearinsec**2) # Ocean density
g= 9.8*yearinsec**2                # Gravity adjusted to our unit system
n = 3                              # Glen's flow law exponent
mu=1000                            # Initial estimate for the viscosity
rho = rhoi * (1 - rhoi/rhow)

uy0 = 1000.0                       # Inflow velocity
H0 = 1000.0                        # Inflow boundary ice thickness

dt=10                              # Time-step size
theta=1                            # TSS activated: theta=1, TSS deactivated: theta=0
T = 2000                           # Simulation length
num_TS = int(T / dt)               # Number of time steps
