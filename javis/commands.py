import os
import traceback 
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.widget import Widget

from javis import javis
from utility.kivy_helper import *

class Commander:
    def __init__(self, app):
        self.app = app
        self.commands = {}
        self.regist_command(app)
        
    def get_commands(self):
        keys = list(self.commands.keys())
        keys.sort()
        return keys
        
    def run_command(self, cmd_text):
        app = javis.JavisApp.instance()
        cmds = cmd_text.strip().split()
        cmd = cmds[0]
        if cmd in self.commands:
            self.commands[cmd](cmds)
            return True
        return False

    def regist_command(self, app):
        def cmd_clear(*args):
            app.clear_output()
        self.commands["clear"] = cmd_clear
        self.commands["cls"] = cmd_clear
        
        def cmd_dir(*args):
            for content in os.listdir():
                print(content)
        self.commands["dir"] = cmd_dir
        self.commands["ls"] = cmd_dir
                    
        def cmd_change_directory(cmds):
            if 1 < len(cmds):
                target = cmds[1]
                try:
                    os.chdir(target)
                    print(os.getcwd())
                except:
                    print("No such file or directory: " + target)
            else:
                print("usage: cd directory")
        self.commands["cd"] = cmd_change_directory
        
        def cmd_memo(*args):
            memo = MemoApp(app)
            app.screen.add_widget(memo)
        self.commands["memo"] = cmd_memo
        
        return True

class MemoApp(Widget):
    def __init__(self, app):
        super(MemoApp, self).__init__()
        layout = ScatterLayout(size=(500, 400))
        create_rect(layout, (0.2, 0.1, 0.2, 0.9))
        self.add_widget(layout)
        #btn = Button(text='memo', size_hint=(1,1))
        #layout.add_widget(btn)
        
        
    
