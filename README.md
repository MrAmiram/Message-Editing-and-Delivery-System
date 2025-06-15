# Message Editing and Delivery System (Python + Tkinter)

A modular Python application that simulates a message editing and delivery system using stack and queue data structures. The project features a graphical user interface (GUI) built with Tkinter and supports offline/online network state simulation, message editing history, and priority-based sending.

سامانه‌ای مدولار به زبان پایتون که عملیات ویرایش و ارسال پیام را با استفاده از ساختارهای داده‌ای پشته و صف شبیه‌سازی می‌کند. این پروژه دارای رابط کاربری گرافیکی (GUI) با استفاده از Tkinter است و وضعیت شبکه (آنلاین/آفلاین)، تاریخچه ویرایش، و ارسال اولویت‌دار را پشتیبانی می‌کند.

---

## 🚀 Features / ویژگی‌ها

- **Undo/Redo message editing** using stacks  
  ویرایش پیام با قابلیت بازگردانی (Undo/Redo) با استفاده از پشته
- **Priority queue system** (1 to 5 levels)  
  سیستم صف با اولویت‌های عددی (۱ تا ۵)
- **Offline/Online simulation**  
  شبیه‌سازی وضعیت آفلاین/آنلاین
- **Automatic queue flushing when online**  
  ارسال خودکار پیام‌های صف در حالت آنلاین
- **Message history tracking**  
  نمایش تاریخچه پیام‌های ارسال‌شده
- **User-friendly GUI with pop-up notifications**  
  رابط کاربری ساده با اعلان‌های پاپ‌آپ
- **Modular code structure** for easy scaling and testing  
  ساختار کدنویسی ماژولار و قابل گسترش

---

## 📂 File Structure / ساختار فایل‌ها

| File | Description | توضیح |
|------|-------------|--------|
| `main.py` | GUI entry point that integrates all modules and manages user interactions | نقطه ورود برنامه و رابط گرافیکی که تمام ماژول‌ها را به هم متصل می‌کند |
| `editor.py` | Handles text editing, undo/redo logic using stacks | مدیریت عملیات ویرایش متن و پشته‌های undo/redo |
| `queue_manager.py` | Manages message queue with 5-level priority using `deque` | مدیریت صف پیام‌ها با اولویت‌های عددی با استفاده از `deque` |
| `network.py` | Controls online/offline state and triggers message sending | کنترل وضعیت شبکه و ارسال پیام‌ها در حالت آنلاین |
| `message.py` | Represents a single message object with serialization support | تعریف ساختار پیام و تبدیل به/از دیکشنری برای ذخیره‌سازی |
| `storage_manager.py` | Manages saving/loading of draft messages and queues | مدیریت ذخیره‌سازی و بازیابی پیش‌نویس‌ها و صف پیام‌ها |

---

## 🧪 How to Run / نحوه اجرا

```bash
python main.py
```
Make sure all required files are in the same directory.  
اطمینان حاصل کنید که همه فایل‌های مورد نیاز در یک پوشه قرار دارند.

---

## 🛠 Requirements / پیش‌نیازها

- Python 3.8 or higher  
  پایتون نسخه ۳.۸ یا بالاتر
- Standard libraries only:  
  فقط کتابخانه‌های استاندارد پایتون:
  - `tkinter`
  - `collections`
  - `json`
  - `time`

If `tkinter` is not installed:  
اگر `tkinter` نصب نیست:
```bash
# Debian/Ubuntu
sudo apt install python3-tk
```

---
## 📸 Screenshots

Below are some screenshots from the GUI:

### ➤ Main Interface

![Main Window with online network](screenshots/network%20online.png)
![Main Window with offline network](screenshots/network%20offline.png)

### ➤ Write and Message with Details

![Write and Message with Details](screenshots/write%20and%20send.png)

### ➤ Pop-up Message Example

![Popup1](screenshots/pop-up%20window.png)
![Popup2](screenshots/popo-up%20window%202.png)

### ➤ History of messages

![History of messages](screenshots/history%20message.png)




---

## 📘 Educational Purpose / هدف آموزشی
This project was created as a final-term assignment for a Data Structures course, showcasing real-world use of stacks and queues with modular architecture and user interface integration.  
این پروژه به‌عنوان تمرین پایانی درس ساختمان داده‌ها طراحی شده است و کاربرد عملی پشته‌ها و صف‌ها را با معماری ماژولار و رابط کاربری گرافیکی نشان می‌دهد.

---

## ✨ Author / نویسنده
Mr.Amiram 
Project completed in 2025  
تکمیل‌شده در سال ۲۰۲۵
