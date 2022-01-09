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
plt.savefig('plots/BAO_angle_z.png',dpi=400,bbox_inches='tight')


'''
Problem 2: Cluster Luminosity (8 points)
For this problem, use data from clusters.txt, which you can find on eCampus. The sample
of clusters in this file is flux limited such that fX (0.1 − 2.4 keV) ≥ 5 × 10−12 erg s−1 cm−2 .
The given fX limit in the 0.1-2.4 keV energy band corresponds to our (the observer’s) rest
frame, while the LX values correspond to the 0.1-2.4 keV energy band in the cluster’s rest
frame.
'''
file=open("clusters.txt","r")

lines=file.readlines()
name=[]
z=[]
flux=[]
Lx=[]
for x in lines[1:]:
    name.append(x.split('\t')[0])
    z.append(float(x.split('\t')[1]))
    flux.append(float(x.split('\t')[2]))
    Lx.append(float(x.split('\t')[3]))
file.close()
print(Lx)
#print(z)

'''
a) Using the same cosmology parameters as the previous question, plot the X-ray lumi-
nosity LX vs z. (3 points)
'''



'''
On the plot above, add the flux limit line (the lowest LX that can be observed for every
z based on the given flux limit). Make sure to show the equation you use to plot this
limit line. (3 points)
'''
def Lum_lim(z):
    fx=5e-12 #erg/s/cm2
    dl=cosmo.luminosity_distance(z).to(u.cm)
    Lx=fx*4*np.pi*(dl**2)
    return Lx

z2=np.linspace(0,0.7,1000)

plt.figure(1)
plt.scatter(z,Lx,s=1)
plt.plot(z2,Lum_lim(z2),'red',linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('z')
plt.ylabel('Lx')
plt.ylim(1e41,1e46)
plt.savefig('plots/xray_lum.png',dpi=400,bbox_inches='tight')

'''
c) Do all the clusters appear above the flux limit line? Why is this the case? (2 points)
'''
plt.show()




