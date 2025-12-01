import tkinter as tk
from tkinter import ttk

class NumberFactsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Facts Program")
        self.root.geometry("400x420")
        self.root.resizable(False, False)


        self.themes = {
            "light": {
                "bg": "#F6F8FA",
                "frame": "#FFFFFF",
                "text": "#1F2328",
                "entry_bg": "#FFFFFF",
                "button_bg": "#0969DA",
                "button_fg": "#FFFFFF",
            },
            "dark": {
                "bg": "#0D1117",
                "frame": "#161B22",
                "text": "#C9D1D9",
                "entry_bg": "#0D1117",
                "button_bg": "#238636",
                "button_fg": "#FFFFFF",
            }
        }

        self.current_theme = "light"
        self.apply_theme()

       
        # UI Layout
        self.title_label = tk.Label(
            root, text="Number Facts Program", 
            font=("Segoe UI", 16, "bold"),
            bg=self.theme["bg"],
            fg=self.theme["text"]
        )
        self.title_label.pack(pady=(15, 5))

        self.frame = tk.Frame(root, bg=self.theme["frame"])
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Input Label
        self.input_label = tk.Label(
            self.frame, text="Enter a whole number:",
            font=("Segoe UI", 11),
            bg=self.theme["frame"], fg=self.theme["text"]
        )
        self.input_label.pack(pady=(15,5))

        # Entry Box
        self.num_entry = tk.Entry(
            self.frame, font=("Segoe UI", 12),
            bg=self.theme["entry_bg"], fg=self.theme["text"],
            justify="center"
        )
        self.num_entry.pack(ipady=4)

        # Analyze Button
        self.analyze_btn = tk.Button(
            self.frame, text="Analyze Number",
            font=("Segoe UI", 11, "bold"),
            bg=self.theme["button_bg"], fg=self.theme["button_fg"],
            command=self.analyze_number
        )
        self.analyze_btn.pack(pady=15, ipadx=10, ipady=4)

        # Result Box
        self.result_box = tk.Text(
            self.frame, height=8, width=36,
            font=("Segoe UI", 11),
            bg=self.theme["frame"], fg=self.theme["text"],
            bd=0
        )
        self.result_box.pack(pady=5)

        # Theme toggle button
        self.theme_btn = tk.Button(
            root, text="Toggle Light/Dark Mode",
            font=("Segoe UI", 10, "bold"),
            bg=self.theme["button_bg"], fg=self.theme["button_fg"],
            command=self.toggle_theme
        )
        self.theme_btn.pack(pady=10)

    
    # Apply Theme
    def apply_theme(self):
        self.theme = self.themes[self.current_theme]
        self.root.configure(bg=self.theme["bg"])


    # Toggle Theme
    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme()
        self.refresh_colors()

    # Update all widget colors
    def refresh_colors(self):
        widgets = [
            (self.title_label, "bg", "fg"),
            (self.input_label, "bg", "fg"),
            (self.frame, "bg", None),
            (self.num_entry, "bg", "fg"),
            (self.analyze_btn, "bg", "fg"),
            (self.result_box, "bg", "fg"),
            (self.theme_btn, "bg", "fg")
        ]

        for w, bg, fg in widgets:
            if bg: w.configure(bg=self.theme["frame"] if w in [self.frame, self.result_box] else self.theme["bg"])
            if fg: w.configure(fg=self.theme["text"])

        self.num_entry.configure(bg=self.theme["entry_bg"], fg=self.theme["text"])
        self.analyze_btn.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])
        self.theme_btn.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])

    
    # Analyze Number Logic
    def analyze_number(self):
        self.result_box.delete("1.0", tk.END)
        try:
            num = int(self.num_entry.get())
        except:
            self.result_box.insert(tk.END, "Please enter a valid whole number.")
            return

        # Conditions
        if num % 2 == 0:
            self.result_box.insert(tk.END, f"{num} is even.\n")
        else:
            self.result_box.insert(tk.END, f"{num} is odd.\n")

        if num > 0:
            self.result_box.insert(tk.END, f"{num} is positive.\n")
        elif num < 0:
            self.result_box.insert(tk.END, f"{num} is negative.\n")
        else:
            self.result_box.insert(tk.END, "The number is zero.\n")

        self.result_box.insert(tk.END, f"The square of {num} is {num*num}\n")


# Run The App
root = tk.Tk()
app = NumberFactsApp(root)
root.mainloop()
