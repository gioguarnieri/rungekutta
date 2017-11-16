#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

filewrite=open(sys.argv[1],'w')


def func(t,y):
 return y 
def func2(t,z,y):
 return (3*z-2*y+6*np.exp(-t))

def k1(t,y):
 return h*func(t,y)
def g1(t,z,y):
 return h*func2(t,z,y)

def k2(t,y):
 return h*func(t+0.5*h,y+0.5*k1(t,y))
def g2(t,z,y):
 return h*func2(t+0.5*h,z+0.5*g1(t,z,y),y+0.5*k1(t,y))

def k3(t,y):
 return h*func(t+0.5*h,y+0.5*k2(t,y))
def g3(t,z,y):
 return h*func2(t+0.5*h,z+0.5*g2(t,z,y),y+0.5*k2(t,y))

def k4(t,y):
 return h*func(t+h,y+k3(t,y))
def g4(t,z,y):
 return h*func2(t+h,z+g3(t,z,y),y+k3(t,y))


yini=2.
zini=2.
tini=0.
tmax=1.

N=10.

h=(tmax-tini)/N
t=tini
y=yini
z=zini

while(t<tmax):
 filewrite.write(str(t) + '     ' + str(y) + '     ' + str(z) +'\n')
 y=y+1./6*(k1(t,y)+2*k2(t,y)+2*k3(t,y)+k4(t,y))
 z=z+1./6*(g1(t,z,y)+2*g2(t,z,y)+2*g3(t,z,y)+g4(t,z,y))
 t=t+h

