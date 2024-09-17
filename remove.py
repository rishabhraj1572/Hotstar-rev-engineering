import os
print("Deleting Temperory Files..")
os.remove("encrypted_video.mp4")
os.remove("encrypted_audio.m4a")
os.remove("Video.mp4")
os.remove("Audio.m4a")
# os.remove("Subtitle.en.vtt")
print("[info] Process Finished. Final Video File is saved in directory.")
