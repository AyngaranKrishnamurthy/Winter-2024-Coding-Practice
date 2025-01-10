class SubsystemA:
    def operation_a(self):
        return "Subsystem A operation"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B operation"

class Facade:
    def __init__(self):
        self._a = SubsystemA()
        self._b = SubsystemB()

    def simplified_operation(self):
        return f"{self._a.operation_a()} and {self._b.operation_b()}"
