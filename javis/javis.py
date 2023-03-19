from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from javis.memory import Memory
from javis.chairman import ChairMan
from javis.evaluator import Evaluator
from javis.listener import Listener
from logger.logger import Logger
from utility.kivy_helper import create_rect
from utility.singleton import SingletonInstane


class JavisApp(App, SingletonInstane):
    def __init__(self):
        super(JavisApp, self).__init__()
        self.logger = Logger.instance()
        self.logger.info(f'Run: {JavisApp.__name__}')

        self.memory = Memory()
        self.chairman = ChairMan(self.memory)
        self.evaluator = Evaluator(self.memory)
        self.listener = Listener(self.memory)

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

    @staticmethod
    def on_text_input(instance, value=None):
        Logger.instance().logger("Input:", instance.text)

    def build(self):
        layout = Widget(size_hint=(1.0, 1.0))

        # btn
        btn = Button(pos=(300, 100), size=(300, 100), text="Enter")
        layout.add_widget(btn)

        # text input
        float_layout = ScatterLayout(size=(600, 300))
        inner_layout = Widget(size_hint=(1, 1))
        create_rect(inner_layout, color=(1, 1, 1, 0.3))
        float_layout.add_widget(inner_layout)

        text_input = TextInput(text='Hello world', multiline=True, size_hint=(None, 1.0), size=(200, 200))
        text_input.bind(on_text_validate=self.on_text_input)
        text_input.bind(text=self.on_text_input)

        inner_layout.add_widget(text_input)
        layout.add_widget(float_layout)

        Clock.schedule_interval(self.update, 0)
        return layout

    def update(self, dt):
        pass

