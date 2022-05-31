import os
import os.path
import hashlib

def rename(path):
    os.chdir(path)
    entities = os.listdir(os.getcwd())
    pcount = 1
    vcount = 1
    for entity in entities:
        if os.path.isfile(entity):
            name, ext = os.path.splitext(entity)
            if ext == '.mp4' or ext == '.mov' or ext == '.MP4' or ext == '.avi' or ext == '.MOV':
                filename = 'Video' + str(vcount) + ext
                os.rename(entity, filename)
                vcount += 1
            elif ext == '.jpg' or ext == '.png' or ext == '.PNG' or ext == '.jpeg' or ext == '.JPG' or ext == '.gif' or ext == '.bmp':
                filename = str(pcount) + ext
                os.rename(entity, filename)
                pcount += 1
        else:
            new_path = os.path.join(path, entity)
            rename(new_path)
            os.chdir(path)

path_entered = input('Enter the path to perform the script on: ')
if os.path.exists(path_entered):
    rename(path_entered)
else:
    print('Path does not exist')
