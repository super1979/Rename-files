import os
import os.path
import hashlib

def rename(path):
    os.chdir(path)
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
            os.chdir(path)

path_entered = input('Enter the path to perform the script on: ')
if os.path.exists(path_entered):
    rename(path_entered)
else:
    print('Path does not exist')
