#TESTING RASPBERRY PI TO TELEGRAM

import telepot
import time
import os
from picamera import PiCamera
import take_pic_with_esp
path=os.getenv("HOME")

# Handling message from Telegram
def handleMessage(msg):
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
     elif (command == '/state'):
       print ("Sending state…");
       state = take_pic_with_esp.currentState;
       if state == 1.0:
            message = "Door is closed";
       elif state == 0.0:
            message = "Door is open";
       bot.sendMessage(id, message);
     else:     
       bot.sendMessage(id, "Command not found..")
 
bot = telepot.Bot('5245859702:AAEBW54A2E7LCqwnHsexIEZOUt6N3zZ3Y10');
bot.message_loop(handleMessage);
print ("Listening to bot messages….");
while 1:
    time.sleep(10);

#python3 telegrambot.py
#telegram /photo 