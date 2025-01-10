class OldSystem:
    def request(self):
        return "Request from old system"

class NewSystem:
    def new_request(self):
        return "Request from new system"

class Adapter:
    def __init__(self, new_system):
        self.new_system = new_system

    def request(self):
        return self.new_system.new_request()
