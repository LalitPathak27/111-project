import os
import shutil

from_dir= "C:/Users/patha/Downloads"
to_dir = "C:/Users/patha/OneDrive/Desktop"

list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name , extension = os.path.splitext(file_name)
    
    if extension == "":
        continue

    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif'] :

        path1  = from_dir + '/' + file_name 
        path2 = to_dir + '/' + "image folder"
        path3 = to_dir + '/' + "image folder" + '/' + file_name

        if os.path.exists(path2):
            print("moving " + file_name)
            shutil.move(path1 , path3)
        else:
            os.makedirs(path2)
            print("moving " + file_name)
            shutil.move(path1 , path3)    
          
