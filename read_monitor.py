import serial
import time
# set up the serial line
ser = serial.Serial('COM3', 115200)
time.sleep(2)
# Read and record the data
data =[]                       # empty list to store the data
try:
    for i in range(50):
        b = ser.readline()         # read a byte string
        string_n = b.decode()  # decode byte string into Unicode  
        string = string_n.rstrip() # remove \n and \r
        try:
            flt = float(string)        # convert string to float
            if flt == 0.0:
                print("Door is closed")
            elif flt == 1.0:
                print("Door is open")
            #print(flt)
            data.append(flt)           # add to the end of data list
        except ValueError:
            pass
        time.sleep(0.1)            # wait (sleep) 0.1 seconds
except KeyboardInterrupt:
    pass

ser.close()
# show the data

for line in data:
    print(line)