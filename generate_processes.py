import os
import time
import subprocess
from text_to_mp3 import text_to_speech_file

def text_to_audio(folder):
    print(folder)
    with open(f"user_uploads/{folder}/desc.txt","r") as f:
        file=f.read()
    text_to_speech_file(file,folder)
       

def create_reel(folder):
    command='''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4 '''
    subprocess.run(command.format(folder=folder), shell=True , check=True)



if __name__ == "__main__":
     # while True:
    
       print("Processing......")
       
       with open("finished_process.txt","r") as f:
          finished_processes=f.readlines()

       folders=os.listdir("user_uploads")
       #print(folders)
       #print(finished_processes)
        
       for folder in folders:
          if (folder not in finished_processes):
             text_to_audio(folder)
             create_reel(folder)
             
             
             with open("finished_process.txt","a") as f:
              f.writelines(folder+"\n") 
       #time.sleep(15)    
         
  #''' if __name__ == "__main__":

    #with open("finished_process.txt", "r", encoding="utf-8") as f:
        #finished_processes = {
           # line.strip().lower() for line in f if line.strip()
        #}

    #folders = [
        #folder.strip().lower()
        #for folder in os.listdir("user_uploads")
       # if os.path.isdir(os.path.join("user_uploads", folder))
    #]

    #print("Folders:", folders)
    #print("Finished:", finished_processes)

    #for folder in folders:
     #   if folder not in finished_processes:
      #      text_to_audio(folder)
       #     create_reel(folder)

        #    with open("finished_process.txt", "a", encoding="utf-8") as f:
         #       f.write(folder + "\n")
  