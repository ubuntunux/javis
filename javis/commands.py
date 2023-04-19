import os

from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.widget import Widget

from javis import javis
from utility.kivy_helper import *

def run_command(cmd):
    app = javis.JavisApp.instance()
    if cmd == 'clear' or cmd == 'cls':
        app.clear_output()
    elif cmd == 'dir' or cmd == 'ls':
        for content in os.listdir():
            print(content)
    elif cmd == 'memo':
        memo = MemoApp(app)
        app.screen.add_widget(memo)
    else:
        return False
    return True

class MemoApp(Widget):
    def __init__(self, app):
        super(MemoApp, self).__init__()
        layout = ScatterLayout(size=(500, 400))
        create_rect(layout, (0.2, 0.1, 0.2, 0.9))
        self.add_widget(layout)
        #btn = Button(text='memo', size_hint=(1,1))
        #layout.add_widget(btn)
        
        
    
