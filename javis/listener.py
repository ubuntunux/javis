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
from javis import commands
from utility.kivy_helper import create_rect, create_dynamic_rect


class Listener:
    def __init__(self, memory):
        self.memory = memory
        self.myGlobals = {}
        self.root_layout = None
        self.history = []
        self.history_index = -1
        self.multiline = False

        # initialize config
        if not Config.has_section(section_listener):
            Config.add_section(section_listener)

        if not Config.has_option(*config_listener_pos):
            Config.set(*config_listener_pos, (0, 0))
        Config.write()

    def initialize(self, app, height, size_hint):
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
            self.multiline = False
            prev_stdout = sys.stdout
            sys.stdout = StringIO()
            cmd = text_input.text.rstrip()

            if cmd != '' and (0 == len(self.history) or self.history[-1] != cmd):
                self.history.append(cmd)
                self.history_index = -1
            
            if cmd != '':
                print(">>>", cmd)

            if commands.run_command(cmd):
                pass
            elif cmd != '':
                try:
                    print(eval(cmd, self.myGlobals))
                except:
                    try:
                        exec(cmd, self.myGlobals)
                    except:
                        print(traceback.format_exc())
            output_text = sys.stdout.getvalue().rstrip()
            # print output
            app.print_output(output_text)
            
            sys.stdout = prev_stdout
            text_input.text = ''

        text_input = TextInput( text='', size_hint=(3, 1), auto_indent=True, font_name=app_font_name)

        text_input.bind(on_text_validate=partial(on_enter, text_input))
        input_layout.add_widget(text_input)

        def on_press_prev(inst):
            if self.multiline:
                return
            num_history = len(self.history)
            if 0 < num_history:
                if self.history_index < 0:
                    self.history_index = num_history - 1
                elif 0 < self.history_index:
                    self.history_index -= 1
                text_input.text = self.history[self.history_index]

        def on_press_next(inst):
            if self.multiline:
                return
            num_history = len(self.history)
            if 0 < num_history and 0 <= self.history_index < num_history:
                self.history_index += 1
                if self.history_index == num_history:
                    text_input.text = ''
                else:
                    text_input.text = self.history[self.history_index]
        
        def on_key_down(keyboard, keycode, key, modifiers):
            key_name = keycode[1]
            if key_name == 'enter' or key_name == 'numpadenter':
                if 'shift' in modifiers:
                    self.multiline = True
                elif 'ctrl' in modifiers:
                    self.multiline = False
                # run
                if not self.multiline:
                    on_enter(text_input, text_input)
            elif key_name == 'up':
                on_press_prev(None)
            elif key_name == 'down':
                on_press_next(None)

        def keyboard_closed(*args):
            pass

        keyboard = Window.request_keyboard(keyboard_closed, text_input)
        keyboard.bind(on_key_down=on_key_down)
        text_input.focus = True

        btn_enter = Button(size_hint=(1, 1), text="Run")
        btn_enter.bind(on_press=partial(on_enter, text_input))
        input_layout.add_widget(btn_enter)

        def on_clear(*args):
            app.clear_output()

        btn_enter = Button(size_hint=(1, 1), text="Clear")
        btn_enter.bind(on_press=on_clear)
        input_layout.add_widget(btn_enter)

        # prev
        btn_prev = Button(size_hint=(0.5, 1), text="<<")
        top_layout.add_widget(btn_prev)
        btn_prev.bind(on_press=on_press_prev)

        # next
        btn_next = Button(size_hint=(0.5, 1), text=">>")
        top_layout.add_widget(btn_next)
        btn_next.bind(on_press=on_press_next)

        # quit
        def on_press_quit(inst):
            app.stop()
        btn_quit = Button(size_hint=(0.5, 1), text="Quit")
        top_layout.add_widget(btn_quit)
        btn_quit.bind(on_press=on_press_quit)

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
