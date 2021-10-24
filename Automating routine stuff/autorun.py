import webbrowser
import subprocess
import pyautogui
import time
# opening tabs
urls = [
    "https://teams.microsoft.com/",
    "https://montana.managebac.com/student",
    "https://outlook.office365.com/mail/inbox",
    "https://web.whatsapp.com"
]
for url in urls:
    webbrowser.open_new(url)

# active the url
time.sleep(1)
pyautogui.click(250, 6)  # coodinates of the url you need

# opening programs
programs = [
    r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    r"C:\Users\Пользователь\AppData\Roaming\Spotify\Spotify.exe"
]
for program in programs:
    subprocess.Popen(f'"{program}"')

# to phase out all the programs and show the desktop
time.sleep(5)
pyautogui.hotkey("win", "d")
