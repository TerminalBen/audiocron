__version__ = '0.0.1'
os.environ['KIVY_AUDIO']='ffpyplayer'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix import boxlayout
from kivy.uix import button
from kivy.clock import Clock
from datetime import timedelta,datetime
from kivy.core.audio import SoundLoader
import time
from android.permissions import request_permissions,Permission

request_permissions([Permission.READ_EXTERNAL_STORAGE])

class Myapp(App):
    def build(self):
        self.flag = 0
        self.original_time=datetime.now()
        self.clock = datetime.now()
        self.my_label = Label(text=datetime.now().strftime('%H:%M:%S'))
        self.layout = boxlayout.BoxLayout(padding=200)
        color=[1,0,0,1]
        btn=button.Button(text="Start",background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        btn1=button.Button(text="Stop",background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        btn2=button.Button(text='Restart',background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        Clock.schedule_interval(self.update_clock, 1)
        self.layout.add_widget(btn)
        self.layout.add_widget(btn1)
        self.layout.add_widget(btn2)
        self.layout.add_widget(self.my_label)
        btn.bind(on_press=self.startspeak)
        btn1.bind(on_press=self.stopspeak)
        btn2.bind(on_press=self.reset)
        return self.layout
        
    def speak(self,*args):
        self.now=datetime.now()
        min_now = self.now.minute
        min_og = self.original_time.minute
        diff = min_now - min_og
        if diff == 0 and self.flag == 0:
            self.speak0()
            self.flag=1
        elif diff==1 and self.flag == 1:
            self.speak1()
            self.flag = 2
        elif diff==2 and self.flag==2:
            self.speak2()
            self.flag=3
        elif diff==3 and self.flag ==3:
            self.speak3()
            self.flag=4
        elif diff==4 and self.flag==4:
            self.speak4()
            self.flag =5
        elif diff==5 and self.flag ==5:
            self.speak5()
            self.flag = 6
        elif diff==6 and self.flag ==6:
            self.speak6()
            self.flag =7
        elif diff==7 and self.flag ==7:
            self.speak7()
            self.flag =8
        elif diff==8 and self.flag ==8:
            self.speak8()
            self.flag =9
        elif diff==9 and self.flag ==9:
            self.speak9()
            self.flag = 10
        elif diff == 10 and self.flag==10:
            self.flag = 0
            self.original_time = datetime.now()
    
        
    def update_clock(self,*args):
        self.clock = self.clock + timedelta(seconds = 1)
        self.my_label.text =datetime.now().strftime('%H:%M:%S')
        

    def speak0(self,*args):
        sound=SoundLoader.load('0.wav')
        sound.play()

    def speak1(self,*args):
        sound=SoundLoader.load('1.wav')
        sound.play()
    
    def speak2(self,*args):
        sound=SoundLoader.load('2.wav')
        sound.play()

    def speak3(self,*args):
        sound=SoundLoader.load('3.wav')
        sound.play()
    
    def speak4(self,*args):
        sound=SoundLoader.load('4.wav')
        sound.play()
    
    def speak5(self,*args):
        sound=SoundLoader.load('5.wav')
        sound.play()
    
    def speak6(self,*args):
        sound=SoundLoader.load('6.wav')
        sound.play()
    
    def speak7(self,*args):
        sound=SoundLoader.load('7.wav')
        sound.play()
    
    def speak8(self,*args):
        sound=SoundLoader.load('8.wav')
        sound.play()

    def speak9(self,*args):
        sound=SoundLoader.load('9.wav')
        sound.play()
    
    def reset(self,*args):
        self.original_time = datetime.now()
        self.flag =0
        
    
    def stopspeak(self,*args):
        Clock.unschedule(self.speak)
        

    
    def startspeak(self,*args):
        self.original_time=datetime.now()
        Clock.schedule_interval(self.speak,1)
       




if __name__ == '__main__':
    Myapp().run()
