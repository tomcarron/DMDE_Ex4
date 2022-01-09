#Script for DMDE Ex4
import numpy as np
import astropy
import astropy.constants as const
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.cosmology import Planck18_arXiv_v2 as P18
from astropy.cosmology import FlatwCDM
import pandas as pd

'''
Problem 1: Baryon Acoustic Oscillations (BAOs)

Use 100 Mpc/h as the BAO length scale, h = 0.67, wDE = −1, Ωm = 0.3, and ΩDE = 0.7 for
the following problem.

a) Plot the angle subtended by BAO in degrees as a function of redshift. (5 points)

b) How can this be used to constrain the cosmological parameters? You may use a different
set of parameters to justify your answer. (3 points)
'''

h=0.67
wde=-1
Om=0.3
Ode=0.7
#l=100 #Mpc/h
#Set the cosmological model

cosmo=FlatwCDM(H0=67.0,Om0=0.3,w0=-1.0)
#print(cosmo.Ode0)
def sub_ang(z):
    d_a=cosmo.angular_diameter_distance(z)
    l=100/0.67 #Mpc
    a=1/(1+z)
    y=l*a / d_a
    return y

redshift=np.linspace(0.1,1000,100000)

plt.figure(0)
plt.semilogx(redshift,sub_ang(redshift))
plt.xlabel('z')
plt.ylabel('$\Theta_{sc}$ [$^\circ$]')
plt.savefig('BAO_angle_z.png',dpi=400,bbox_inches='tight')
plt.show()




