# sfls
**S**potify **F**ullscreen **L**yrics **S**witcher

## In a nutshell

**sfls** (**S**potify **F**ullscreen **L**yrics **S**witcher) automatically shows lyrics while they're being sung, and hides them during the instrumental parts when using the fullscreen Spotify player.

## Requirements

- **Python 3** (tested on 3.10.6 and 3.12.1)
- **Spotify Desktop app**
- **Spotify Premium** (free version doesn't have the fullscreen player)
- **Windows machine**
- **1440p monitor** (will support other resolutions in the future)

## Installation

1. Clone the repository / Download .zip
2. Create a virtual environment: `python3 -m venv env` and activate it
3. Install dependencies: `pip install -r requirements.txt`

## Usage

- Run `main.py` and follow the instructions.
  
You **will need** to have a timings file inside `timings/` for each song you want sfls to work for.

In case you don't have a timings file, you can make it yourself by running the `timingsCreator.py` and following the simple instructions.

## Quick note

- sfls will keep doing its job until it reaches the first song for which it does not have the timings file
- to stop sfls, alt+tab to the console and close it or wait for it to reach a song it doesn't have the timings file for
