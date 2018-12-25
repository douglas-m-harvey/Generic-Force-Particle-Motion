import numpy as np

f0_x_arr = np.zeros((4, 1))
f0_y_arr = np.zeros((4, 1))
f0_z_arr = np.zeros((4, 1))
f1_x_arr = np.zeros((4, 1))
f1_y_arr = np.zeros((4, 1))
f1_z_arr = np.zeros((4, 1))
f2_x_arr = np.zeros((4, 1))
f2_y_arr = np.zeros((4, 1))
f2_z_arr = np.zeros((4, 1))
f3_x_arr = np.zeros((4, 1))
f3_y_arr = np.zeros((4, 1))
f3_z_arr = np.zeros((4, 1))
Px = np.array([f0_x_arr, f1_x_arr, f2_x_arr, f3_x_arr])
Py = np.array([f0_y_arr, f1_y_arr, f2_z_arr, f3_y_arr])
Pz = np.array([f0_x_arr, f1_y_arr, f2_z_arr, f3_z_arr])

for k in range(0, 4):
    for i in range(0, 4):
        for j in range(0, 4):
            if i != j:
                print(str(i) + str(j) + "No match")
                f_x = 1
                f_y = 1
                f_z = 1
                
                Px[i][k] += f_x
                Py[i][k] += f_y
                Pz[i][k] += f_z
    
            else:
                print(str(i) + str(j) + "Match")
            
print("Px = " + str(Px) + "end")
print("Py = " + str(Py) + "end")
print("Pz = " + str(Pz) + "end")