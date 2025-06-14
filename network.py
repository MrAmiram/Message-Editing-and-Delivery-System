# network.py

class NetworkManager:
    def __init__(self, message_queue=None, message_callback=None):
        self.is_online = False
        self.message_queue = message_queue
        self.message_callback = message_callback
    
    def set_callback(self, callback):
        self.message_callback = callback

    def connect_queue(self, queue):
        self.message_queue = queue

    def go_offline(self):
        self.is_online = False
        if self.message_callback:
            self.message_callback("Network status: Offline")

    def go_online(self):
        self.is_online = True
        if self.message_callback:
            self.message_callback("Network status: Online")
        if self.message_queue:
            self.message_queue.send_all(self)

    def toggle_status(self):
        if self.is_online:
            self.go_offline()
        else:
            self.go_online()

    def status(self):
        return "online" if self.is_online else "ofline"
