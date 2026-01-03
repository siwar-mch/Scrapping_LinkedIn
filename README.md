# 🔐 LinkedIn Automation with Playwright (Python)

## 📌 Project Overview

This project demonstrates **web automation using Python and Playwright** to simulate a realistic interaction with LinkedIn.

The script automates the following actions:

* Logging into LinkedIn
* Accessing the user's connections
* Opening a chat window
* Typing and sending a message using **human-like behavior**

This project was developed **strictly for educational purposes** as part of a university module related to **cybersecurity and web automation**.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand how modern web automation tools work
* Simulate human behavior to interact with dynamic web pages
* Study bot-detection mechanisms used by platforms like LinkedIn
* Apply good practices such as delays, event triggering, and error handling

---

## 🛠️ Technologies Used

* **Python 3**
* **Playwright (Sync API)**
* **Chromium Browser**

---

## 📂 Project Structure

```
project/
│
├── LinkedIn_scraper.py     # Main automation script
├── preuve_succes_m4c1.png  # Screenshot after successful execution
├── erreur_rapport.png      # Screenshot captured in case of error
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites

* Python 3.8 or higher
* pip (Python package manager)

### 2️⃣ Install Playwright

```bash
pip install playwright
```

### 3️⃣ Install Browser Dependencies

```bash
playwright install
```

---

## ▶️ How to Run the Script

1. Open a terminal in the project directory
2. Run the script using:

```bash
python LinkedIn_scraper.py
```

3. The browser will open and perform the automation visibly

---

## 🧠 How the Script Works

The script is divided into **three main steps**:

### 🔐 Step 1: Authentication

* Opens the LinkedIn login page
* Types the email and password using simulated human typing
* Waits for redirection to confirm successful login

### 👥 Step 2: Accessing Connections

* Navigates to the LinkedIn connections page
* Searches for the first available "Message" button
* Opens the chat window

### 💬 Step 3: Sending a Message

* Types the message character by character
* Uses random delays to simulate human behavior
* Sends the message using the send button or keyboard fallback

---

## 🧑‍💻 Human Typing Simulation

To avoid bot-like behavior, the script uses a custom function that:

* Types text one character at a time
* Adds random delays between keystrokes
* Triggers JavaScript events on the page

This approach improves realism and reliability during automation.

---

## 📸 Screenshots & Error Handling

* After a successful execution, a screenshot is taken as proof
* In case of failure, an error screenshot is automatically saved
* This helps with debugging and reporting

---

## ⚠️ Limitations

* CAPTCHA or two-factor authentication may block the script
* UI changes on LinkedIn may require selector updates
* Excessive automation may violate platform policies

---

## ⚖️ Ethical & Legal Notice

⚠️ **Important**:

This project is intended **only for educational and experimental purposes**.

* Do NOT use this script for spam or abusive behavior
* Always respect the terms of service of online platforms
* The author is not responsible for misuse of this project

---

## 🎓 Academic Context

This project was developed as part of a university course related to:

* Cybersecurity
* Web automation
* Bot detection and prevention

It aims to provide hands-on experience with real-world web technologies.

---

## ✅ Conclusion

This project highlights how web automation can be implemented responsibly to understand modern web security challenges. It provides practical insights into how platforms detect automated behavior and how human interaction can be simulated programmatically.

---

📌 *Thank you for reviewing this project.*
