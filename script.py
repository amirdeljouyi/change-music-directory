import eyed3
import glob
import os
from shutil import copyfile

path = "./"
cp_path = "/media/media/Spotify/"
file_type = "mp3"
total_path = path + "*" + "." + file_type

mp3musics = glob.glob(total_path)
for file in mp3musics:
    mp3 = eyed3.load(file)
    artist = mp3.tag.artist
    album = mp3.tag.album
    directory = cp_path + artist
    subdirectory = directory + "/" + album
    filedirectory = subdirectory + "/" + file
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
    if not os.path.exists(filedirectory):
        copyfile(file, filedirectory)
    

