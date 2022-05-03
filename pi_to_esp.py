#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        ser.write(b"Hello from Raspberry Pi!\n")
        #or
        #ser.write("Hello from Raspberry Pi!\n".encode('utf-8'))
        #or
        #ser.write("Hello from Raspberry Pi!\n".encode('ascii'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

#$ chmod +x bidirectional_serial_communication.py 
#$ ./bidirectional_serial_communication.py 