# -*- coding: utf-8 -*-
"""
Quadratic.py- solves ax**2+bx+c and returns the results.
"""

import numpy as np

a = 23
b = 233
c = 23

discriminant = b**2-4*a*c
vertex = (-b/(2*a))

if discriminant < 0:
    xpos = (np.sqrt(-discriminant))/(2*a)
    xneg = (np.sqrt(-discriminant))/(2*a)
    print(vertex,"+", xpos, "i")
    print(vertex,"-", xneg, "i" )
elif discriminant > 0:
    xpos = (np.sqrt(discriminant))/(2*a)
    xneg = (-np.sqrt(discriminant))/(2*a)
    print(vertex + xpos)
    print(vertex + xneg)
else:
    print(vertex)