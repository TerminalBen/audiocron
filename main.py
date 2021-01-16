from kivy.app import App
from kivy.uix.label import Label
from kivy.uix import boxlayout
from kivy.uix import button
from kivy.clock import Clock
from kivy.properties import NumericProperty
import pyttsx3
import time

class Myapp(App):
    flag=0
    mytime=NumericProperty(0)
    def build(self):
        layout = boxlayout.BoxLayout(padding=200)
        color=[1,0,0,1]
        btn=button.Button(text="Iniciar",background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        btn1=button.Button(text="Parar",background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        btn2=button.Button(text='Reset',background_color=color,size_hint=(.5,.5),pos_hint={'center_x':.5,'center_y':.5})
        label=Label(text=str(self.mytime))
        layout.add_widget(btn)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(label)
        btn.bind(on_press=self.start_counting)
        btn1.bind(on_press=self.stop_counting)
        btn2.bind(on_press=self.reset)
        return layout


    def increment_time(self,interval):
        self.mytime+=1
        print(f'{self.mytime}')
 

    def start_counting(self,instance):
        self.flag=1
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time,1)
        Clock.schedule_interval(self.speak,10)
        #self.speak(self.increment_time)
        

    def stop_counting(self,instance):
        self.flag=0
        Clock.unschedule(self.increment_time)
        print(f'flag{self.flag}')
        print(f'tempo_stop:{self.mytime}')

    def reset(self,instance):
        self.mytime=0
        print(f'tempo:{self.mytime}')

    def speak(self,instance):
        #use pyttsx3 to speak
        if (self.mytime==10):
            engine =pyttsx3.init()
            engine.say("minute one!")
            engine.runAndWait()
            engine.stop()
        elif (self.mytime==20):
            engine =pyttsx3.init()
            engine.say("minute two!")
            engine.runAndWait()
            engine.stop()
        else:
            pass
                



        

if __name__ == '__main__':
    Myapp().run()
