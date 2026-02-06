import tkinter as tk
import os

BASE = os.path.join(os.path.expanduser("~"), "Documents", "WS")
CONFIG = os.path.join(BASE, "config.wsc")

class SetupGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WS 설정")
        self.geometry("400x200")

        self.label = tk.Label(self, text="WS 설정을 시작합니다", font=("Arial", 12))
        self.label.pack(pady=30)

        self.button = tk.Button(self, text="설정하기", command=self.setup)
        self.button.pack()

    def setup(self):
        if not os.path.exists(BASE):
            self.label.config(text="❌ WS가 설치되어 있지 않습니다")
            return

        config = """#WSC1
font=classic
size=12
color=white
"""

        with open(CONFIG, "w", encoding="utf-8") as f:
            f.write(config)

        self.label.config(text="✅ 설정 완료!\nconfig.wsc 생성됨")
        self.button.config(text="닫기", command=self.destroy)

if __name__ == "__main__":
    SetupGUI().mainloop()
