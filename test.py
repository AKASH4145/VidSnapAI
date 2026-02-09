import os

folders=os.listdir("user_uploads")
       #print(folders)
       #print(finished_processes)

with open("finished_process.txt","w+") as f:
     finished_processes=f.readlines()
     for folder in folders:
          if (folder not in finished_processes):
            # text_to_audio(folder)
            # create_reel(folder)
             
             
             with open("finished_process.txt","a") as f:
              f.writelines(folder+"\n")


        
