# main.py

import tkinter as tk
from tkinter import messagebox
from editor import MessageEditor
from queue_manager import MessageQueue
from network import NetworkManager

# Initialize core components
editor = MessageEditor()
queue = MessageQueue()
network = NetworkManager(queue)

# GUI setup
root = tk.Tk()
root.title("Message Editor and Sender System")
root.geometry("600x500")
root.resizable(False, False)

# --- Network Status ---
status_label = tk.Label(root, text="Network: Offline", fg="red", font=("Arial", 12))
status_label.pack(pady=5)

def toggle_network():
    network.toggle_status()
    status = network.status()
    status_label.config(text=f"Network: {status}", fg="green" if status == "Online" else "red")

tk.Button(root, text="Toggle Online/Offline", command=toggle_network).pack()

# --- Message Text Area ---
text_area = tk.Text(root, height=6, font=("Arial", 12))
text_area.pack(padx=10, pady=10)

# --- Editor Buttons ---
def write_text():
    editor.write(text_area.get("1.0", tk.END))
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, editor.get_message())

def undo_text():
    editor.undo()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, editor.get_message())

def redo_text():
    editor.redo()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, editor.get_message())

def delete_last_word():
    editor.delete_last_word()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, editor.get_message())

def clear_text():
    editor.clear()
    text_area.delete("1.0", tk.END)

tk.Frame(root, height=1, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=5, pady=5)

edit_frame = tk.Frame(root)
edit_frame.pack()

tk.Button(edit_frame, text="Add Text", command=write_text).grid(row=0, column=0, padx=5)
tk.Button(edit_frame, text="Undo", command=undo_text).grid(row=0, column=1, padx=5)
tk.Button(edit_frame, text="Redo", command=redo_text).grid(row=0, column=2, padx=5)
tk.Button(edit_frame, text="Delete Last Word", command=delete_last_word).grid(row=0, column=3, padx=5)
tk.Button(edit_frame, text="Clear", command=clear_text).grid(row=0, column=4, padx=5)

# --- Message Info (receiver and priority) ---
send_frame = tk.Frame(root)
send_frame.pack(pady=10)

tk.Label(send_frame, text="Receiver:").grid(row=0, column=0)
receiver_entry = tk.Entry(send_frame)
receiver_entry.grid(row=0, column=1, padx=5)

tk.Label(send_frame, text="Priority (1-5):").grid(row=0, column=2)
priority_entry = tk.Entry(send_frame, width=5)
priority_entry.grid(row=0, column=3)

def send_message():
    msg = editor.get_message()
    receiver = receiver_entry.get()
    priority = priority_entry.get()
    if not msg or not receiver:
        messagebox.showwarning("Warning", "Please enter message and receiver.")
        return
    queue.enqueue(msg, receiver, priority)
    editor.clear()
    text_area.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Message added to queue.")

tk.Button(send_frame, text="Add to Queue", command=send_message).grid(row=0, column=4, padx=10)

# --- Send and History Operations ---
def send_next():
    queue.send_next(network)

def send_all():
    queue.send_all(network)

def show_history():
    history_win = tk.Toplevel(root)
    history_win.title("Sent Message History")
    history_text = tk.Text(history_win, height=10)
    history_text.pack()
    for i, msg in enumerate(reversed(queue.sent_stack[-5:]), 1):
        history_text.insert(tk.END, f"{i}. To {msg.receiver} (Priority {msg.priority}): {msg.text}\n")

tk.Frame(root, height=1, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=5, pady=10)

action_frame = tk.Frame(root)
action_frame.pack()

tk.Button(action_frame, text="Send Next", command=send_next).grid(row=0, column=0, padx=10)
tk.Button(action_frame, text="Send All", command=send_all).grid(row=0, column=1, padx=10)
tk.Button(action_frame, text="Show History", command=show_history).grid(row=0, column=2, padx=10)

root.mainloop()
