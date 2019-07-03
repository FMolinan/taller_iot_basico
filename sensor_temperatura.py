import RPi.GPIO as io
import os
import glob
import time


io.setmode(io.BOARD)
io.setwarnings(True)
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm strong_pullup=2')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.8)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

if __name__ == '__main__':
    while True:
        temp = read_temp()[0]
        print("La temperatura es: "+ str(temp))
        time.sleep(1)