#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

filewrite=open(sys.argv[1],'w')


def func(y,t):
 return 1+(t-y)**2

def k2(y,t):
 return func(t+0.5*h,y+0.5*h*func(y,t))
def k3(y,t):
 return func(t+0.5*h,y+0.5*h*k2(y,t))
def k4(y,t):
 return func(t+h,y+h*k3(y,t))

yini=1.
tini=2.
tmax=3.
N=10.
h=(tmax-tini)/N

t=tini
y=yini
while(t<tmax):
 y=y+h/6*(func(y,t)+2*k2(y,t)+2*k3(y,t)+k4(y,t))
 t=t+h
 filewrite.write(str(t) + '     ' + str(y) + '\n')

