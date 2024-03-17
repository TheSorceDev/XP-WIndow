import tkinter as tk
from tkinter import ttk

class WinXPWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Fensterattribute
        self.title("Windows XP Style Window")
        self.geometry("400x300")
        self.overrideredirect(True)  # Remove window frame

        # Hintergrundfarben
        self.bg_color = "#f0f0f0"
        self.title_bg_color = "#0058a3"
        self.title_fg_color = "white"
        self.content_bg_color = "#ffffff"

        # Titelbalken
        self.title_bar = tk.Frame(self, bg=self.title_bg_color, relief="raised", bd=1)
        self.title_bar.pack(side="top", fill="x")

        self.close_button = tk.Button(self.title_bar, text="\u00D7", bg=self.title_bg_color, fg=self.title_fg_color, bd=0, font=("Arial", 8, "bold"), command=self.quit)
        self.close_button.pack(side="right", padx=5, pady=2)

        self.title_label = tk.Label(self.title_bar, text="Windows XP Style Window", bg=self.title_bg_color, fg=self.title_fg_color, font=("Arial", 8, "bold"))
        self.title_label.pack(side="left", padx=5, pady=2)

        # Inhaltsbereich
        self.content = tk.Frame(self, bg=self.content_bg_color)
        self.content.pack(side="top", fill="both", expand=True)

        self.label = tk.Label(self.content, text="Content goes here", font=("Arial", 12), bg=self.content_bg_color)
        self.label.pack(padx=20, pady=20)

        # Ereignisverfolgung für Fensterbewegung
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.title_bar.bind("<B1-Motion>", self.on_move)

        # Variablen für Bewegungsverfolgung
        self._x = 0
        self._y = 0

        self.style = ttk.Style()
        self.style.theme_use('winnative')

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    app = WinXPWindow()
    app.mainloop()