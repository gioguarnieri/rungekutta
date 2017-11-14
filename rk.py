#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

filewrite=open(sys.argv[1],'w')


def func(t,y):
 return 1+(t-y)**2

def k2(t,y):
 return func(t+0.5*h,y+0.5*h*func(t,y))
def k3(t,y):
 return func(t+0.5*h,y+0.5*h*k2(t,y))
def k4(t,y):
 return func(t+h,y+h*k3(t,y))

yini=1.
tini=2.
tmax=3.
N=10.
h=(tmax-tini)/N

t=tini
y=yini
filewrite.write(str(t) + '     ' + str(y) + '\n')
while(t<tmax):
 y=y+h/6*(func(t,y)+2*k2(t,y)+2*k3(t,y)+k4(t,y))
 t=t+h
 filewrite.write(str(t) + '     ' + str(y) + '\n')

