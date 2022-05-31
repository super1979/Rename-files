import os
import os.path
import hashlib

def rename(p):
    os.chdir(p)
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
            new_path = os.path.join(p, entity)
            rename(new_path)
            os.chdir(p)

path = 'F:\Main1'
rename(path)
