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
        # traning
        def cmd_traning(args):
            if 6 == len(args):
                y,x,w,r,n = [eval(x) for x in args[1:]]
                w0 = 0.0
                for i in range(n):
                    predict = x*w+w0
                    error = y - predict
                    #print("p:%f, e:%f, x:%f, r:%f, w:%f, dw:%f" % (predict, error, x, r, w, r*error*x))
                    w += r * error * x
                    w0 += r * error
                    print("[%d] Goal: %f, Init: %f, Predict: %f, Error: %f, Weight: %f, Weight0: %f" % (i,y,x,predict,error,w,w0))
                return (w,w0)      
            else:
                print("ex) traning y(goal) x(init) w(weight) r(learning ratio) n(traning num)")
            return (0,0)
        self.commands["traning"] = cmd_traning
        
        # sum of series
        def cmd_sum_of_sequence(args):
            if 5 == len(args):
                target = args[1]
                s = lambda a, r, n, m: (m-n+1)*(2*a+r*(n+m-2))/2
                print(s(*[eval(x) for x in args[1:]]))
            else:
                print("ex) sum_of_sequence a r n m",args)
        self.commands["sum_of_sequence"] = cmd_sum_of_sequence
        
        # clear
        def cmd_clear(*args):
            app.clear_output()
        self.commands["clear"] = cmd_clear
        self.commands["cls"] = cmd_clear
        
        # dir
        def cmd_dir(*args):
            for content in os.listdir():
                print(content)
        self.commands["dir"] = cmd_dir
        self.commands["ls"] = cmd_dir
        
        # change dir           
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
        
        # memo
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
        
        
    
