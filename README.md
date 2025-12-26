# 🎙️ Vietnamese Voice Assistant (Python)

## 📌 Mô tả
Một trợ lý giọng nói tiếng Việt chạy local, cho phép điều khiển máy tính bằng giọng nói:
- Mở ứng dụng
- Điều khiển trình duyệt
- Phát nhạc
- Gõ văn bản
- Trả lời thời gian

Project tập trung vào **Python application + rule-based NLP**

---

## 🛠️ Công nghệ sử dụng
- Python 3
- SpeechRecognition
- gTTS
- PyGame
- PyAutoGUI
- VLC

---

## ⚙️ Chức năng chính
- Wake word (xin chào)
- Nhận dạng giọng nói tiếng Việt
- Xử lý lệnh bằng rule-based intent
- Phản hồi bằng giọng nói
- Điều khiển hệ thống

---

## 🧠 Kiến trúc
- `speech.py`: xử lý nghe & nói
- `commands.py`: logic xử lý lệnh
- `music_player.py`: quản lý nhạc
- `main.py`: vòng lặp chính

---

## ▶️ Cách chạy
```bash
pip install speechrecognition gtts pygame pyautogui python-vlc
python main.py
