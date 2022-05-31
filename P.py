import os
import os.path
import hashlib

os.chdir('F:\Main1')
entities = os.listdir(os.getcwd())
file_count = 1
for entity in entities:
    name, ext = os.path.splitext(entity)
    filename = str(file_count) + ext
    os.rename(entity, filename)
    file_count += 1
