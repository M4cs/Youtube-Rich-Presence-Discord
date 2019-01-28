# Youtube Rich Presence for Discord
Description: Grab Title Of Youtube Video on Windows to Display On Discord as Rich Presence.

Author: Me

Main Contributors: LewdNeko, SplendidX

Version: 1.1

Changelog:

V1.1: Fixed Buggies and added cleaner code from Neko and Splendid  

![alt text](https://image.prntscr.com/image/pG214_S_R_iYfSjunn5YTg.png)  										

![alt text](https://image.prntscr.com/image/kkmfZPEASiSJXA-ypF7EyQ.png)

[![GitHub stars](https://img.shields.io/github/stars/M4cs/Youtube-Rich-Presence-Discord.svg?longCache=true&style=for-the-badge)](https://github.com/M4cs/Youtube-Rich-Presence-Discord/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/M4cs/Youtube-Rich-Presence-Discord.svg?longCache=true&style=for-the-badge)](https://github.com/M4cs/Youtube-Rich-Presence-Discord/network)
[![GitHub issues](https://img.shields.io/github/issues/M4cs/Youtube-Rich-Presence-Discord.svg?longCache=true&style=for-the-badge)](https://github.com/M4cs/Youtube-Rich-Presence-Discord/issues)
[![GitHub license](https://img.shields.io/github/license/M4cs/Youtube-Rich-Presence-Discord.svg?longCache=true&style=for-the-badge)](https://github.com/M4cs/Youtube-Rich-Presence-Discord)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/M4cs/Youtube-Rich-Presence-Discord.svg?longCache=true&style=for-the-badge)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FM4cs%2FYoutube-Rich-Presence-Discord)

# Pre-Reqs

- Windows
- Python 3.6 (Until Pypresence fixes 3.7 Compatability)
- Discord Account
- Discord App Client ID (Grab from [here](https://discordapp.com/developers/applications/me))

This Program Uses Pypresence! Check them out here:

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

In order to get pre-reqs simply clone this repo and run:
```
pip install -r requirements.txt
```

# Running The Program

## Setting Client ID:

On line 6 you must set your Client ID. You can refer to the link above in Pre-Reqs to see where to find your Client ID. You need to add an application and then pull the Client ID.

I reccommend using pythonw for this so you can run it in the background and not worry about a command prompt staying open. 

**You have to keep a single tab open on a browser for YouTube when listening to music or be tabbed into your Youtube Video for it to register!**

I usually just keep one browser open to just youtube and then open another browser to browse the web. I know this is annoying but it's how it works until I find a workaround due to how the win32api finds titles. I may work on a browser extension..

Run:
```
pythonw.exe windows.py
```
and then you can close the command prompt and it will run in the background!
