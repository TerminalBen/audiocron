__version__ = '0.0.3'
#os.environ['KIVY_AUDIO']='ffpyplayer'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix import boxlayout
from kivy.uix import gridlayout
from kivy.uix import button
from kivy.clock import Clock
from datetime import timedelta,datetime
from kivy.core.audio import SoundLoader
import time
#from android.permissions import request_permissions,Permission
#request_permissions([Permission.READ_EXTERNAL_STORAGE])

class Myapp(App):
    def build(self):
        self.counter = 0
        self.aux=0
        self.original_time=datetime.now()#original time
        self.now=datetime.now() # for the clock only
        #self.min_now = int('{:02d}'.format(self.now.minute)[1]) #now time parsed
        #self.min_og = int('{:02d}'.format(self.original_time.minute)[1]) #original time parsed
        self.clock = datetime.now()
        self.my_label = Label(text=datetime.now().strftime('%H:%M:%S'))
        #self.layout = boxlayout.BoxLayout(spacing=2, orientation='vertical')
        self.layout= gridlayout.GridLayout(cols=1,spacing=2,padding = 100)
        red=[1,0,0,1]
        green = [0,1,0,1]
        yellow = [1,1,0,1]
        btn=button.Button(text="Start",background_color=green,size_hint=(0.5,0.5),font_size=50,pos_hint={'center_x':.5,'center_y':.5})
        btn1=button.Button(text="Stop",background_color=red,size_hint=(.5,.5),font_size=50,pos_hint={'center_x':.5,'center_y':.5})
        btn2=button.Button(text='Restart',background_color=yellow,size_hint=(.5,.5),font_size=50,pos_hint={'center_x':.5,'center_y':.5})
        Clock.schedule_interval(self.update_clock, 1)
        self.layout.add_widget(btn)
        self.layout.add_widget(btn1)
        self.layout.add_widget(btn2)
        self.layout.add_widget(self.my_label)
        btn.bind(on_press=self.startspeak)
        btn1.bind(on_press=self.stopspeak)
        btn2.bind(on_press=self.reset)
        return self.layout

        
    def count_changes(self,*args):
        self.agora = datetime.now()
        #self.diff = self.agora-self.original_time
        #self.diff_sec = int (self.diff.seconds/60)
        #print(f'diff_before:{self.diff_sec}')
        #if self.agora.minute == self.original_time.minute:
            #self.diff_sec =0
        #    self.counter =0
        if self.agora.minute != self.original_time.minute:
            self.counter +=1
            self.original_time=self.agora
            #self.diff_sec +=1
        #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        #return int(self.diff_sec)
        return self.counter
        
        
        
    def speak(self,*args):
        #x= self.count_changes()
        #print(x)
        if self.count_changes() == 0 and self.aux==0:
            self.speak0()
            self.aux=1
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 1 and self.aux==1:
            self.speak1()
            self.aux=2
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 2 and self.aux ==2:
            self.speak2()
            self.aux=3
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 3 and self.aux ==3:
            self.speak3()
            self.aux=4
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 4 and self.aux ==4:
            self.speak4()
            self.aux=5
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 5 and self.aux ==5:
            self.speak5()
            self.aux=6
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 6 and self.aux ==6:
            self.speak6()
            self.aux=7
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 7 and self.aux ==7:
            self.speak7()
            self.aux=8
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 8 and self.aux ==8:
            self.aux=9
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif self.count_changes() == 9 and self.aux ==9:
            self.speak9()
            self.aux=10
            #print(f'aux: {self.aux} ----- min_now:{self.agora.minute} --------min_og:{self.original_time.minute}------counter: {self.counter}')
        elif  self.count_changes() ==10 and self.aux==10:
            self.reset()
        

    def update_clock(self,*args):
        self.clock = self.clock + timedelta(seconds = 1)
        self.my_label.text =datetime.now().strftime('%H:%M:%S')
        
    def speak0(self,*args):
        sound=SoundLoader.load('0.wav')
        sound.play()
        time.sleep(2)
        sound.unload()

    def speak1(self,*args):
        sound=SoundLoader.load('1.wav')
        sound.play()
        time.sleep(2)
        sound.unload()
    
    def speak2(self,*args):
        sound=SoundLoader.load('2.wav')
        sound.play()
        time.sleep(2)
        sound.unload()

    def speak3(self,*args):
        sound=SoundLoader.load('3.wav')
        sound.play()
        time.sleep(2)
        sound.unload()
    
    def speak4(self,*args):
        sound=SoundLoader.load('4.wav')
        sound.play()
        time.sleep(2)
        sound.unload()
    
    def speak5(self,*args):
        sound=SoundLoader.load('5.wav')
        sound.play()
        time.sleep(2)
        sound.unload()
    
    def speak6(self,*args):
        sound=SoundLoader.load('6.wav')
        sound.play()
        time.sleep(2)
        sound.unload()
    
    def speak7(self,*args):
        sound=SoundLoader.load('7.wav')
        sound.play()
        time.sleep(2)
        sound.unload()
    
    def speak8(self,*args):
        sound=SoundLoader.load('8.wav')
        sound.play()
        time.sleep(2)
        sound.unload()

    def speak9(self,*args):
        sound=SoundLoader.load('9.wav')
        sound.play()
        time.sleep(2)
        sound.unload()

    

    def stop_sound(self,*args):
        sound=SoundLoader.load('stop.wav')
        sound.play()
        time.sleep(2)
        sound.unload()

    def reset(self,*args):
        #self.original_time = datetime.now()
        self.aux =0
        self.counter=0
        #self.agora = datetime.now()
        
    def stopspeak(self,*args):
        self.stop_sound()
        Clock.unschedule(self.speak)
        Clock.unschedule(self.count_changes)
        self.reset()
        
    def startspeak(self,*args):
        self.original_time=datetime.now()
        #Clock.schedule_interval(self.count_changes,1)
        Clock.schedule_interval(self.speak,1)
        self.init_sound()

    def init_sound(self,*args):
        sound=SoundLoader.load('init.wav')
        sound.play()
        #time.sleep(2)
        #sound.unload()
if __name__ == '__main__':
    Myapp().run()