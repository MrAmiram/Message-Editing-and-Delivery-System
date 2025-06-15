# main.py
# This is the main entry point for the application.
# It sets up the graphical user interface (GUI) using Tkinter and integrates all the modules.

import tkinter as tk
from tkinter import messagebox
from editor import MessageEditor
from queue_manager import MessageQueue
from network import NetworkManager

                                                                                                                    # Pop-up Display Function
def show_popup(message):                                                                            
                                                                                                                    # A simple utility function to show informational pop-up messages to the user.
    messagebox.showinfo("Status", message)

                                                                                                                    # Initialize Core Modules 
                                                                                                                    # Create instances of the core components of our application.
editor = MessageEditor()
                                                                                                                    # Pass the popup function as a callback so the queue can display messages.
queue = MessageQueue(message_callback=show_popup)
                                                                                                                    # The network manager needs access to the queue to send messages when it comes online.
network = NetworkManager(queue, message_callback=show_popup)

                                                                                                                    # Tkinter Window 
                                                                                                                    # Set up the main application window.
root = tk.Tk()
root.title("Message Editor and Sender System")
root.geometry("600x500")                                                                                            # Set a fixed size for the window.
root.resizable(False, False)                                                                                        # Prevent the window from being resized.

                                                                                                                    # Network Status Label
                                                                                                                    # This label displays the current network status (Online/Offline).
status_label = tk.Label(root, text="Network: Offline", fg="red", font=("Arial", 12))
status_label.pack(pady=5)

def toggle_network():
                                                                                                                    # This function is called when the "Toggle Online/Offline" button is clicked.
    network.toggle_status()                                                                                         # Change the network state.
    status = network.status()                                                                                       # Get the new status string.
                                                                                                                    # Update the label's text and color based on the new status.
    status_label.config(text=f"Network: {status.capitalize()}", fg="green" if status == "online" else "red")

                                                                                                                    # Create the button to toggle the network status.
tk.Button(root, text="Toggle Online/Offline", command=toggle_network).pack()

                                                                                                                    # Text Area for Message 
                                                                                                                    # This is the main text box where the user composes their message.
text_area = tk.Text(root, height=10, font=("Arial", 12))
text_area.pack(padx=10, pady=10)

                                                                                                                    # Editor Button Functions 
                                                                                                                    # These functions connect the editor buttons to the MessageEditor's methods.
def update_text_area():
                                                                                                                    # A helper function to refresh the text area with the editor's current message.
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, editor.get_message())

def write_text():
                                                                                                                    # Appends the current text in the text_area to the editor's message.
    editor.write(text_area.get("1.0", tk.END).strip())
    update_text_area()

def undo_text():
                                                                                                                    # Reverts the last change in the editor.
    editor.undo()
    update_text_area()

def redo_text():
                                                                                                                    # Re-applies the last undone change in the editor.
    editor.redo()
    update_text_area()

def delete_last_word():
                                                                                                                    # Deletes the last word from the editor's message.
    editor.delete_last_word()
    update_text_area()

def clear_text():
                                                                                                                    # Clears the editor's message completely.
    editor.clear()
    update_text_area()

                                                                                                                    # Editor Buttons
                                                                                                                    # A separator line for visual clarity.
tk.Frame(root, height=1, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=5, pady=5)

                                                                                                                    # A frame to hold the editor action buttons in a grid layout.
edit_frame = tk.Frame(root)
edit_frame.pack()

tk.Button(edit_frame, text="Set Text", command=write_text).grid(row=0, column=0, padx=5)
tk.Button(edit_frame, text="Undo", command=undo_text).grid(row=0, column=1, padx=5)
tk.Button(edit_frame, text="Redo", command=redo_text).grid(row=0, column=2, padx=5)
tk.Button(edit_frame, text="Delete Last Word", command=delete_last_word).grid(row=0, column=3, padx=5)
tk.Button(edit_frame, text="Clear", command=clear_text).grid(row=0, column=4, padx=5)

                                                                                                                    # Message Metadata Frame 
                                                                                                                    # This frame contains input fields for the message receiver and priority.
send_frame = tk.Frame(root)
send_frame.pack(pady=10)

tk.Label(send_frame, text="Receiver:").grid(row=0, column=0)
receiver_entry = tk.Entry(send_frame)
receiver_entry.grid(row=0, column=1, padx=5)

tk.Label(send_frame, text="Priority (1-5):").grid(row=0, column=2)
priority_entry = tk.Entry(send_frame, width=5)
priority_entry.grid(row=0, column=3)
priority_entry.insert(0, "3")                                                                                       # Set default priority to 3.

def add_to_queue():
                                                                                                                    # This function takes the message from the editor and adds it to the sending queue.
    msg = editor.get_message()
    receiver = receiver_entry.get()
    priority = priority_entry.get()
    if not msg or not receiver:
                                                                                                                    # Show a warning if the message or receiver is missing.
        messagebox.showwarning("Warning", "Please enter both a message and a receiver.")
        return
                                                                                                                    # Add the message to the queue.
    queue.enqueue(msg, receiver, priority)                                                                  
                                                                                                                    # Clear the editor and text area for the next message.
    clear_text() 
    messagebox.showinfo("Success", "Message added to queue.")

                                                                                                                    # The button to trigger the add_to_queue function.
tk.Button(send_frame, text="Add to Queue", command=add_to_queue).grid(row=0, column=4, padx=10)

                                                                                                                    # Message Operations (Send / History)
                                                                                                                    # Functions for sending messages and viewing history.
def send_next():
    queue.send_next(network)

def send_all():
    queue.send_all(network)

def show_history():
                                                                                                                    # Creates a new pop-up window to display the sent message history.
    history_win = tk.Toplevel(root)
    history_win.title("Sent Message History")
    history_text = tk.Text(history_win, height=10, width=50)
    history_text.pack(padx=5, pady=5)
                                                                                                                    # Get the last 5 sent messages from the queue's sent_stack.
    history_items = queue.sent_stack[-5:]
    if not history_items:
        history_text.insert(tk.END, "No messages have been sent yet.")
    else:
        for i, msg in enumerate(reversed(history_items), 1):
            history_text.insert(tk.END, f"{i}. To {msg.receiver} (Prio {msg.priority}): {msg.text}\n")
    history_text.config(state=tk.DISABLED)                                                                          # Make the history text read-only.

                                                                                                                    # Another visual separator.
tk.Frame(root, height=1, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=5, pady=10)

                                                                                                                    # A frame for the final action buttons.
action_frame = tk.Frame(root)
action_frame.pack()

tk.Button(action_frame, text="Send Next", command=send_next).grid(row=0, column=0, padx=10)
tk.Button(action_frame, text="Send All", command=send_all).grid(row=0, column=1, padx=10)
tk.Button(action_frame, text="Show History", command=show_history).grid(row=0, column=2, padx=10)

                                                                                                                    # Run GUI Loop
                                                                                                                    # This line starts the Tkinter event loop, which listens for user actions.
root.mainloop()
