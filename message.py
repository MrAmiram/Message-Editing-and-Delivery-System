# message.py

import time

class Message:
    def __init__(self, text, receiver, priority="3", timestamp=None):
        self.text = text
        self.receiver = receiver
        self.priority = int(priority)  # اولویت عددی 1 (فوری) تا 5 (کمترین اهمیت)
        self.timestamp = timestamp or time.time()

    def to_dict(self):
        return {
            "text": self.text,
            "receiver": self.receiver,
            "priority": self.priority,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data["text"],
            receiver=data["receiver"],
            priority=data["priority"],
            timestamp=data["timestamp"]
        )

    def __str__(self):
        return f"[به {self.receiver} | اولویت {self.priority}] {self.text}"
