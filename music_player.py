# music_player.py
import os
import time
import random
import vlc
import pygame
import threading

music_folder = r"C:\Users\ACER NITRO5\OneDrive\Máy tính\drive-download-20251002T050906Z-1-001"

playlist = []
current_track = 0
player = None
is_random_mode = False

current_volume = 80 


SUPPORTED_FORMATS = (".wav", ".mp3", ".flac", ".ogg", ".m4a")

def load_playlist():
    global playlist
    if os.path.exists(music_folder):
        playlist = [
            os.path.join(music_folder, f)
            for f in os.listdir(music_folder)
            if f.lower().endswith(SUPPORTED_FORMATS)
        ]
        playlist.sort()
    else:
        playlist = []


def play_track(index):
    global current_track, player, current_volume
    load_playlist()

    if not playlist:
        return "Không có bài nhạc nào trong thư mục."

    if index < 0 or index >= len(playlist):
        return "Không tìm thấy bài nhạc."

    current_track = index
    track = playlist[index]

    try:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
    except:
        pass

    if player is not None:
        player.stop()

    player = vlc.MediaPlayer(track)
    player.play()

    time.sleep(0.2)

    player.audio_set_volume(current_volume)

    return f"Đang phát: {os.path.basename(track)}"


def play_by_name(name):
    global current_track, is_random_mode
    is_random_mode = False
    for i, song in enumerate(playlist):
        if name.lower() in song.lower():
            current_track = i
            return play_track(i)
    return f"Không tìm thấy bài hát chứa: {name}"

def play_random():
    global current_track, is_random_mode
    is_random_mode = True
    current_track = random.randint(0, len(playlist) - 1)
    return play_track(current_track)


def stop_music():
    global player
    if player:
        player.stop()
        return "Đã dừng nhạc."
    return "Không có nhạc nào đang phát."


def pause_music():
    global player
    if player:
        player.pause()
        return "Đã tạm dừng nhạc."
    return "Không có nhạc đang phát."


def resume_music():
    global player
    if player:
        player.play()
        return "Tiếp tục phát nhạc."
    return "Không có nhạc để tiếp tục."


def next_track():
    global current_track
    return play_track(current_track + 1)


def previous_track():
    global current_track
    return play_track(current_track - 1)


def volume_up():
    global player, current_volume
    if player:
        current_volume = min(100, current_volume + 10)
        player.audio_set_volume(current_volume)
        return f"Tăng âm lượng lên {current_volume}%."
    return "Không có nhạc nào đang phát."


def volume_down():
    global player, current_volume
    if player:
        current_volume = max(0, current_volume - 10)
        player.audio_set_volume(current_volume)
        return f"Giảm âm lượng xuống {current_volume}%."
    return "Không có nhạc nào đang phát."


def set_volume(percent):
    global player, current_volume
    if player:
        current_volume = max(0, min(100, percent))
        player.audio_set_volume(current_volume)
        return f"Đã đặt âm lượng thành {current_volume}%."
    return "Không có nhạc nào đang phát."

def auto_next_loop():
    global player, current_track

    while True:
        if player is not None:
            state = player.get_state()

            if state == vlc.State.Ended:
                current_track += 1
                if current_track >= len(playlist):
                    current_track = 0
                play_track(current_track)

        time.sleep(0.3)

threading.Thread(target=auto_next_loop, daemon=True).start()