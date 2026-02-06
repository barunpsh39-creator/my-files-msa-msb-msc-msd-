import tkinter as tk
import shutil
import os

BASE = os.path.join(os.path.expanduser("~"), "Documents", "WS")

class DeleteGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WS 삭제")
        self.geometry("400x200")

        self.label = tk.Label(self, text="WS 프로그램을 삭제할까요?", font=("Arial", 12))
        self.label.pack(pady=30)

        self.button = tk.Button(self, text="삭제", command=self.delete)
        self.button.pack()

    def delete(self):
        if os.path.exists(BASE):
            shutil.rmtree(BASE)
            self.label.config(text="🗑 삭제 완료!")
        else:
            self.label.config(text="이미 삭제되어 있습니다")

        self.button.config(text="닫기", command=self.destroy)

if __name__ == "__main__":
    DeleteGUI().mainloop()
