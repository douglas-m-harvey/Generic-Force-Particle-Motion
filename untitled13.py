"Generic Force Particle Motion"

import numpy as np
import scipy.constants as c
import matplotlib.pyplot as plt

t_step = 3600
t_cycles = 24
t_step_array = np.zeros((t_cycles, 1))
debug_mode = 1


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
#p2 = particle(5.972e24, 0, 149.6e9, 0, 0, 0, 29.8e3, 0)
#P = np.append(P, p2)
#p3 = particle(6.39e23, 0, 228e9, 0, 0, 0, 24e3, 0)
#P = np.append(P, p3)


def force_gravity(P, k):
    for i in range(0, int(float(np.shape(P)[0]))):
        f_x = 0
        f_y = 0
        f_z = 0
        for j in range(0, int(float(np.shape(P)[0]))):
            if i != j:
                
                radius = np.sqrt(float((P[j].position_x[k] - P[i].position_x[k])**2 + (P[j].position_y[k]                            - P[i].position_y[k])**2 + (P[j].position_z[k] - P[i].position_z[k])**2))
                
                f_x = (-c.G*P[i].mass*P[j].mass)*(P[j].position_x[k] - P[i].position_x[k])/radius**3
#                print("force on " + str(i) + " from " + str(j) + " = " + str(f_x))
                f_y = (-c.G*P[i].mass*P[j].mass)*(P[j].position_y[k] - P[i].position_y[k])/radius**3
                f_z = (-c.G*P[i].mass*P[j].mass)*(P[j].position_z[k] - P[i].position_z[k])/radius**3
        
                P[i].force_x[k] += f_x
                P[i].force_y[k] += f_y
                P[i].force_z[k] += f_z  
            else:
                pass
        
    return()

def acceleration(P, k):
    for i in range(0, int(float(np.shape(P)[0]))):
        a_x = P[i].force_x[k]/P[i].mass
        a_y = P[i].force_y[k]/P[i].mass
        a_z = P[i].force_z[k]/P[i].mass
        
        P[i].acceleration_x[k] = a_x
        P[i].acceleration_y[k] = a_y
        P[i].acceleration_z[k] = a_z  
    return()

def velocity(P, k):
    for i in range(0, int(float(np.shape(P)[0]))):
        v_x = float(P[i].velocity_x[k - 1] + P[i].acceleration_x[k]*t_step)
        v_y = float(P[i].velocity_y[k - 1] + P[i].acceleration_y[k]*t_step)
        v_z = float(P[i].velocity_z[k - 1] + P[i].acceleration_z[k]*t_step)
                    
        P[i].velocity_x[k] = v_x
        P[i].velocity_y[k] = v_y
        P[i].velocity_z[k] = v_z
    return()
    
def position(P, k):
    for i in range(0, int(float(np.shape(P)[0]))):
        p_x = float(P[i].position_x[k - 1] + P[i].velocity_x[k]*t_step)
        p_y = float(P[i].position_y[k - 1] + P[i].velocity_y[k]*t_step)
        p_z = float(P[i].position_z[k - 1] + P[i].velocity_z[k]*t_step)
                    
        P[i].position_x[k] = p_x
        P[i].position_y[k] = p_y
        P[i].position_z[k] = p_z
    return()
    

for k in range(0, t_cycles + 1):
    t_step_array[k] = k
    print(str(k) + ": " + str(P[1].position_x[k]))
    force_gravity(P, k)
    acceleration(P, k)
    velocity(P, k)
    position(P, k + 1) "THIS DOESN'T WORK YET"
    print(str(k) + ": " + str(P[1].position_x[k]))
    
if debug_mode == 1:
            
    print("P[1].force_x = " + str(P[1].force_x) + "end")
    #print("P[1].force_y = " + str(P[1].force_y) + "end")
    #print("P[1].force_y = " + str(P[1].force_z) + "end")
    
    print("P[1].acceleration_x = " + str(P[1].acceleration_x) + "end")
    #print("P[1].acceleration_y = " + str(P[1].acceleration_y) + "end")
    #print("P[1].acceleration_z = " + str(P[1].acceleration_z) + "end")
    
    print("P[1].velocity_x = " + str(P[1].velocity_x) + "end")
    #print("P[1].velocity_y = " + str(P[1].velocity_y) + "end")
    #print("P[1].velocity_z = " + str(P[1].velocity_z) + "end")
    
    print("P[1].position_x = " + str(P[1].position_x) + "end")
    #print("P[1].position_y = " + str(P[1].position_y) + "end")
    #print("P[1].position_z = " + str(P[1].position_z) + "end")
    
    plt.figure()
    plt.scatter(t_step_array, P[1].force_x)
    plt.show()
    
    plt.figure()
    plt.scatter(t_step_array, P[1].acceleration_x)
    plt.show()
    
    plt.figure()
    plt.scatter(t_step_array, P[1].velocity_x)
    plt.show
    
    plt.figure()
    plt.scatter(t_step_array, P[1].position_x)
    plt.show