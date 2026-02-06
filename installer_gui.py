import tkinter as tk
from tkinter import filedialog
import os
import shutil

FILES = ["doc1.wsa", "doc2.wsb", "doc3.wsc", "doc4.wsd"]

class Installer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WS 설치 마법사")
        self.geometry("450x250")

        self.install_path = tk.StringVar()
        self.install_path.set(os.path.join(os.path.expanduser("~"), "Documents", "WS"))

        self.label = tk.Label(self, text="WS 프로그램 설치", font=("Arial", 14))
        self.label.pack(pady=10)

        self.path_label = tk.Label(self, textvariable=self.install_path)
        self.path_label.pack(pady=5)

        self.choose_btn = tk.Button(self, text="설치 경로 선택", command=self.choose_path)
        self.choose_btn.pack(pady=5)

        self.install_btn = tk.Button(self, text="설치", command=self.install)
        self.install_btn.pack(pady=15)

        self.result = tk.Label(self, text="")
        self.result.pack()

    def choose_path(self):
        folder = filedialog.askdirectory()
        if folder:
            self.install_path.set(os.path.join(folder, "WS"))

    def install(self):
        path = self.install_path.get()
        os.makedirs(path, exist_ok=True)

        for f in FILES:
            if os.path.exists(f):
                shutil.copy(f, path)

        self.result.config(text="✅ 설치 완료!\n" + path)
        self.install_btn.config(text="닫기", command=self.destroy)

if __name__ == "__main__":
    Installer().mainloop()
