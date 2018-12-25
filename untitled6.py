# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 18:31:43 2018

@author: My Surface Pro
"""

import numpy as np
import scipy as sp
import scipy.constants as c


t_step = 1
t_cycles = 10
t_step_array = np.zeros((t_cycles, 1))


class particle:
    def __init__(self, mass, charge, \
                 initial_position_x, initial_position_y, initial_position_z, initial_velocity_x, initial_velocity_y, initial_velocity_z):
        self.mass, self.charge, \
        self.initial_position_x, self.initial_position_y, self.initial_position_z, self.initial_velocity_x, self.initial_velocity_y, self.initial_velocity_z, \
        self.position_x, self.position_y, self.position_z, self.velocity_x, self.velocity_y, self.velocity_z, self.force_x, self.force_y, self.force_z \
        = mass, charge, \
        initial_position_x, initial_position_y, initial_position_z, initial_velocity_x, initial_velocity_y, initial_velocity_z, \
        np.full((t_cycles, 1), initial_position_x), np.full((t_cycles, 1), initial_position_y), np.full((t_cycles, 1), initial_position_z), np.full((t_cycles, 1), initial_velocity_x), np.full((t_cycles, 1), initial_velocity_y), np.full((t_cycles, 1), initial_velocity_z), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1))


P = np.empty(0)

p0 = particle(10**3, -1, 0, 0, 0, 0, 0, 0)
P = np.append(P, p0)
p1 = particle(10**3, -1, 1, 1, 1, 1, 1, 1)
P = np.append(P, p1)
#p2 = particle(10**3, -1, 2, 2, 2, 2, 2, 2)
#P = np.append(P, p2)
#p3 = particle(10**3, -1, 3, 3, 3, 3, 3, 3)
#P = np.append(P, p3)


def force(P, k):
    f_x = 0
    f_y = 0
    f_z = 0
    for i in range(1, int(float(np.shape(P)[0]))):
        for j in range(1, int(float(np.shape(P)[0]))):
            if i != j:
                
                radius = np.sqrt(float((P[j].position_x[k] - P[i].position_x[k])**2 + (P[j].position_y[k] - P[i].position_y[k])**2 + (P[j].position_z[k] - P[i].position_z[k])**2))
                
                inclination = np.arccos((P[j].position_z[k] - P[i].position_z[k])/radius)
                
                azimuth = np.arctan((P[j].position_y[k] - P[i].position_y[k])/(P[j].position_x[k] - P[i].position_x[k]))
                
                magnitude = float(-c.G*P[i].mass*P[j].mass/radius**2)
                
                f_x = magnitude*np.sin(inclination)*np.cos(azimuth)

                f_y = magnitude*np.sin(inclination)*np.sin(azimuth)
                
                f_z = magnitude*np.cos(inclination) 
            
                P[i].force_x[k] += f_x
                P[i].force_y[k] += f_y
                P[i].force_z[k] += f_z
            
            else:
                pass
        
    return

for i in range(t_cycles):
    force(P, i)