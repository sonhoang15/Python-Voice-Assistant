# main.py
import time
import speech_recognition as sr
from speech import speak, robot_ear
from commands import execute_command

assistant_awake = False
AWAKE_TIMEOUT = 15
last_command_time = 0
last_state = ""


def print_state(text):
    global last_state
    if text != last_state:
        print(text)
        last_state = text


with sr.Microphone() as mic:

    robot_ear.adjust_for_ambient_noise(mic, duration=1)
    print(" Đã hiệu chỉnh tiếng ồn nền")

    while True:

        if not assistant_awake:
            print_state(" Đang chờ hotword 'xin chào'...")

            try:
                audio = robot_ear.listen(mic, timeout=5, phrase_time_limit=7)
                you = robot_ear.recognize_google(audio, language="vi-VN").lower()
            except:
                continue

            if "xin chào" in you or "chào" in you:
                assistant_awake = True
                last_command_time = time.time()
                speak("Xin chào Hoàng Sơn! Tôi có thể giúp gì?")
            continue

        print_state(" Trợ lý đang hoạt động...")

        if time.time() - last_command_time > AWAKE_TIMEOUT:
            assistant_awake = False
            speak("Không có lệnh mới, tôi sẽ nghỉ.")
            continue

        try:
            audio = robot_ear.listen(mic, timeout=5, phrase_time_limit=7)
            command = robot_ear.recognize_google(audio, language="vi-VN").lower()
            print(" Lệnh nhận được:", command)
        except:
            continue

        last_command_time = time.time()
        reply = execute_command(command)

        if reply == "EXIT_AI":
            speak("Tạm biệt! hẹn gặp lại sau.")
            break

        speak(reply)

        time.sleep(0.7)