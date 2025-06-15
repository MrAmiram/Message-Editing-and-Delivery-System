# queue_manager.py
# This module manages message queues, including sending, history, and storage.

from collections import deque                                                   # Import deque for efficient queue operations (append/popleft)
from message import Message                                                     # Import the Message class to create message objects
from storage_manager import StorageManager                                      # Import StorageManager for saving and loading the queue state

class MessageQueue:                                         
                                                                                # Manages multiple message queues with different priorities
    def __init__(self, message_callback=None):                                  # Initializes the message queue
        self.queues = {i: deque() for i in range(1, 6)}                         # Create 5 priority queues (1-5)
        self.sent_stack = []                                                    # Stack to store a history of sent messages
        self.message_callback = message_callback                                # A callback function to display messages in the UI

    def set_callback(self, callback):                                           # Sets a callback function for UI updates
        self.message_callback = callback                            

    def enqueue(self, text, receiver, priority="3"):                            # Creates a new message and adds it to the appropriate queue
        msg = Message(text, receiver, priority)                                 # Create a Message object
        self.queues[msg.priority].append(msg)                                   # Add the message to the queue corresponding to its priority

    def send_next(self, network_manager):                                       # Sends the next message from the highest priority queue
                                                                                # First, check the internet connection status
        if not network_manager.is_online:
            if self.message_callback:
                                                                                # If offline, display a message to the user
                self.message_callback("You are offline. Cannot send messages.")
            return                                                              # And exit the function

                                                                                # Loop through queues from highest priority (1) to lowest (5)
        for pr in range(1, 6):
            if self.queues[pr]:
                                                                                # If there's a message in the current priority queue
                msg = self.queues[pr].popleft()                                 # Get the message from the front of the queue
                print(f"send message to {msg.receiver}: {msg.text}")            # Simulate sending the message
                self.sent_stack.append(msg)                                     # Add the sent message to the history
                return                                                          # Exit the function after sending one message

        print("no messages to send.")                                           # This message is shown if all queues are empty

    def send_all(self, network_manager):                                        # Sends all messages currently in all queues
                                                                                # First, check the internet connection status
        if not network_manager.is_online:
            if self.message_callback:
                self.message_callback("You are offline. Cannot send messages.")
            return

                                                                                # Keep sending as long as there is at least one message in any queue
        while any(self.queues[p] for p in self.queues):
            self.send_next(network_manager)                                     # Send messages one by one

    def print_history(self):                                                    # Prints the last 5 sent messages
        print("\nRecent sent messages:")
                                                                                # Loop over the last 5 items of the history stack in reverse order
        for i, msg in enumerate(reversed(self.sent_stack[-5:]), 1):
            print(f"{i}. to {msg.receiver} ({msg.priority}): {msg.text}")

    def delete_by_index(self, priority_level, index):                           # Deletes a message from a queue by its index
        try:
                                                                                # Find the queue for the given priority level
            queue = self.queues[int(priority_level)]
            del queue[index]                                                    # Delete the message at the specified index
            print("message deleted successfully.")
        except:
                                                                                # Handle cases where the priority or index is invalid
            print("invalid index or priority level.")

    def save_queue(self):                                                       # Saves the current state of the queues to a file
        StorageManager.save_queue(self)                                         # The saving task is delegated to StorageManager

    def load_queue(self):                                                       # Loads the queue state from a file
        StorageManager.load_queue(self)                                         # The loading task is delegated to StorageManager
