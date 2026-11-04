# Password Security Checker

A beginner-friendly Python desktop project that checks password strength locally.

## Features

- Checks password length and character variety.
- Identifies a few predictable patterns.
- Shows a strength label and improvement suggestions.
- Includes a show/hide password option.
- Runs locally: it does not save, log, or transmit passwords.

## Requirements

- Python 3.9 or newer
- Tkinter (usually included with standard Python on Windows)

No third-party Python packages are required.

## Run on Windows

1. Install Python from https://www.python.org/downloads/
2. Download and extract this project ZIP.
3. Open the extracted folder.
4. Open Command Prompt in that folder.
5. Run:

```bash
python password_checker.py
```

## Run on Linux

```bash
python3 password_checker.py
```

If Tkinter is missing on a Debian/Kali-based system, install the operating-system package:

```bash
sudo apt install python3-tk
```

## Project structure

```text
Password_Security_Checker/
├── password_checker.py
├── README.md
└── .gitignore
```

## Important security note

This is an educational strength estimator, not a guarantee that a password is secure.
It does not check whether a password has appeared in known data breaches. Do not enter
a real password that you currently use; test with sample passwords instead.

For better account security, use a unique password or passphrase for every account
and enable multi-factor authentication where available.
