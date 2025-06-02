# 照護者 APP GUI
# 依照 VSC.md 規格實作的照護者介面

import tkinter as tk
from tkinter import ttk
import json
import datetime

class CaregiverApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Future Memory Cassette - 照護者介面")
        self.setup_gui()
        self.tasks = []
        self.load_tasks()
        
    def setup_gui(self):
        """設置 GUI 介面"""
        # 任務清單
        self.task_listbox = tk.Listbox(self.window, height=15, width=50)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind('<Double-Button-1>', self.show_task_details)
        
        # 重新整理按鈕
        self.refresh_button = ttk.Button(
            self.window,
            text="重新整理",
            command=self.refresh_tasks
        )
        self.refresh_button.pack(pady=5)
        
    def load_tasks(self):
        """載入任務資料"""
        try:
            with open('tasks.json', 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
                self.update_task_list()
        except FileNotFoundError:
            self.tasks = []
            
    def update_task_list(self):
        """更新任務清單顯示"""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "□"
            time = datetime.datetime.fromisoformat(task["time"]).strftime("%Y-%m-%d %H:%M")
            self.task_listbox.insert(tk.END, f"{status} {time} - {task['transcript'][:30]}...")
            
    def show_task_details(self, event):
        """顯示任務詳情"""
        selection = self.task_listbox.curselection()
        if not selection:
            return
            
        task = self.tasks[selection[0]]
        detail_window = tk.Toplevel(self.window)
        detail_window.title("任務詳情")
        
        # 逐字稿
        ttk.Label(detail_window, text="原始逐字稿：").pack(pady=5)
        ttk.Label(detail_window, text=task["transcript"]).pack()
        
        # 提醒語句
        ttk.Label(detail_window, text="提醒語句：").pack(pady=5)
        ttk.Label(detail_window, text=task["reminder"]).pack()
        
        # 時間
        time = datetime.datetime.fromisoformat(task["time"]).strftime("%Y-%m-%d %H:%M")
        ttk.Label(detail_window, text="提醒時間：").pack(pady=5)
        ttk.Label(detail_window, text=time).pack()
        
        # 完成狀態
        status = "已完成" if task["completed"] else "未完成"
        ttk.Label(detail_window, text="完成狀態：").pack(pady=5)
        ttk.Label(detail_window, text=status).pack()
        
    def refresh_tasks(self):
        """重新載入任務資料"""
        self.load_tasks()
        
    def run(self):
        """運行應用程式"""
        self.window.mainloop()

if __name__ == "__main__":
    app = CaregiverApp()
    app.run()
