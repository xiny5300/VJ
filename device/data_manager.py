# 資料存儲模組
# 處理任務的儲存和讀取

import json
import os
from datetime import datetime

class DataManager:
    def __init__(self, storage_path="tasks.json"):
        """初始化資料管理器
        Args:
            storage_path (str): JSON 檔案儲存路徑
        """
        self.storage_path = storage_path
        self.tasks = []
        self.load_tasks()
        
    def load_tasks(self):
        """載入所有任務"""
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
            self.save_tasks()
            
    def save_tasks(self):
        """儲存所有任務"""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            
    def add_task(self, task_data):
        """新增任務
        Args:
            task_data (dict): 任務資料
        """
        self.tasks.append(task_data)
        self.save_tasks()
        
    def update_task(self, task_id, updates):
        """更新任務
        Args:
            task_id (int): 任務索引
            updates (dict): 要更新的欄位
        """
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].update(updates)
            self.save_tasks()
            
    def get_task(self, task_id):
        """取得特定任務
        Args:
            task_id (int): 任務索引
        Returns:
            dict: 任務資料
        """
        if 0 <= task_id < len(self.tasks):
            return self.tasks[task_id]
        return None
        
    def get_pending_tasks(self):
        """取得未完成的任務
        Returns:
            list: 未完成的任務清單
        """
        now = datetime.now()
        return [
            task for task in self.tasks
            if not task["completed"] and
            datetime.fromisoformat(task["time"]) > now
        ]
        
    def get_completed_tasks(self):
        """取得已完成的任務
        Returns:
            list: 已完成的任務清單
        """
        return [task for task in self.tasks if task["completed"]]
        
    def clear_old_tasks(self, days=30):
        """清理舊任務
        Args:
            days (int): 要保留的天數
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        self.tasks = [
            task for task in self.tasks
            if datetime.fromisoformat(task["time"]) > cutoff_date or
            not task["completed"]
        ]
        self.save_tasks()
