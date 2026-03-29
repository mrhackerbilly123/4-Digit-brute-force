# 🔓 4-Digit Password Brute Force Simulation (Python)

A simple Python script that demonstrates how a 4-digit numeric password can be guessed using brute force.  
This project shows how weak short passwords are and why stronger security practices matter.

---

## 📌 Overview

This script:

- Takes a 4-digit password from the user
- Validates the input
- Simulates a brute force attack by trying all combinations from `0000` to `9999`
- Stops when the correct password is found

You use this to understand how brute force attacks work in a controlled environment.

---

## ⚙️ Features

- Input validation (must be exactly 4 digits)
- Automated password guessing
- Real-time attempt display
- Zero-padded guessing (`0000 → 9999`)

---

## 🛠️ How It Works

- User enters a 4-digit password
- Program checks:
  - Length is 4
  - All characters are digits
- Script loops through all possible combinations:
  - Converts numbers to 4-digit format using `zfill(4)`
  - Prints each attempt
- When match is found:
  - Displays the password
  - Stops execution

---

## ▶️ Usage

### 1. Run the script
```bash
python brute_force.py
