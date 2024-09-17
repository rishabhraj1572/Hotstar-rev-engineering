import os
import shutil
def divider():
	count = int(shutil.get_terminal_size().columns)
	count = count - 1
	print ('-' * count)

def run():
        keys=input("Enter Decryption Keys : ")
        os.system('mp4decrypt --key '+keys+' encrypted_video.mp4 Video.mp4')
        os.system('mp4decrypt --key '+keys+' encrypted_audio.m4a Audio.m4a')
        divider()
        print("[info] Decryption Complete!")
        n=input("Enter Content Name/Name with Episode Number")
        nnn=n.replace("-", ".")
        nn=nnn.replace(":", "")
        nam= nn.replace(" ", ".")
        name=nam+"-RR"
        print("Merging Files and Processing.. (Takes a while)")
        os.system('ffmpeg -i Video.mp4 -i Audio.m4a -c copy '+name+'.mkv')




def next_phase():
        exec(open('remove.py').read())

run()
# next_phase()
