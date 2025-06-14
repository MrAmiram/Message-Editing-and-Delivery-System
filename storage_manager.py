# storage_manager.py

import json
from message import Message

class StorageManager:
    @staticmethod
    def save_draft(editor, filename="draft.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({
                "message": editor.message,
                "undo_stack": editor.undo_stack,
                "redo_stack": editor.redo_stack
            }, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_draft(editor, filename="draft.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                editor.message = data["message"]
                editor.undo_stack = data["undo_stack"]
                editor.redo_stack = data["redo_stack"]
            print("پیش‌نویس پیام بارگذاری شد.")
        except FileNotFoundError:
            print("پیش‌نویسی برای بارگذاری وجود ندارد.")

    @staticmethod
    def save_queue(queue_manager, filename="queue.json"):
        all_msgs = []
        for pr in queue_manager.queues:
            for msg in queue_manager.queues[pr]:
                all_msgs.append(msg.to_dict())
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(all_msgs, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_queue(queue_manager, filename="queue.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    msg = Message.from_dict(item)
                    queue_manager.queues[msg.priority].append(msg)
            print("صف پیام‌ها بارگذاری شد.")
        except FileNotFoundError:
            print("صفی برای بارگذاری وجود ندارد.")
