import pyautogui as pt 
import pyperclip as pc 
from pynput.mouse import Controller , Button 
from time import sleep

from whatsapprespo import response


mouse = Controller ()

class WhatsApp: 
    #Starting Values
    def __init__(self,speed=.5,click_speed =.3 ):
        self.speed = speed 
        click_speed = click_speed 
        self.msg= ''
        self.last_msg = ''

    #To Open New Msg in whatsapp
    def new_msg(self):
     try: 
        #To locate green dot on screen with confidence level 
        position = pt.locateOnScreen('Images/green_dot.jpeg', confidence = .7)
        pt.moveTo(position[0:2],duration=self.speed)
        #Need to change this co-ordinates(-50,0) If your screen size is diff ,in order to open new message
        pt.moveRel(-50,0,duration=self.speed)
        pt.doubleClick(interval=self.speed)
     except  Exception as e :
        print('Exception (new_msg): ' , e)

    #To navigate to msg
    def nav_mess(self):
     try :
        #To locate clip on screen with confidence level 
        position = pt.locateOnScreen('Images/clip.jpeg', confidence = .7)
        pt.moveTo(position[0:2],duration=self.speed)
        #Need to change this co-ordinates(40,-55) If your screen size is diff ,in order to locate message
        pt.moveRel(40,-55,duration=self.speed)
     except  Exception as e :
        print('Exception (nav_msg): ' , e)
    
    #To Go to Text Box
    def text_box(self):
     try :
        #To locate clip on screen with confidence level 
        position = pt.locateOnScreen('Images/clip.jpeg', confidence = .7)
        pt.moveTo(position[0:2],duration=self.speed)
       #Need to change this co-ordinates(100,10) If your screen size is diff ,in order to click on text box
        pt.moveRel(100,10,duration=self.speed)
        pt.doubleClick(interval=self.speed)
     except  Exception as e :
        print('Exception (text_box): ' , e)

    #To Copy the Message
    def get_msg(self):
        #This will run after locating the message
        mouse.click(Button.left,3)
        sleep(self.speed)
        mouse.click(Button.right,1)
        sleep(self.speed)
        #Need to change (30,-130), If Copy option is on different location 
        pt.moveRel(30,-130 ,duration=self.speed)
        mouse.click(Button.left,1)

        self.message = pc.paste()
        print('User says:', self.message)

    #To send Message
    def send_msg(self):
     try:
            #Importing response function from whatsapprespo to give response to coppied message
            bot_respo=response(self.message)
            print('You say:',bot_respo)
            pt.typewrite(bot_respo,interval=.1)
            pt.typewrite('\n')
            #self.last_message =self.message        

     except Exception as e:
        print('Exception (send_msg):',e)    

wa_bot = WhatsApp(speed = .50, click_speed=.7)
sleep(2)

def chatbot():
  wa_bot.new_msg()
  wa_bot.nav_mess()
  wa_bot.get_msg()
  wa_bot.text_box()
  wa_bot.send_msg()

chatbot()