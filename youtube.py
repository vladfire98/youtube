#!/usr/bin/env python3

from pytube import YouTube
import os
import argparse
from moviepy.editor import *


def get_audio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    print("Downloading...")
    out_file = video.download(output_path='/home/bednyakov/Музыка/')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    filetoconvert = AudioFileClip(out_file)
    filetoconvert.write_audiofile(new_file)
    print('NEW-FILE: ' + new_file)
    #os.rename(out_file, new_file)  
    print(yt.title + " has been successfully downloaded (audio).")


def get_video(link):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download(output_path='/home/bednyakov/Музыка/')
    print(yt.title + " has been successfully downloaded (video).")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required = False, action='store_true', help = "Youtube video URL")
    ap.add_argument("-a", "--audio", required = False, action='store_true', help = "Audio only")
    ap.add_argument("URL", help = "URL to Youtube content")
    args = vars(ap.parse_args())

    if args["video"]:
        get_video(args["URL"])
    else:
        get_audio(args["URL"])
