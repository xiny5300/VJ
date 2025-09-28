# Future Memory Cassette

Future Memory Cassette 是一個智能提醒系統，整合了語音互動、AI 智能提醒與手機端資料介面。本系統旨在提升使用者的生活自主性，同時減輕照護者或家人的負擔。

## 功能特點

- 語音錄音與自動轉文字
- 智能時間辨識
- AI 生成溫柔提醒語句
- 語音播放提醒
- 手機監控介面
- 任務完成追蹤

## 系統需求

- Python 3.8+
- Windows 10/11
- 麥克風
- 揚聲器

## 安裝說明

1. 克隆專案：
```bash
git clone https://github.com/xiny5300/VJ.git
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

3. 設定環境變數：
- 將 Gemini API 金鑰加入環境變數
- 設定 Python 路徑

## 使用說明

### 裝置端（患者使用）

1. 執行裝置端程式：
```bash
cd device
python main.py
```

2. 點擊「開始錄音」按鈕
3. 說出要提醒的事項
4. 系統會自動辨識並設定提醒

### 照護者 APP

1. 執行照護者介面：
```bash
cd caregiver_app
python main.py
```

2. 查看任務清單
3. 雙擊任務可查看詳細資訊

## 專案結構

```
future_cassette/
├── device/
│   ├── main.py              # 裝置端主程式
│   ├── audio_processor.py   # 語音處理模組
│   ├── ai_processor.py      # AI 處理模組
│   ├── data_manager.py      # 資料管理模組
│   └── config.py            # 設定檔
├── caregiver_app/
│   └── main.py              # 照護者介面主程式
├── requirements.txt         # 相依套件清單
└── README.md               # 說明文件
```

## 開發團隊

- 開發者：[Your Name]
- 專案維護：[Organization]

## 授權協議

本專案採用 MIT 授權協議。詳見 [LICENSE](LICENSE) 檔案。
