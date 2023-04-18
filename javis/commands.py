import os

from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout

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
        memo(app)
    else:
        return False
    return True
    
def memo(app):
    layout = ScatterLayout(size=(300, 300))
    create_rect(layout, (0.2, 0.1, 0.2, 0.9))
    #btn = Button(text='memo', size_hint=(1,1))
    #layout.add_widget(btn)
    app.screen.add_widget(layout)
    
