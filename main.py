"""Real time plotting of Microphone level using kivy
"""

'''[hex(x) for x in frames[0]]. If you want to get the actual 2-byte numbers use the format string '<H' with the struct module.
https://stackoverflow.com/questions/35970282/what-are-chunks-samples-and-frames-when-using-pyaudio
'''

'''
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.garden.graph import MeshLinePlot
from kivy_garden.graph import MeshLinePlot
#from kivy_garden.graph import Graph, LinePlot
from kivy.clock import Clock
from threading import Thread
#import audioop
#import pyaudio
from audiostream import get_output, AudioSample, get_input_sources, get_input
from android.permissions import request_permissions,Permission,check_permission
'''

#Real time plotting of Microphone level using kivy

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread
#import audioop
#import pyaudio
import random

def get_fake_mic_level():
    #source: http://stackoverflow.com/questions/26478315/getting-volume-levels-from-pyaudio-for-use-in-arduino
    #audioop.max alternative to audioop.rms

    global levels
    
    while True:
        print("we here")
        #mx = random.random()
        mx = random.randrange(200)
        #print(mx)
        print(levels)
        if len(levels) >= 100:
            levels = []
        levels.append(mx)


class Logic(BoxLayout):

    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        
        
    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.1)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/5) for i, j in enumerate(levels)]


class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    #get_level_thread = Thread(target = get_microphone_level)
    get_level_thread = Thread(target = get_fake_mic_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    RealTimeMicrophone().run()
    
