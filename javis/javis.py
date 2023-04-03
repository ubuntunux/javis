import os.path

from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
from kivy.metrics import Metrics
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard
from kivy.logger import Logger

from javis.constants import *
from javis.memory import Memory
from javis.chairman import ChairMan
from javis.evaluator import Evaluator
from javis.listener import Listener
from utility.kivy_helper import *
from utility.singleton import SingletonInstane


class JavisApp(App, SingletonInstane):
    def __init__(self):
        super(JavisApp, self).__init__()
        Logger.info(f'Run: {JavisApp.__name__}')
        
        self.memory = Memory()
        self.chairman = ChairMan(self.memory)
        self.evaluator = Evaluator(self.memory)
        self.listener = Listener(self.memory)
        self.screen_helper = None

        # # create
        # chairman_thread = Thread(target=chairman, args=[memory])
        # listener_thread = Thread(target=listener, args=[memory])
        # evaluator_thread = Thread(target=evaluator, args=[memory])
        #
        # # start
        # chairman_thread.start()
        # evaluator_thread.start()
        # listener_thread.start()
        #
        # # end
        # listener_thread.join(0.1)
        # evaluator_thread.join(0.1)
        # chairman_thread.join(0.1)
        # initialize config
        
    def destroy(self):
        with open(javis_output_file, 'w') as f:
            f.write(self.output.text)

    def on_stop(self):
        self.listener.destroy()
        self.destroy()
        Config.write()
        
    def build(self):
        # Window.maximize()
        Window.softinput_mode = 'below_target'
        # keyboard_mode: '', 'system', 'dock', 'multi', 'systemanddock', 'systemandmulti'
        Config.set('kivy', 'keyboard_mode', 'system')
        Window.configure_keyboards()
        
        self.root = Widget()
        self.screen_helper = ScreenHelper(size=Window.size)
        self.root.add_widget(self.screen_helper.screen_manager)
        screen = Screen(name="javis")
        self.screen_helper.add_screen(screen)
        self.screen_helper.current_screen(screen)
        
        layout = BoxLayout(orientation='vertical', size=(1, 1))
        screen.add_widget(layout)
         
        
        output = ''
        if os.path.exists(javis_output_file):
            with open(javis_output_file, 'r') as f:
                output = f.read()
                
        self.output = TextInput(
            text=output,
            halign='left',
            readonly=True,
            font_name='fonts/NanumGothic_Coding.ttf',
            font_size="12dp",
            multiline=True,
            size_hint=(1, 2),
            background_color=(1, 1, 1, 0),
            foreground_color=(1, 1, 1, 1)
        )
        layout.add_widget(self.output)

        listener_widget = self.listener.initialize(self, self.output, height='100sp', size_hint=(1, None))
        layout.add_widget(listener_widget)

        Clock.schedule_interval(self.update, 0)
        return self.root

    def update(self, dt):
        pass

