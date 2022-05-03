import telepot
import serial
import time
import os
from picamera import PiCamera
from datetime import datetime
path=os.getenv("HOME")
bot = telepot.Bot('5245859702:AAEBW54A2E7LCqwnHsexIEZOUt6N3zZ3Y10')
id = '5116513926'
# set up the serial line
# ser = serial.Serial('COM3', 115200)
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Defaults to open
global currentState
global currentStateMessage

time.sleep(2)
# Read and record the data
data =[]                       # empty list to store the data

# Handling message from Telegram
def handleMessage(msg):
     global currentState
     global currentStateMessage
     id = msg['chat']['id'];
     command = msg['text'];
     print ('Command ' + command + ' from chat id' + str(id)); 
     if (command == '/photo'):   
       print ("Taking picture…");   
       # Initialize the camera   
       camera = PiCamera();   
       camera.start_preview()   
       camera.capture(path + '/pic.jpg',resize=(640,480))   
       time.sleep(2)   
       camera.stop_preview()   
       camera.close()   
       # Seding picture   
       bot.sendPhoto(id, open(path + '/pic.jpg', 'rb'))
     elif (command == '/status'):
       print("Sending current status...");
       state = currentState;
       message = currentStateMessage
       bot.sendMessage(id, message);
     elif (command == '/help'):
       print("Sending help...");
       message = "Commands: \n/photo: Take a picture \n/status: Get the current status \n/help: Get this message"
       bot.sendMessage(id, message);
     else:     
       bot.sendMessage(id, "Command not found..")
 
#bot.message_loop(handleMessage);
#print ("Listening to bot messages….");
#while 1:
#    time.sleep(10);

def main():
    global currentState
    global currentStateMessage
    # Update State and Take Picture if Needed
    try:
        for i in range(50):
            b = ser.readline()         # read a byte string
            string_n = b.decode()  # decode byte string into Unicode  
            string = string_n.rstrip() # remove \n and \r
            try:
                flt = float(string)
                bot.message_loop(handleMessage);
                print ("Listening to bot messages….");
                if flt == 1.0:
                    print("Door is closed")
                    currentState = 1.0
                    currentStateMessage = str(datetime.now()) + " Door is closed"
                elif flt == 0.0:
                    print("Door is open")
                    currentState = 0.0
                    currentStateMessage = str(datetime.now()) + " Door is open"
                    print ("Taking picture…");   
                    # Initialize the camera   
                    camera = PiCamera();   
                    camera.start_preview()   
                    camera.capture(path + '/pic.jpg',resize=(640,480))   
                    time.sleep(2)   
                    camera.stop_preview()   
                    camera.close()   
                    # Seding picture   
                    bot.sendPhoto(id, open(path + '/pic.jpg', 'rb'))
                #print(flt)
                data.append(flt)           # add to the end of data list
                time.sleep(0.1)            # wait (sleep) 0.1 seconds
            except ValueError:
                pass
    except KeyboardInterrupt:
        pass

    ser.close()
    # show the data

    for line in data:
        print(line)

# Run main
if __name__ == '__main__':
	main()