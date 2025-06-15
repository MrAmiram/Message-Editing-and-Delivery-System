# message.py
# This module defines the Message class, which represents a single message object.
import time                                                                 # Used to generate timestamps for messages
class Message:
                                                                            # Represents a message with content, a recipient, priority, and a timestamp.
    def __init__(self, text, receiver, priority="3", timestamp=None):
                                                                            # Initializes a new Message object.
        self.text = text                                                    # The content of the message.
        self.receiver = receiver                                            # The recipient of the message.
        self.priority = int(priority)                                       # The priority level, 1 (highest) to 5 (lowest).
        self.timestamp = timestamp or time.time()                           # Use a provided timestamp or create a new one.

    def to_dict(self):
                                                                            # Converts the Message object to a dictionary for easy serialization (e.g., to JSON).
        return {
            "text": self.text,
            "receiver": self.receiver,
            "priority": self.priority,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
                                                                            # A class method to create a Message instance from a dictionary.
                                                                            # This is useful for deserialization (e.g., from JSON).
        return cls(
            text=data["text"],
            receiver=data["receiver"],
            priority=data["priority"],
            timestamp=data["timestamp"]
        )

    def __str__(self):
                                                                            # Returns a user-friendly string representation of the message.
        return f"[To {self.receiver} | Priority {self.priority}] {self.text}"
