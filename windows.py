import ctypes
from pypresence import Presence
import time, os, sys

client_id = ''  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

def full():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []
    def foreach_window(hwnd, lParams):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    sub = 'YouTube'
    for text in titles:
        if sub in text:
            textp = text.replace("(", "")
            textp2 = textp.replace(")", "")
            textp3 = textp2.replace("YouTube", "")
            textp4 = textp3.replace("Waterfox", "")
            textp5 = textp4.replace("Audio", "")
            textp6 = textp5.replace("Official Music Video", "")
            textp7 = textp6.replace("Official Audio", "")
            textp8 = textp7.replace("WSHH Exclusive", "")
            textp9 = textp8.replace("- ", "")
            textp10 = textp9.replace("-", "")
            textp11 = textp10.replace("Official", "")
            textp12 = textp11.replace("  ", "")
            textp13 = textp12.replace("   ", "")
            textp14 = textp13.replace("    ", "")
            textp15 = textp14.replace("Google Chrome", "")
            textp16 = textp15.replace("Firefox", "")
            textp17 = textp16.replace("Internet Explorer", "")

    print(RPC.update(state=textp17 + " on Youtube", details="Listening to: "))  # Set the presence
    time.sleep(15) # Can only update rich presence every 15 seconds
    full()

try:
    full()
except KeyboardInterrupt:
    print('Closing program')
finally:
    RPC.close()
