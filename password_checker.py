"""
Password Security Checker
A local-only password strength checker. Passwords are evaluated on this device
and are never saved, logged, or sent over a network.
"""

import re
import tkinter as tk
from tkinter import ttk, messagebox


def assess_password(password: str):
    """Return a score, label, and improvement tips."""
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 10:
        score += 1
    else:
        tips.append("Use at least 12 characters.")

    checks = [
        (r"[a-z]", "Add lowercase letters."),
        (r"[A-Z]", "Add uppercase letters."),
        (r"\d", "Add numbers."),
        (r"[^A-Za-z0-9]", "Add symbols (such as !, #, or %)."),
    ]

    for pattern, tip in checks:
        if re.search(pattern, password):
            score += 1
        else:
            tips.append(tip)

    if password and re.search(r"(.)\1{2,}", password):
        score -= 1
        tips.append("Avoid repeating the same character several times.")

    if re.search(r"1234|abcd|qwerty|password", password, re.IGNORECASE):
        score -= 1
        tips.append("Avoid common words and predictable sequences.")

    score = max(0, min(score, 6))
    if not password:
        label = "Not checked"
    elif score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    else:
        label = "Strong"

    if password and not tips:
        tips.append("Good work. Consider using a unique passphrase for every account.")

    return score, label, tips


class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Security Checker")
        self.root.geometry("520x410")
        self.root.minsize(460, 370)

        main = ttk.Frame(root, padding=22)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main, text="Password Security Checker",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")

        ttk.Label(
            main,
            text="Check password strength locally. Your password is not stored or transmitted.",
            wraplength=460
        ).pack(anchor="w", pady=(6, 18))

        ttk.Label(main, text="Enter a password:").pack(anchor="w")
        self.password_var = tk.StringVar()
        self.entry = ttk.Entry(main, textvariable=self.password_var, show="•", width=48)
        self.entry.pack(fill="x", pady=(5, 8))
        self.entry.bind("<KeyRelease>", self.check)

        self.show_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            main, text="Show password", variable=self.show_var,
            command=self.toggle_visibility
        ).pack(anchor="w")

        self.result_var = tk.StringVar(value="Strength: Not checked")
        ttk.Label(
            main, textvariable=self.result_var,
            font=("Segoe UI", 13, "bold")
        ).pack(anchor="w", pady=(18, 6))

        self.progress = ttk.Progressbar(main, maximum=6, mode="determinate")
        self.progress.pack(fill="x", pady=(0, 12))

        ttk.Label(main, text="Suggestions:").pack(anchor="w")
        self.tips_box = tk.Text(main, height=6, wrap="word", state="disabled")
        self.tips_box.pack(fill="both", expand=True, pady=(5, 10))

        ttk.Button(main, text="Clear", command=self.clear).pack(anchor="e")

        self.root.bind("<Control-l>", lambda _event: self.clear())
        self.entry.focus_set()

    def toggle_visibility(self):
        self.entry.configure(show="" if self.show_var.get() else "•")

    def check(self, _event=None):
        password = self.password_var.get()
        score, label, tips = assess_password(password)
        self.result_var.set(f"Strength: {label}")
        self.progress["value"] = score

        self.tips_box.configure(state="normal")
        self.tips_box.delete("1.0", "end")
        if password:
            for tip in tips:
                self.tips_box.insert("end", f"• {tip}\n")
        else:
            self.tips_box.insert("end", "Type a password to see suggestions.")
        self.tips_box.configure(state="disabled")

    def clear(self):
        self.password_var.set("")
        self.check()
        self.entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    PasswordCheckerApp(root)
    root.mainloop()
