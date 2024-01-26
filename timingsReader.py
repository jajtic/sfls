#store timings from .txt into a list

from SwSpotify import spotify

def nowPlaying(v):
    title, artist = spotify.current()
    currentSongRaw = artist + " - " + title
    currentSong = artist.replace(" ", "_") + "_" + title.replace(" ", "_")
    replacements = [("/", "_"), ("\\", "_"), (":", "_"), ("*", "_"), ("?", "_"), ('"', "_"), ("<", "_"), (">", "_"), ("|", "_")]
    for old, new in replacements:
        currentSong = currentSong.replace(old, new)
    if v == "raw":
        return currentSongRaw
    else:
        return currentSong

def getTimingsPath():
    playing = nowPlaying("0")
    playing = playing + ".txt"
    return "timings/" + playing

def read_timings(file_path):
    try:
        timingsList = []
        with open(file_path, 'r') as file:
            for line in file:
                timing = float(line.strip())
                timingsList.append(timing)
        return timingsList
    except FileNotFoundError:
        print("Song timings file not found")
        exit()

#get values for use in main.py executeTimings()
def delayTimings(timingsList):
    subtracted_timings = []
    subtracted_timings.append(timingsList[0])
    track_length = int(timingsList[-1])
    timingsList.pop()
    for i in range(1, len(timingsList)):
        subtracted_timings.append(timingsList[i] - timingsList[i-1])
    return subtracted_timings, track_length