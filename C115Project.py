import os
import shutil

source='C:/Users/slane/OneDrive/Documents/New folder/main.txt'
dest='C:/Users/slane/OneDrive/Documents/New folder/slane.txt'

if(os.path.exists(source)):
    os.rename(source,dest)
    print('renamed')