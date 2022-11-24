import os
import time
import ctypes
from dotenv import load_dotenv
from pypresence import Presence
from textfilters import useless_words

load_dotenv()
client_id = os.getenv('DISCORD_YT_APP_TOKEN')

window_titles = []

RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop


def full():
    print("beginning")
    song_name = None
    enum_windows = ctypes.windll.user32.EnumWindows
    enum_windows_proc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    get_window_text = ctypes.windll.user32.GetWindowTextW
    get_window_text_length = ctypes.windll.user32.GetWindowTextLengthW
    is_window_visible = ctypes.windll.user32.IsWindowVisible

    def foreach_window(hwnd, lParams):
        if is_window_visible(hwnd):
            length = get_window_text_length(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            get_window_text(hwnd, buff, length + 1)
            window_titles.append(buff.value)
        return True

    enum_windows(enum_windows_proc(foreach_window), 0)
    title_filter = 'YouTube Music'
    for window_title in window_titles:
        if title_filter in window_title:
            print(window_title)
            song_name = window_title
            for useless_word in useless_words:
                song_name = song_name.replace("(" + useless_word + ")", "")
                song_name = song_name.replace("[" + useless_word + "]", "")
                song_name = song_name.replace(useless_word, "")
                song_name = song_name.replace("  ", " ")
                song_name = song_name.replace("  ", " ")
                song_name = song_name.replace("( )", "")

    if song_name is not None and song_name != '':
        song_name = (song_name[:120] + '..') if len(song_name) > 120 else song_name
        print(RPC.update(state=song_name, details="Listening to",
                         large_image="none", large_text="none",
                         small_image="none", small_text="none"))
    time.sleep(15)
    full()


try:
    full()
except KeyboardInterrupt:
    print('Closing program')
except UnboundLocalError:
    print('No Youtube Tab Found!')
    print('Please bring tab to foreground or keep it open in a separate browser!')
finally:
    RPC.close()
    print("The end")
