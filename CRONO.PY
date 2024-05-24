import tkinter as tk
from playsound import playsound
import threading

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")
        self.master.geometry("300x200")

        self.time_left = 60  # 1 minuto em segundos
        self.label = tk.Label(master, text="01:00", font=("Helvetica", 48))
        self.label.pack(expand=True)

        self.update_clock()

    def play_tick(self):
        threading.Thread(target=playsound, args=('/tick.mp3',)).start()

    def update_clock(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            time_format = f"{minutes:02}:{seconds:02}"

            if self.time_left <= 15:
                self.label.config(fg="red")

            if (self.time_left == 18) or (self.time_left == 17) or (self.time_left == 16):
                self.play_tick()
            if (self.time_left == 3) or (self.time_left == 2) or (self.time_left == 1):
                self.play_tick()

            self.label.config(text=time_format)
            self.time_left -= 1
            self.master.after(1000, self.update_clock)
        else:
            self.label.config(text="00:00")

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
