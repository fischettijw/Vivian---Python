# https://www.youtube.com/watch?v=Y0HN9tdLuJo&t=79s

import tkinter as tk
import time


class DigitalClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Digital Clock")
        self.clock_label = tk.Label(self.master, font=(
            "Arial", 80), bg="black", fg="white")
        self.clock_label.pack(fill=tk.BOTH, expand=1)
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.master.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
