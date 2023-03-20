from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.uix.widget import Widget
from kivy.logger import Logger

from javis.memory import Memory
from javis.chairman import ChairMan
from javis.evaluator import Evaluator
from javis.listener import Listener
from utility.singleton import SingletonInstane


class JavisApp(App, SingletonInstane):
    def __init__(self):
        super(JavisApp, self).__init__()
        Logger.info(f'Run: {JavisApp.__name__}')

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

    def build(self):
        Window.maximize()
        layout = Widget(size_hint=(1, 1))

        listener_widget = self.listener.initialize()
        layout.add_widget(listener_widget)

        Clock.schedule_interval(self.update, 0)
        return layout

    def update(self, dt):
        pass

