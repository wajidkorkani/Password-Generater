# 🛡️Password Generator

A sleek, lightweight Python application that generates secure, randomized passwords at the click of a button. Featuring a high-contrast red and black interface, this tool provides a quick way to generate 8-character strings for local use.

---

## 🚀 Features
* **One-Click Generation:** Instantly creates a new password.
* **Randomized Entropy:** Pulls from four distinct character pools (Uppercase, Lowercase, Numbers, and Symbols).
* **Dark Mode UI:** A minimalist "hacker-style" aesthetic built with `tkinter`.
* **Auto-Clear:** Automatically removes the old password before inserting the new one.

---

## 🛠️ How It Works
The application uses a "list of lists" structure to categorize different character types:
1. **Symbols:** `! @ # $ % ^ & * ( ) - + = { } [ ] | : ; < > . ? /`
2. **Digits:** `0-9`
3. **Lowercase:** `a-z`
4. **Uppercase:** `A-Z`

When the **Generate Password** button is pressed, the script randomly selects one of these four categories and then picks a random character from within that category, repeating the process until an 8-character string is formed.

---

## 📦 Installation & Usage

### **Prerequisites**
* **Python 3.x**
* **Tkinter** (Usually included with Python. If not, install via `pip install tk` or your system package manager).

### **Running the App**
1. **Save the code** to a file named `app.py`.
2. **Open your terminal** or command prompt.
3. **Run the script on windows:**
   ```bash
   python app.py
   ```
4. **Run the script on linux:**
   ```bash
   python3 app.py
   ```
5. **Click the "Generate Password" button** to see your new password appear in the entry field.