# 語音處理模組
# 包含錄音、語音識別和語音合成功能

import sound_device as sd
import numpy as np
import wave
import whisper
import pyttsx3
from gtts import gTTS
import os
import tempfile

class AudioProcessor:
    def __init__(self):
        self.sample_rate = 16000
        self.channels = 1
        self.whisper_model = whisper.load_model("base")
        self.tts_engine = pyttsx3.init()
        
    def start_recording(self, duration=None):
        """開始錄音
        Args:
            duration (float): 錄音時長（秒），None 表示持續錄音直到呼叫 stop_recording
        """
        self.recording = []
        def callback(indata, frames, time, status):
            if status:
                print(status)
            self.recording.append(indata.copy())
            
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            callback=callback
        )
        self.stream.start()
        
    def stop_recording(self):
        """停止錄音並儲存為 WAV 檔案"""
        self.stream.stop()
        self.stream.close()
        
        # 合併錄音數據
        recording = np.concatenate(self.recording, axis=0)
        
        # 儲存為臨時 WAV 檔案
        temp_wav = tempfile.mktemp(suffix=".wav")
        with wave.open(temp_wav, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(recording.tobytes())
            
        return temp_wav
        
    def transcribe_audio(self, audio_file):
        """使用 Whisper 進行語音識別
        Args:
            audio_file (str): WAV 檔案路徑
        Returns:
            str: 識別出的文字
        """
        result = self.whisper_model.transcribe(audio_file)
        return result["text"]
        
    def text_to_speech(self, text, use_gtts=False):
        """文字轉語音
        Args:
            text (str): 要轉換的文字
            use_gtts (bool): 是否使用 Google TTS，預設使用 pyttsx3
        """
        if use_gtts:
            tts = gTTS(text=text, lang='zh-tw')
            temp_mp3 = tempfile.mktemp(suffix=".mp3")
            tts.save(temp_mp3)
            os.system(f'start {temp_mp3}')  # Windows 系統上播放
        else:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
