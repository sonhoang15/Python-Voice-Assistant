# commands.py
import os
import subprocess
import webbrowser
import datetime
import pyautogui

from music_player import (
    play_track, play_by_name, play_random,
    stop_music, pause_music, resume_music,
    next_track, previous_track,
    volume_up, volume_down, set_volume
)


def execute_command(command):

    if "mở meta tft" in command:
        exe_path = r"C:\Program Files (x86)\Overwolf\OverwolfLauncher.exe"
        args = [
            exe_path,
            "-launchapp",
            "aheglebeeekjdnkljmpngplhpedgejncjhojnndh",
            "-from-desktop"
        ]

        if os.path.exists(exe_path):
            subprocess.Popen(args)
            return "Đang mở Meta TFT."
        else:
            return "Không tìm thấy Overwolf Launcher."

    if "mở game" in command:
        app_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
        
        if os.path.exists(app_path):
            subprocess.Popen(app_path)
            return "Đang mở game."
        else:
            return "Tôi không tìm thấy game trên máy bạn."


    if "mở youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Mở YouTube cho bạn đây."

    if "tìm kiếm" in command:
        query = command.replace("tìm kiếm", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Tôi đang tìm kiếm {query} trên Google."

    if "phát nhạc" in command or "mở nhạc" in command:
        return play_track(0)

    if "dừng nhạc" in command or "tắt nhạc" in command:
        return stop_music()

    if "tạm dừng" in command or "dừng lại" in command:
        return pause_music()

    if "tiếp tục" in command or "phát tiếp" in command:
        return resume_music()

    if "bài tiếp" in command or "chuyển bài" in command:
        return next_track()

    if "bài trước" in command or "quay lại bài" in command:
        return previous_track()

    if "phát ngẫu nhiên" in command or "ngẫu nhiên" in command:
        return play_random()

    if "phát bài" in command or "mở bài" in command:
        return play_by_name(command.replace("phát bài", "").strip())

    if "tăng âm lượng" in command:
        return volume_up()

    if "giảm âm lượng" in command:
        return volume_down()

    if "âm lượng" in command:
        try:
            percent = int(''.join(filter(str.isdigit, command)))
            return set_volume(percent)
        except:
            return "Bạn muốn đặt âm lượng bao nhiêu phần trăm?"

    if "gõ" in command:
        text = command.replace("gõ", "").strip()
        pyautogui.write(text)
        return f"Tôi đã gõ: {text}"

    if "mấy giờ" in command:
        now = datetime.datetime.now().strftime("%H:%M ngày %d tháng %m năm %Y")
        return f"Bây giờ là {now}"

    if "tạm biệt" in command or "thoát" in command or "kết thúc" in command:
        return "EXIT_AI"

    return "Tôi không hiểu lệnh này."
