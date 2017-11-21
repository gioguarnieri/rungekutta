#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

filewrite=open(sys.argv[1],'w')


def func(t,z,y):
 return z
def func2(t,z,y):
 return (3.*z-2.*y+6.*np.exp(-t))

def k1(t,z,y):
 return h*func(t,z,y)
def k2(t,z,y):
 return h*func(t+h/2.,z+g1(t,z,y)/2.,y+k1(t,z,y)/2.)
def k3(t,z,y):
 return h*func(t+h/2.,z+g2(t,z,y)/2.,y+k2(t,z,y)/2.)
def k4(t,z,y):
 return h*func(t+h,z+g3(t,z,y), y+k3(t,z,y))


def g1(t,z,y):
 return h*func2(t,z,y)
def g2(t,z,y):
 return h*func2(t+h/2.,z+g1(t,z,y)/2.,y+k1(t,z,y)/2.)
def g3(t,z,y):
 return h*func2(t+h/2.,z+g2(t,z,y)/2.,y+k2(t,z,y)/2.)
def g4(t,z,y):
 return h*func2(t+h,z+g3(t,z,y), y+k3(t,z,y))

yini=2.
zini=2.
tini=0.
tmax=1.

N=100.

h=(tmax-tini)/N
t=tini
y=yini
z=zini

while(t<tmax):
 filewrite.write(str(t)+'    '+str(y)+'\n')
 y=y+1./6*(k1(t,z,y)+2.*k2(t,z,y)+2.*k3(t,z,y)+k4(t,z,y))
 z=z+1./6*(g1(t,z,y)+2.*g2(t,z,y)+2.*g3(t,z,y)+g4(t,z,y))
 t=t+h
