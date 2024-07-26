#!/usr/bin/env python3

from pytube import YouTube
import os
from sys import argv
import argparse
import telebot
import shutil
from datetime import datetime, date, time
#import time
from moviepy.editor import *

token = "TOKEN"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.first_name)


def get_audio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    # download the file
    print("Downloading...")
    out_file = video.download(output_path='/tmp/youtube_music')
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    #os.rename(out_file, new_file)
    filetoconvert = AudioFileClip(out_file)
    filetoconvert.write_audiofile(new_file)
    # result of success
    print(yt.title + " has been successfully downloaded (audio).")
    return new_file


def log(message):
    print("<!------!>")
    print(datetime.now())
    print("Сообщение от {0} {1} {2} (id = {3}) \n {4}".format(message.from_user.first_name,
                                                      message.from_user.last_name,
                                                      message.from_user.username,
                                                      str(message.from_user.id), message.text))

@bot.message_handler(content_types=["text"])
def main(message):
    try:
        bot.send_document(message.chat.id, document=open(get_audio(message.text), 'rb'))
        try:
            shutil.rmtree('/tmp/youtube_music')
        except OSError as e:
            print("Error: %s : %s" % ('/tmp/youtube_music', e.strerror))
    except BaseException:
        bot.reply_to(message, 'Повтори попытку...')
    log(message)


if __name__ == "__main__":
    bot.polling(none_stop= True)
