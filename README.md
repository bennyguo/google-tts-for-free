# Google TTS for FREE

Google cloud services, including [Google TTS API](https://cloud.google.com/text-to-speech) requires user to sign up with a credit card. For those who don't have one, this script provide a semi-automatic way to get TTS audio file of mp3 format using the HAR file exported by Chrome Devtools.

## Requirements

- Python 2 / 3
- Chrome (any other browser that can export HAR file also works)

## Usage

1. Open [Google TTS API](https://cloud.google.com/text-to-speech) page in Chrome. Open Devtools from Chrome's main menu (Settings > More Tools > Developer Tools). You can also Press F12 (Windows) or Cmd+Option+i (Mac).
2. Use the demo in the page as many times as you want. 
3. Click on the download button on the upper right corner of the Devtools panel, and this will export the HAR file we'll use later. Choose a location to save it.
4. Download the `extract.py` script. You can achive it by `git clone` this repository.
5. Execute `python extract.py <path/to/your_har_file> -o <output directory>` to extract all the audios you generated on the demo page in mp3 format.

## Command Line Arguments

- har: Path of the har file, required.
- -o OUTPUT, --output OUTPUT: Audio output directory, default to `output/`.
