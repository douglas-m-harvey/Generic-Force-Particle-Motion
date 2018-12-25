# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:16:45 2018

@author: My Surface Pro
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as c


t_step = 3600
t_cycles = 2
t_step_array = np.zeros((t_cycles, 1))


class particle:
    def __init__(self, mass, charge, \
                 initial_position_x, initial_position_y, initial_position_z, initial_velocity_x, initial_velocity_y, initial_velocity_z):
        self.mass, self.charge, \
        self.initial_position_x, self.initial_position_y, self.initial_position_z, self.initial_velocity_x, self.initial_velocity_y, self.initial_velocity_z, \
        self.position_x, self.position_y, self.position_z, self.velocity_x, self.velocity_y, self.velocity_z, self.force_x, self.force_y, self.force_z, self.acceleration_x, self.acceleration_y, self.acceleration_z \
        = mass, charge, \
        initial_position_x, initial_position_y, initial_position_z, initial_velocity_x, initial_velocity_y, initial_velocity_z, \
        np.full((t_cycles, 1), initial_position_x, dtype = float), np.full((t_cycles, 1), initial_position_y, dtype = float), np.full((t_cycles, 1), initial_position_z, dtype = float), np.full((t_cycles, 1), initial_velocity_x, dtype = float), np.full((t_cycles, 1), initial_velocity_y, dtype = float), np.full((t_cycles, 1), initial_velocity_z, dtype = float), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1)), np.zeros((t_cycles, 1))


P = np.empty(0)

p0 = particle(1.989e30, 0, 0, 0, 0, 0, 0, 0)
P = np.append(P, p0)
p1 = particle(4.867e24, 0, 108e9, 0, 0, 0, 35e3, 0)
P = np.append(P, p1)
p2 = particle(5.972e24, 0, 149.6e9, 0, 0, 0, 29.8e3, 0)
P = np.append(P, p2)
p3 = particle(6.39e23, 0, 228e9, 0, 0, 0, 24e3, 0)
P = np.append(P, p3)


for k in range(1, t_cycles):
    for i in range(0, int(float(np.shape(P)[0]))):
        for j in range(0, int(float(np.shape(P)[0]))):
            print("i = " + str(i))
            print("j = " + str(j))
            if i != j:
                print("i = " + str(i))
                print("j = " + str(j))    
                f_x = (-c.G*P[i].mass*P[j].mass)/(P[j].position_x[k] - P[i].position_x[k])
                f_y = (-c.G*P[i].mass*P[j].mass)/(P[j].position_y[k] - P[i].position_y[k])
                f_z = (-c.G*P[i].mass*P[j].mass)/(P[j].position_z[k] - P[i].position_z[k])
                
                P[i].force_x[k] += f_x
                P[i].force_y[k] += f_y
                P[i].force_z[k] += f_z

            else:
                pass


#        a_x = P[i].force_x[k]/P[i].mass
#        a_y = P[i].force_y[k]/P[i].mass
#        a_z = P[i].force_z[k]/P[i].mass
#        
#        P[i].acceleration_x[k] = a_x
#        P[i].acceleration_y[k] = a_y
#        P[i].acceleration_z[k] = a_z            
#                    
#        
#        v_x = float(P[i].velocity_x[k - 1] + a_x*t_step/2)
#        v_y = float(P[i].velocity_y[k - 1] + a_y*t_step/2)
#        v_z = float(P[i].velocity_z[k - 1] + a_z*t_step/2)
#                    
#        P[i].velocity_x[k] = v_x
#        P[i].velocity_y[k] = v_y
#        P[i].velocity_z[k] = v_z
#                    
#                    
#        p_x = float(P[i].position_x[k - 1] + v_x*t_step)
#        p_y = float(P[i].position_y[k - 1] + v_y*t_step)
#        p_z = float(P[i].position_z[k - 1] + v_z*t_step)
#                    
#        P[i].position_x[k] = p_x
#        P[i].position_y[k] = p_y
#        P[i].position_z[k] = p_z
#        
#        t_step_array[k] = k
#
#plt.figure()
#plt.scatter(P[0].position_x, P[0].position_y)
#plt.scatter(P[1].position_x, P[1].position_y) 
#plt.scatter(P[2].position_x, P[2].position_y) 
#plt.scatter(P[3].position_x, P[3].position_y) 
#plt.show
#
#plt.figure()
#plt.scatter(t_step_array, P[1].force_y)
#plt.show