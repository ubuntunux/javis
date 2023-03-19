from threading import Thread
import time


class Listener:
    def __init__(self, memory):
        self.memory = memory

    def update_listener(self):
        while True:
            self.memory.listener_data.listen_data = input("listen: ")
            print(">>", self.memory.listener_data.listen_data)
            if self.memory.machine_state == MachineState.PrepareToExit:
                break
        print("end - listener")
