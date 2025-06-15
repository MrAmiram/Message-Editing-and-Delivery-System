# network.py
# This module simulates network connectivity to demonstrate online/offline functionality.

class NetworkManager:
                                                                            # Manages the simulated network state (online/offline).

    def __init__(self, message_queue=None, message_callback=None):
                                                                            # Initializes the network manager.
        self.is_online = False                                              # Start in an offline state by default.
        self.message_queue = message_queue                                  # Reference to the message queue to trigger sending messages.
        self.message_callback = message_callback                            # A callback function to update the UI with status changes.

    def set_callback(self, callback):
                                                                            # Sets a new callback function for UI updates.
        self.message_callback = callback

    def connect_queue(self, queue):
                                                                            # Links the network manager to a message queue instance.
        self.message_queue = queue

    def go_offline(self):
                                                                            # Sets the network status to offline.
        self.is_online = False
        if self.message_callback:
                                                                            # Notify the UI that the status has changed to offline.
            self.message_callback("Network status: Offline")

    def go_online(self):
                                                                            # Sets the network status to online and attempts to send all queued messages.
        self.is_online = True
        if self.message_callback:
                                                                            # Notify the UI that the status has changed to online.
            self.message_callback("Network status: Online")
        if self.message_queue:
                                                                            # If a message queue is connected, tell it to send all pending messages.
            self.message_queue.send_all(self)

    def toggle_status(self):
                                                                            # Toggles the network status between online and offline.
        if self.is_online:
            self.go_offline()
        else:
            self.go_online()

    def status(self):
                                                                            # Returns the current network status as a string.
        return "online" if self.is_online else "offline"                    # Corrected the typo from "ofline" to "offline"
