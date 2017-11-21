#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

def prova(x):
 return -1./10*(np.sin(x)+3*np.cos(x))

def func(t,z,y):
 return z+2*y
def func2(t,z,y):
 return func(t,z,y)+np.cos(t)

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

yinir=-0.3
yfimr=-0.1

yini1=-0.3
zini1=0

yini2=0.
zini2=1.

tini=0.
tmax=np.pi/2.

N=10.

h=(tmax-tini)/N
t=tini
y1=[yini1]
z1=[zini1]

y2=[yini2]
z2=[zini2]

i=[y1,y2]
j=[z1,z2]
for y,z in zip(i,j):
 while(t<tmax):
  y.append(y[-1]+1./6*(k1(t,z[-1],y[-1])+2.*k2(t,z[-1],y[-1])+2.*k3(t,z[-1],y[-1])+k4(t,z[-1],y[-1])))
  z.append(z[-1]+1./6*(g1(t,z[-1],y[-1])+2.*g2(t,z[-1],y[-1])+2.*g3(t,z[-1],y[-1])+g4(t,z[-1],y[-1])))
  t=t+h
 t=tini

filewrite=open(sys.argv[1],'w')
multi=(yfimr-y1[-1])/y2[-1]
for ii in xrange(len(y1)):
 fimy=y1[ii]+multi*y2[ii]
 filewrite.write(str(t)+'    '+str(y1[ii]) + '   ' + str(y2[ii])+ '   ' +str(fimy)+ '   ' +str(prova(t)) +'\n')
 t=t+h
