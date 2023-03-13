from enum import Enum
from threading import Thread
import time


class MachineState(Enum):
    Boot = 0
    Normal = 1
    PrepareToExit = 2
    Exit = 3


class WillingType(Enum):
    Nothing = 0
    ShouldExit = 1


class Job:
    def __init__(self):
        self.name = None
        self.type = None


class evaluatorData:
    def __init__(self):
        self.willing_type = WillingType.Nothing


class ListenerData:
    def __init__(self):
        self.listen_data = None


class Memory:
    def __init__(self):
        self.master_name = None
        self.machine_state = MachineState.Boot
        self.listener_data = ListenerData()
        self.evaluator_data = evaluatorData()


def chairman(memory: Memory):
    while True:
        time.sleep(0)
        if memory.evaluator_data.willing_type == WillingType.ShouldExit:
            memory.machine_state = MachineState.PrepareToExit
            break
    print("end - chairman")


def evaluator(memory: Memory):
    while True:
        time.sleep(0)

        if type(memory.listener_data.listen_data) is str and memory.listener_data.listen_data.lower().startswith(
                "quit"):
            memory.evaluator_data.willing_type = WillingType.ShouldExit

        if memory.machine_state == MachineState.PrepareToExit:
            break
    print("end - evaluator")


def listener(memory: Memory):
    while True:
        memory.listener_data.listen_data = input("listen: ")
        print(">>", memory.listener_data.listen_data)
        if memory.machine_state == MachineState.PrepareToExit:
            break
    print("end - listener")


def main():
    memory = Memory()
    # create
    chairman_thread = Thread(target=chairman, args=[memory])
    listener_thread = Thread(target=listener, args=[memory])
    evaluator_thread = Thread(target=evaluator, args=[memory])

    # start
    chairman_thread.start()
    evaluator_thread.start()
    listener_thread.start()

    # end
    listener_thread.join(0.1)
    evaluator_thread.join(0.1)
    chairman_thread.join(0.1)
    print("bye")


if __name__ == "__main__":
    main()
