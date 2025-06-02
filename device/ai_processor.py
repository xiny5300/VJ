# AI 處理模組
# 包含時間辨識和提醒語句生成功能

import re
from datetime import datetime, timedelta
from google.cloud import aiplatform
import json

class AIProcessor:
    def __init__(self, api_key=None):
        """初始化 AI 處理器
        Args:
            api_key (str): Gemini API 金鑰
        """
        # TODO: 設定 Gemini API 認證
        pass
        
    def extract_time(self, text):
        """從文字中提取時間資訊
        Args:
            text (str): 輸入文字
        Returns:
            datetime: 辨識出的時間
        """
        # 基本時間模式
        patterns = [
            r'明天早上(\d+)點',
            r'明天下午(\d+)點',
            r'今天早上(\d+)點',
            r'今天下午(\d+)點',
            r'後天早上(\d+)點',
            r'後天下午(\d+)點'
        ]
        
        now = datetime.now()
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                hour = int(match.group(1))
                if '下午' in pattern and hour < 12:
                    hour += 12
                    
                if '明天' in pattern:
                    target_date = now + timedelta(days=1)
                elif '後天' in pattern:
                    target_date = now + timedelta(days=2)
                else:
                    target_date = now
                    
                return datetime(
                    target_date.year,
                    target_date.month,
                    target_date.day,
                    hour,
                    0
                )
                
        # 如果無法辨識，返回 None
        return None
        
    def generate_reminder(self, transcript, time):
        """生成提醒語句
        Args:
            transcript (str): 原始逐字稿
            time (datetime): 辨識出的時間
        Returns:
            str: 生成的提醒語句
        """
        # TODO: 調用 Gemini API 生成提醒語句
        # 目前使用簡單的模板
        time_str = time.strftime("%Y年%m月%d日 %H:%M")
        return f"現在是{time_str}，提醒您：{transcript}"
        
    def format_task_data(self, transcript, reminder, time):
        """格式化任務資料
        Args:
            transcript (str): 原始逐字稿
            reminder (str): 提醒語句
            time (datetime): 提醒時間
        Returns:
            dict: 格式化的任務資料
        """
        return {
            "transcript": transcript,
            "reminder": reminder,
            "time": time.isoformat(),
            "completed": False
        }
