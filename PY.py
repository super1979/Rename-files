import os
import os.path
import hashlib

os.chdir('F:\Main1')
entities = os.listdir(os.getcwd())
pcount = 20327
vcount = 1
for entity in entities:
    name, ext = os.path.splitext(entity)
    if ext == '.mp4' or ext == '.mov' or ext == '.MP4' or ext == '.avi' or ext == '.MOV':
        filename = 'Video' + str(vcount) + ext
        os.rename(entity, filename)
        vcount += 1
    elif ext == '.jpg' or ext == '.png' or ext == '.PNG' or ext == '.jpeg' or ext == '.JPG' or ext == '.gif' or ext == '.bmp':
        filename = str(pcount) + ext
        os.rename(entity, filename)
        pcount += 1
