from fenics import *
from constants import *
from SSA_functions import *

# Read in the mesh

mesh = Mesh('Mesh1000.xml')
h = CellDiameter(mesh)

# Define the function spaces

V = FunctionSpace(mesh, 'P', 1)
VV = VectorFunctionSpace(mesh,"CG",1)

uvec=Function(VV)
(ux,uy)=split(uvec)

uvect=TrialFunction(VV)
(u1,u2)=split(uvect)

vvect=TestFunction(VV)
(v1,v2)=split(vvect)

phi = TestFunction(V)
thick_new = TrialFunction(V)

# Interpolate fields 

a_s_ = Expression("0.0", degree=2)
a_b_ = Expression("0.0", degree=2)
a_s = interpolate(a_s_, V)
a_b = interpolate(a_b_, V)

thick_ = Expression(str(H0), degree=2)
thick = interpolate(thick_, V)

zs_ = Expression("30.0", degree=2)
zs = interpolate(zs_, V)

# Boundary conditions

boundaries = mark_bed_surface(mesh)
ds = Measure("ds", domain=mesh, subdomain_data=boundaries)
n = FacetNormal(mesh)

# Define boundary conditions (BCs)

# Dirichlet BCs for the velocity field
bc1 = DirichletBC(VV.sub(0), 0.0, boundaries,2)
bc2 = DirichletBC(VV.sub(1), uy0, boundaries,2)
bc4 = DirichletBC(VV.sub(0), 0.0, boundaries,3)
bc6 = DirichletBC(VV.sub(0), 0.0, boundaries,4)
bc7 = DirichletBC(VV.sub(0), 0.0, boundaries,5)
bc8 = DirichletBC(VV.sub(1), 0.0, boundaries,5)

# Dirichlet BCs for the thickness field

H_bc = DirichletBC(V, H0, boundaries, 2)

