
# 🖱️ AutoClicker — Simple Tkinter Auto Clicker

<img width="428" height="363" alt="Screenshot 2026-05-11 180005" src="https://github.com/user-attachments/assets/f2dd9b06-6f12-4fd4-8b15-c96c9667e864" />

A lightweight and easy‑to‑use auto clicker built with **Python**, **Tkinter**, and the **mouse** / **keyboard** libraries.  
You choose the number of clicks per second, press **Start**, and the program clicks automatically until you press **ESC**.

---

## 🚀 Features

- Set custom **Clicks Per Second (CPS)**
- Clean and colorful **Tkinter GUI**
- Start/Stop with buttons or **ESC hotkey**
- Error handling for invalid input
- Info popup when pressing **I**
- Smooth clicking using `root.after()` scheduling

---

## 📦 Installation

### 1. Install Python (if you don’t have it)
Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Install required libraries

```bash
pip install mouse,keyboard
```

Tkinter comes with Python by default.

### 3. Run the program

```bash
python autoclicker.py
```

---

## ▶️ Usage

1. Enter the number of **clicks per second**  
2. Press **Start**  
3. The auto clicker begins clicking immediately  
4. Press **ESC** or the **Exit** button to stop

You can also press **I** to show an information popup.

---

## 🧩 Project Structure

```
autoclicker/
│── autoclicker.py     # Main application
│── README.md          # Project documentation
```

---

## 🛠️ How It Works

- The user enters CPS → program converts it to delay in milliseconds  
- Tkinter’s `root.after()` schedules repeated clicks  
- `mouse.click()` performs the actual clicking  
- `keyboard.add_hotkey('esc', exit_app)` stops the clicker instantly  

---

## ⚠️ Disclaimer

Use this tool responsibly.  
Some games or applications may **ban automation tools**, so use at your own risk.

---

## 🤝 Contributing

Pull requests are welcome!  
If you want to add features (right‑click mode, hold‑to‑click, fixed coordinates, etc.), feel free to fork the project.

---

## 📄 License

MIT License — free to use, modify, and share.
