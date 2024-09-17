import os
import shutil

mpd_url=input("Enter MPD URL : ")
cookie_value = input("Enter Cookie Value : ")



def divider():
	count = int(shutil.get_terminal_size().columns)
	count = count - 1
	print ('-' * count)

print ('yt-dlp --external-downloader aria2c --no-warnings --allow-unplayable-formats --no-check-certificate -F --add-header "referer: https://www.hotstar.com/" --add-header "origin: https://www.hotstar.com" --add-header "cookie: %s" '%cookie_value + '"%s"'%mpd_url)


print("[info] Processing Video Info..")
os.system('yt-dlp --external-downloader aria2c --no-warnings --allow-unplayable-formats --no-check-certificate -F --add-header "referer: https://www.hotstar.com/" --add-header "origin: https://www.hotstar.com" --add-header "cookie: %s" '%cookie_value + '"%s"'%mpd_url)
divider()

VIDEO_ID = input("ENTER VIDEO_ID (Press Enter for Best): ")
if VIDEO_ID == "":
	VIDEO_ID = "bv"
	
AUDIO_ID = input("ENTER AUDIO_ID (Press Enter for Best): ")
if AUDIO_ID == "":
	AUDIO_ID = "ba"

divider()
print("Downloading Encrypted Video from CDN..")
os.system(f'yt-dlp -o "encrypted_video.mp4" --no-warnings --external-downloader aria2c --allow-unplayable-formats --no-check-certificate -f {VIDEO_ID} --add-header "referer: https://www.hotstar.com/" --add-header "origin: https://www.hotstar.com" --add-header "cookie: %s" '%cookie_value + '"%s"'%mpd_url+' -o "encrypted_video.mp4"')
print("Downloading Encrypted Audio from CDN..")
os.system(f'yt-dlp -o "encrypted_audio.m4a" --no-warnings --external-downloader aria2c --allow-unplayable-formats --no-check-certificate -f {AUDIO_ID} --add-header "referer: https://www.hotstar.com/" --add-header "origin: https://www.hotstar.com" --add-header "cookie: %s" '%cookie_value + '"%s"'%mpd_url+' -o "encrypted_audio.m4a"')
# print("Downloading English Subtitles ..")
# os.system('yt-dlp --write-subs --skip-download --external-downloader aria2c --verbose --allow-u  --add-header "referer: https://www.hotstar.com/" --add-header "origin: https://www.hotstar.com" --add-header "cookie: %s" '%cookie_value + '"%s"'%mpd_url+' --output Subtitle')


exec(open('decrypt.py').read())




