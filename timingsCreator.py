## script to help create timing files
import timingsReader as tr
import os, time

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def timeCalculator(time):
        time = time.split(":")
        time = int(time[0]) * 60 + int(time[1])
        return time

def timingsEditor(timingsFilePath):
    print("Whenever you need to input a time, use the format mm:ss or m:ss\n")
    track_length = timeCalculator(input("Enter the length of the song (mm:ss) > "))
    clearScreen()
    timing1 = "0"
    while True:
        if timing1 == "":
            with open(timingsFilePath, 'a') as timingsFile:
                timingsFile.write(str(track_length))
                timingsFile.close()
                print("Data written to file")
                time.sleep(0.5)
                clearScreen()
                break
        else:
            while True:
                timing1 = input("Enter the time when the lyrics section begins, or leave empty if there are no more lyrics (mm:ss) > ")
                if timing1 == "":
                    break
                timing1 = timeCalculator(timing1)
                timing2 = timeCalculator(input("Enter the time when the lyrics section ends (mm:ss) > "))
                with open(timingsFilePath, 'a') as timingsFile:
                    timingsFile.write(str(timing1) + "\n")
                    timingsFile.write(str(timing2) + "\n")
                    timingsFile.close()
                    print("Data written to file")
                    time.sleep(0.5)
                    clearScreen()
                    break
    input("Timings file has been saved. Press enter to exit.")
    quit()


def createTimings(timingsFilePath):
    timingsFilePath = str(timingsFilePath)
    print(f"Creating timings file {timingsFilePath}")
    with open(timingsFilePath, 'w') as timingsFile:
        timingsFile.close()
    clearScreen()
    timingsEditor(timingsFilePath)

def begin():
    input("Play the song you want to make timings for and press enter to begin.")
    clearScreen()
    timingsPath = tr.getTimingsPath()
    print("The following song was detected:\n")
    print(tr.nowPlaying('raw'))
    choice = input("\nDo you want to create timings for this song? (Y/n) > ")
    if choice.lower() == "y" or choice.lower() == "":        
        createTimings(timingsPath)
    else:
        print("Cancelled.")
        exit()

begin()