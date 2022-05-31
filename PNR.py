import os
import os.path
import hashlib

def rename(p):
    os.chdir(p)
    entities = os.listdir(os.getcwd())
    file_count = 1
    for entity in entities:
        if os.path.isfile(entity):
            name, ext = os.path.splitext(entity)
            filename = str(file_count) + ext
            os.rename(entity, filename)
            file_count += 1
        else:
            new_path = os.path.join(p, entity)
            rename(new_path)
            os.chdir(p)

path = 'F:\Main1'
rename(path)
