#!/usr/bin/python3
from mesh import *
from ddt import *
from div import *
from initial import *
from interpolate import *
from simulation import *
from spacing import *
from stencil import *
from weighting import *

mesh = Mesh(nx=32, spacing=SmoothNonuniform())
stencil = Stencil([-3, -2, -1, 0])

simulation = Simulation(
        mesh=mesh,
        Co=0.5,
        u=1,
        tracer=TruncatedSine().tracer,
        ddt=RungeKutta4(),
        interpolation=PointwisePolynomial(
            mesh,
            stencil,
            InverseDistanceWeighting(mesh, stencil),
            order=3)
)

simulation.integrate(endTime=1)
simulation.results[0].dumpTo('build/0.dat')
simulation.results[-1].dumpTo('build/1.dat')

for i, r in enumerate(simulation.results[1:-1]):
    r.dumpTo('build/{i}.dt.dat'.format(i=i+1))

print('l2error', simulation.l2error())

