#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

filewrite=open(sys.argv[1],'w')


def func(t,y):
 return y 
def func2(t,z,y):
 return 3*z-2*y+6*np.exp(-t)

def k2(t,y):
 return func(t+0.5*h,y+0.5*h*func(t,y))
def k3(t,y):
 return func(t+0.5*h,y+0.5*h*k2(t,y))
def k4(t,y):
 return func(t+h,y+h*k3(t,y))

def g2(t,z,y):
 return func2(t+0.5*h,z+0.5*h*func2(t,z,y),y+0.5*h*func(t,y))
def g3(t,z,y):
 return func2(t+0.5*h,z+0.5*h*func2(t,z,y)*g2(t,z,y),y+0.5*h*func(t,y)*k2(t,y))
def g4(t,z,y):
 return func2(t+h,z+h*g3(t,z,y),y+h*k3(t,y))


yini=2.
zini=2.
tini=0.
tmax=1.
N=10.
h=(tmax-tini)/N
t=tini
y=yini
z=zini

filewrite.write(str(t) + '     ' + str(y) + '\n')
while(t<tmax):
 oy=y
 y=y+h/6*(func(t,y)+2*k2(t,y)+2*k3(t,y)+k4(t,y))
 z=z+h/6*(func2(t,z,y)+2*g2(t,z,y)+2*g3(t,z,y)+g4(t,z,y))
 t=t+h
 filewrite.write(str(t) + '     ' + str(y) + '     ' + str(z) +'\n')

