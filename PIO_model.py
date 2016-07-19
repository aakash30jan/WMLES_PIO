#!/usr/bin/env python

################################################
###  Michael Howland, mhowland@stanford.edu  ###
###  CTR Summer Program 2016                 ###
###  Predictive Inner Outer Model, Marusic   ###
###  2011 in WMLES                           ###
################################################

# Import libraries
import numpy as np
import scipy.io as sio
import struct

# Parameters
retau = 2000
plane_num = 1
d=2.5
folder = ''
folder = 'data/' + 'Retau' + str(retau) + '/' + 'plane_' + str(plane_num) + '/' + str(d) + 'd/'
#print folder

# Load calibration data
t=1
nz = 4608 #number of spanwise locations
folder_bin = folder + 'cali_mat' + '_t' + str(t) + '.bin'
#print folder_bin
f = open(folder_bin, 'rb')
data = np.fromfile(f, dtype=np.float64)
#print len(data)
nx = float(len(data))/(float(nz)+1)
#print nx
s = (nx, 1)
tplus = np.zeros(s, dtype=np.float64)
s = (nx, nz) 
tau_w_star = np.zeros(s, dtype=np.float64)
# Unpack the binary data
for j in range(0, nz+1):
	if j == 0:
		tplus = data[0 : nx - 1]
	else:
		tau_w_star[:,j-1] = data[(j)*nx : (j+1)*nx]
#print tau_w_star[0,0], tau_w_star[4345, 0], tau_w_star[0,1]
#print tplus[0]

