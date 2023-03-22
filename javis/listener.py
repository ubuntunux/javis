import os
from functools import partial
from io import StringIO
import sys
from threading import Thread
import time
import traceback

from kivy.core.window import Window
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer

from javis.constants import *
from utility.kivy_helper import create_rect, create_dynamic_rect


class Listener:
    def __init__(self, memory):
        self.memory = memory
        self.myGlobals = {}
        self.root_layout = None

        # initialize config
        if not Config.has_section(section_listener):
            Config.add_section(section_listener)

        if not Config.has_option(*config_listener_pos):
            Config.set(*config_listener_pos, (0, 0))
        Config.write()

    def initialize(self, output, height, size_hint):
        # inner layout
        self.root_layout = BoxLayout(orientation='vertical', height=height, size_hint=size_hint)
        create_dynamic_rect(self.root_layout, color=(1, 1, 1, 0.1))

        # top layout
        top_layout = BoxLayout(orientation='horizontal', size_hint=(1.0, 1.0), padding='4sp')
        self.root_layout.add_widget(top_layout)
        label = Label(text="Javis", font_size='30sp', halign='right')
        top_layout.add_widget(label)

        # input_layout
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1.0, 1.0), padding='4sp')
        self.root_layout.add_widget(input_layout)

        # text layout
        def on_enter(text_input, instance):
            prev_stdout = sys.stdout
            sys.stdout = StringIO()
            cmd = text_input.text.rstrip()
            if cmd == 'clear' or cmd == 'cls':
                output.text = ''
            if cmd == 'dir' or cmd == 'ls':
                for content in os.listdir():
                    print(content)
            else:
                print(">>>", cmd)
                try:
                    print(eval(cmd, self.myGlobals))
                except:
                    try:
                        exec(cmd, self.myGlobals)
                    except:
                        print(traceback.format_exc())
            output.text = '\n'.join([output.text, sys.stdout.getvalue()]).rstrip()
            sys.stdout = prev_stdout
            text_input.text = ''

        text_input = TextInput( text='', size_hint=(3, 1), font_name='fonts/NanumGothic_Coding.ttf')

        text_input.bind(on_text_validate=partial(on_enter, text_input))
        input_layout.add_widget(text_input)
        
        def on_key_down(keyboard, keycode, key, modifiers):
            if keycode[1] == 'enter' or keycode[1] == 'numpadenter':
                on_enter(text_input, text_input)
            # if not text_input.focus:
            #     text_input.focus = True

        def keyboard_closed(*args):
            pass

        keyboard = Window.request_keyboard(keyboard_closed, text_input)
        keyboard.bind(on_key_down=on_key_down)
        text_input.focus = True

        btn_enter = Button(size_hint=(1, 1), text="Run")
        btn_enter.bind(on_press=partial(on_enter, text_input))
        input_layout.add_widget(btn_enter)

        def on_clear(*args):
            output.text = ''

        btn_enter = Button(size_hint=(1, 1), text="Clear")
        btn_enter.bind(on_press=on_clear)
        input_layout.add_widget(btn_enter)

        return self.root_layout

    def destroy(self):
        Config.set(*config_listener_pos, self.root_layout.pos)

    def update_listener(self):
        while True:
            self.memory.listener_data.listen_data = input("listen: ")
            print(">>", self.memory.listener_data.listen_data)
            if self.memory.machine_state == MachineState.PrepareToExit:
                break
        print("end - listener")
