class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action()

class Receiver:
    def action(self):
        print("Action performed!")

class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def invoke(self):
        self._command.execute()
