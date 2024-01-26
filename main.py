import pyautogui as pg
import timingsReader as tr
import time

def pressAltTab():
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')

def pressControlLeft():
    pg.keyDown('ctrl')
    pg.press('left')
    pg.keyUp('ctrl')

##* use later to support more screen resolutions
def getSystemResolution():
    resolution = pg.size()
    resolution = str(resolution[0]) + "x" + str(resolution[1])
    return resolution

## values for use with 1440p
def allowEnterForLyrics():
    pg.click(2233, 1289)
    time.sleep(0.1)
    pg.click(2233, 1289)
def executeTimings():
    timings, track_length = tr.delayTimings(tr.read_timings(tr.getTimingsPath()))
    timingsNoDelay = tr.read_timings(tr.getTimingsPath())
    print(tr.getTimingsPath())
    print(tr.nowPlaying("0"))
    print(track_length)
    for timing in timings:
        print("Delaying", timing, "seconds")
        time.sleep(timing)
        print("Pressing enter")
        pg.press('enter')
    print(f"waiting for song to end ({track_length - timingsNoDelay[-2]}s)")
    time.sleep(track_length - timingsNoDelay[-2])
    print(f"--- {tr.nowPlaying('raw')} -> song ended ---")


print("System resolution:", getSystemResolution())
input("Launch Spotify in fullscreen mode with lyrics OFF and press enter to continue. This will restart the playback of the current song.")
print(tr.nowPlaying("0"))
print("Timings path:", tr.getTimingsPath())

print("Pressing Alt+Tab")
pressAltTab()
time.sleep(0.5)

print("Pressing lyrics button")
allowEnterForLyrics()

print("Moving cursor off screen")
pg.moveTo(2560, 700)

print("Restarting playback")
pressControlLeft()

while True:
    print("Begin executing timings")
    executeTimings()
    allowEnterForLyrics()
    pg.moveTo(2560, 700)