# network.py

class NetworkManager:
    def __init__(self, message_queue=None):
        self.is_online = False
        self.message_queue = message_queue

    def connect_queue(self, queue):
        self.message_queue = queue

    def go_offline(self):
        self.is_online = False
        print("network: offline")

    def go_online(self):
        self.is_online = True
        print("network: online")
        if self.message_queue:
            self.message_queue.send_all(self)

    def toggle_status(self):
        if self.is_online:
            self.go_offline()
        else:
            self.go_online()

    def status(self):
        return "online" if self.is_online else "ofline"
