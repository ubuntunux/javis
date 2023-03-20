from functools import partial
from threading import Thread
import time
import traceback

from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

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

    def initialize(self):
        listener_pos = eval(Config.get(*config_listener_pos))

        self.root_layout = ScatterLayout(pos=listener_pos, size=('600sp', '80sp'), do_rotation=False, do_scale=False)
        create_dynamic_rect(self.root_layout, color=(1, 1, 1, 0.1))

        # inner layout
        inner_layout = BoxLayout(orientation='vertical')
        self.root_layout.add_widget(inner_layout)

        # top layout
        top_layout = BoxLayout(orientation='horizontal', width='600sp', size_hint=(1.0, 1.0), padding='4sp')
        inner_layout.add_widget(top_layout)
        label = Label(text="Javis", font_size='30sp', halign='right')
        top_layout.add_widget(label)

        # input_layout
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1.0, 1.0), padding='4sp')
        inner_layout.add_widget(input_layout)

        # text layout
        def on_enter(instance):
            try:
                print(eval(instance.text, self.myGlobals))
            except:
                try:
                    exec(instance.text, self.myGlobals)
                except:
                     print(traceback.format_exc())
            instance.text = ''
            instance.focus = True

        def on_focus(inst, value):
            if not value:
                inst.focus = True
        text_input = TextInput(text='Hello world', size_hint=(3, 1), multiline=False, auto_indent=True)
        text_input.bind(on_text_validate=on_enter)
        text_input.bind(focus=on_focus)
        input_layout.add_widget(text_input)

        # button
        def callback(instance):
            config.set('listener_pos', self.root_layout.pos)
            config.save()
        btn_enter = Button(size_hint=(1, 1), text="Enter")
        btn_enter.bind(on_press=callback)
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
