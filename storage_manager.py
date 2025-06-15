# storage_manager.py
# This module handles saving and loading application state to and from JSON files.
# It uses static methods, so it doesn't need to be instantiated.

import json
from message import Message                                             # Used to reconstruct message objects from file data

class StorageManager:
                                                                        # A utility class responsible for all file I/O operations.

    @staticmethod
    def save_draft(editor, filename="draft.json"):
                                                                        # Saves the state of the message editor (message, undo/redo stacks) to a JSON file.
        with open(filename, "w", encoding="utf-8") as f:                # Open file in write mode with UTF-8 encoding
                                                                        # Create a dictionary with the editor's current state
            data_to_save = {
                "message": editor.message,
                "undo_stack": editor.undo_stack,
                "redo_stack": editor.redo_stack
            }
                                                                        # Dump the dictionary to the file as a JSON string
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_draft(editor, filename="draft.json"):
                                                                        # Loads the editor's state from a JSON file.
        try:
            with open(filename, "r", encoding="utf-8") as f:            # Open file in read mode
                data = json.load(f)                                     # Load the JSON data from the file
                                                                        # Restore the editor's state from the loaded data
                editor.message = data["message"]
                editor.undo_stack = data["undo_stack"]
                editor.redo_stack = data["redo_stack"]
            print("draft loaded successfully.")
        except FileNotFoundError:
                                                                        # Handle the case where the draft file doesn't exist yet
            print("no draft found to load.")

    @staticmethod
    def save_queue(queue_manager, filename="queue.json"):
                                                                        # Serializes all messages from the queue manager into a list of dictionaries and saves to a file.
        all_msgs = []
                                                                        # Iterate through each priority queue
        for pr in queue_manager.queues:
                                                                        # Iterate through each message in the current queue
            for msg in queue_manager.queues[pr]:
                all_msgs.append(msg.to_dict())                          # Convert message object to a dictionary and add to the list
        
        with open(filename, "w", encoding="utf-8") as f:                # Open the file for writing
                                                                        # Save the list of message dictionaries to the JSON file
            json.dump(all_msgs, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_queue(queue_manager, filename="queue.json"):
                                                                        # Loads messages from a JSON file and repopulates the message queues.
        try:
            with open(filename, "r", encoding="utf-8") as f:            # Open the file for reading
                data = json.load(f)                                     # Load the list of message dictionaries
                                                                        # Iterate through each dictionary in the loaded data
                for item in data:
                                                                        # Recreate the message object from the dictionary
                    msg = Message.from_dict(item) 
                                                                        # Add the restored message object to its corresponding priority queue
                    queue_manager.queues[msg.priority].append(msg)
            print("queue loaded successfully.")
        except FileNotFoundError:
                                                                        # Handle the case where the queue file doesn't exist
            print("no queue found to load.")
