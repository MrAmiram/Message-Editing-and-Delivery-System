# queue_manager.py

from collections import deque
from message import Message
from storage_manager import StorageManager

class MessageQueue:
    def __init__(self, message_callback=None):
        self.queues = {i: deque() for i in range(1, 6)}
        self.sent_stack = []
        self.message_callback = message_callback
    
    def set_callback(self, callback):
        self.message_callback = callback

    def enqueue(self, text, receiver, priority="3"):
        msg = Message(text, receiver, priority)
        self.queues[msg.priority].append(msg)

    def send_next(self, network_manager):
        if not network_manager.is_online:
            if self.message_callback:
                self.message_callback("You are offline. Cannot send messages.")
            return
        
        for pr in range(1, 6):
            if self.queues[pr]:
                msg = self.queues[pr].popleft()
                print(f"send message to {msg.receiver}: {msg.text}]")
                self.sent_stack.append(msg)
                return
        print("no messages to send.")

    def send_all(self, network_manager):
        if not network_manager.is_online:
            if self.message_callback:
                self.message_callback("You are offline. Cannot send messages.")
            return
        while any(self.queues[p] for p in self.queues):
            self.send_next(network_manager)

    def print_history(self):
        print("\nRecent sent messages:")
        for i, msg in enumerate(reversed(self.sent_stack[-5:]), 1):
            print(f"{i}. به {msg.receiver} ({msg.priority}): {msg.text}")

    def delete_by_index(self, priority_level, index):
        try:
            queue = self.queues[int(priority_level)]
            del queue[index]
            print("message deleted successfully.")
        except:
            print("invalid index or priority level.")

    def save_queue(self):
        StorageManager.save_queue(self)

    def load_queue(self):
        StorageManager.load_queue(self)
