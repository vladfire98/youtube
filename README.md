# youtube
pip3 install argparse

pip3 install pytube

pip3 install moviepy

chmod +x youtube.py

cp ./youtube.py /usr/bin/youtube

youtube --help

```
usage: youtube [-h] [-v] [-a] URL

positional arguments:
  URL          URL to Youtube content

options:
  -h, --help   show this help message and exit
  -v, --video  Youtube video URL
  -a, --audio  Audio only
```

## Using example
Get audio:

```
youtube <URL>
```


Get video:

```
youtube -v <URL>
```

## Change the regex in cipher.py
In function get_throttling_function_name change regex in variables function_patterns

```
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
```

## Convert MP4 to MP3 from Linux

CBR:

```
ffmpeg -i video.mp4 -vn \
       -acodec libmp3lame -ac 2 -ab 160k -ar 48000 \
        audio.mp3
```

VBR:

```
ffmpeg -i video.mp4 -vn \
       -acodec libmp3lame -ac 2 -qscale:a 4 -ar 48000 \
        audio.mp3
```
