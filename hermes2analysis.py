# Copyright 2019 MIT Rocket Team
import io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

Hermes2_datalog = "datalog.txt"

with open('DATALOG.TXT', 'r') as log:
    data = log.read()
    print(data)

print('\n')
print(data[0])

# Starts 9999
# Then, the time in microseconds
# Then accelerometer x
# a_y
# a_z
# internal temp
# Load cell (arbitrary)
# pressure tap
# another 9999

data_split = data.split('\n')
print(data_split[0])

start_index = 226137

times = data_split[start_index::9]
times = savgol_filter(times, 23, 9)
a_x = data_split[start_index+1::9]
a_y = data_split[start_index+2::9]
a_z = data_split[start_index+3::9]
inter_temp = data_split[start_index+4::9]
load_cell = data_split[start_index+5::9]
#load_cell = savgol_filter(load_cell, 7, 2)
pressure_tap = data_split[start_index+6::9]
pressure_tap = savgol_filter(pressure_tap, 7, 3)

x_axis = len(times)

plt.figure(0)
plt.plot(range(x_axis), times)
plt.savefig("time_figure.png")
# plt.show()

plt.figure(1)
plt.plot(range(x_axis), a_x)
plt.savefig("a_x.png")
# plt.show()

plt.figure(2)
plt.plot(range(x_axis), a_y)
plt.savefig("a_y.png")
# plt.show()

plt.figure(3)
plt.plot(range(x_axis), a_z)
plt.savefig("a_z.png")
# plt.show()

plt.figure(4)
plt.plot(range(x_axis), inter_temp)
plt.title("Hermes 2: MIT RT: Load Cell Raw Data Plot")
plt.savefig("inter_temp.png")
# plt.show()

x_axis = len(load_cell)
plt.figure(5)
plt.plot(range(x_axis), load_cell)
plt.title("Hermes 2: MIT RT: Load Cell Raw Data Plot")
plt.yticks([500,1000,1500,2000,2500,3000,3500,4000])
plt.savefig("load_cell.png")
# print(type(load_cell[0]))
# plt.show()

# Plot polyfit function
x_axis = []; load_cell_polyfit = []
for i in range(len(load_cell)):
    x_axis.append(float(i))
    load_cell_polyfit.append(float(load_cell[i]))
load_cell = np.polyfit(x_axis, load_cell_polyfit, 5)

def lc_polyf_function(x_point):
    # input an x (time) point
    # return 5th order polyfit to x point
    lc_polyf = 7.16316638e-19*x_point**5 + -5.22358440e-14*x_point**4 + 1.33691983e-09*x_point**3 + -1.41940613e-05*x_point**2 + 5.61645765e-02*x_point + 7.69260739e+02
    return lc_polyf

load_cell_polyfit = []
for i in range(len(load_cell)):
    load_cell_polyfit.append(lc_polyf_function(x_axis[i]))

x_axis = len(load_cell_polyfit)
plt.figure(6)
plt.plot(range(x_axis), load_cell_polyfit)
plt.title("Hermes 2: MIT RT: Load Cell Polyfit Data Plot")
plt.yticks([500,1000,1500,2000,2500,3000,3500,4000])
plt.savefig("load_cell_polyfit.png")
# print(type(load_cell[0]))
# plt.show()


x_axis = len(pressure_tap[10:])
plt.figure(7)
plt.plot(range(x_axis), pressure_tap[10:])
plt.savefig("pressure_tap.png")
# plt.show()


# More object oriented programming stuff below

# prepare for RT_plot_raw
data_list = [times, a_x, a_y, a_z, inter_temp, load_cell, pressure_tap]

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def RT_plot_raw(data_lines: object) -> object:
    # Input a number of txt based, string lists
    # output simple plots for MIT RT
    import matplotlib.pyplot as plt
    for i in range(len(data_lines)):
        data_line = data_lines[i]
        x_axis = len(data_line)
        plt.figure(i)
        plt.plot(range(x_axis), data_line)
        plt.savefig("{}.png".format(namestr(data_lines[i], globals())))
        # plt.show()

# RT_plot_raw(data_list)

print(a_z)