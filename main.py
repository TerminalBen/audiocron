__version__ = '0.0.2'
#import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix import boxlayout
from kivy.uix import button
from kivy.clock import Clock
from datetime import timedelta,datetime
from kivy.core.audio import SoundLoader
import time
#from android.permissions import request_permissions,Permission
#request_permissions([Permission.READ_EXTERNAL_STORAGE])

init = SoundLoader.load('init.wav')
stop = SoundLoader.load('stop.wav')
sound0=SoundLoader.load('0.wav')
sound1=SoundLoader.load('1.wav')
sound2=SoundLoader.load('2.wav')
sound3=SoundLoader.load('3.wav')
sound4=SoundLoader.load('4.wav')
sound5=SoundLoader.load('5.wav')
sound6=SoundLoader.load('6.wav')
sound7=SoundLoader.load('7.wav')
sound8=SoundLoader.load('8.wav')
sound9=SoundLoader.load('9.wav')

class Myapp(App):
    def build(self):
        self.flag = 0
        self.clock = datetime.now()
        self.my_label = Label(text=datetime.now().strftime('%H:%M:%S'))
        self.layout = boxlayout.BoxLayout(padding=200)
        color=[1,0,0,1]
        btn=button.Button(text="Start",background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        btn1=button.Button(text="Stop",background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        Clock.schedule_interval(self.update_clock, 1)
        self.layout.add_widget(btn)
        self.layout.add_widget(btn1)
        self.layout.add_widget(self.my_label)
        btn.bind(on_press=self.startspeak)
        btn1.bind(on_press=self.stopspeak)
        return self.layout
        
    def speak(self,*args):
        self.min_now = datetime.now().minute
        min_str = "%02d"% self.min_now
        self.value = (min_str[1])
        if self.value == '0' and self.flag == 0:
            self.speak0()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 1
        elif self.value == '1' and self.flag ==1:
            self.speak1()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 2
        elif self.value == '2' and self.flag ==2:
            self.speak2()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 3
        elif self.value == '3' and self.flag ==3:
            self.speak3()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 4
        elif self.value == '4' and self.flag ==4:
            self.speak4()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 5
        elif self.value == '5' and self.flag ==5:
            self.speak5()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 6
        elif self.value == '6' and self.flag == 6:
            self.speak6()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 7
        elif self.value == '7' and self.flag == 7:
            self.speak7()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 8
        elif self.value == '8' and self.flag == 8:
            self.speak8()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 9
        elif self.value == '9' and self.flag == 9:
            self.speak9()
            #print(f'flag{self.flag} | min_now {self.value}')
            self.flag = 0

    def update_clock(self,*args):
        self.clock = self.clock + timedelta(seconds = 1)
        self.my_label.text =datetime.now().strftime('%H:%M:%S')
        

    def speak0(self):
        sound0.play()

    def speak1(self):
        sound1.play()
    
    def speak2(self):
        sound2.play()

    def speak3(self):
        sound3.play()
    
    def speak4(self):
        sound4.play()
    
    def speak5(self):
        sound5.play()
    
    def speak6(self):
        sound6.play()
    
    def speak7(self):
        sound7.play()
    
    def speak8(self):
        sound8.play()

    def speak9(self):
        sound9.play()

    def sound_init(self):
        init.play()
    
    def stop_sound(self):
        stop.play()

    """For debugging purposes only
    """
    def print_shit(self,*args):
       print(f'Print_shit -> flag:{self.flag} | min_now:{self.value}')
    
    def stopspeak(self,*args):
        self.stop_sound()
        Clock.unschedule(self.speak)
        Clock.unschedule(self.print_shit)
        
    def startspeak(self,*args):
        self.sound_init()
        time.sleep(2) 
        self.min_now = datetime.now().minute
        min_str = "%02d"% self.min_now
        self.value = (min_str[1])
        self.flag = int(min_str[1])
        Clock.schedule_interval(self.speak,1)       




if __name__ == '__main__':
    Myapp().run()