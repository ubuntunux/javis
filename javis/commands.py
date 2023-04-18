import os

def run_command(app, cmd):
    if cmd == 'clear' or cmd == 'cls':
        app.clear_output()
    elif cmd == 'dir' or cmd == 'ls':
        for content in os.listdir():
            print(content)
    else:
        return False
    return True