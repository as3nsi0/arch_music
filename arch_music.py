# -*- coding: utf-8 -*-
"""
This application allow us download the music from the youtube videos
Esta función permite  descargar la musica de los videos de Youtube

Output: A target directory where you save the songs in .mp3
Input: The output is a simple txt with the youtube links separate with line escapes

@author: Victor


Third parties: You required AVbin and ffmpeg
"""

import os
import ffmpy
import pafy
import shutil

# This allow us to download the video and the index to download
def download_videos(link, index):
    try:
        v = pafy.new(link)
        name_song = v.title
        #v.getbestaudio().download()
        audio = ''
        for name in v.audiostreams:
            if('ogg' in str(name)):
                audio = name
                break
        if(audio == ''):
            v.getbestaudio().download()
        else:
            audio.download(name_song+'.ogg')
    except:
        print("The song with the nex title: " + name_song + " has a problem to download.\n")
        name_song = ''
    return name_song

# This function allow us to change music format
def format_conversion(name, name_final, format='mp3'):
    try:
        ff = ffmpy.FFmpeg(inputs = {name:None},outputs = {name_final+'.'+format:None})
        ff.run()
    except:
        print('Ha fallado la conversión de '+name+ ' a ' + name_final)
    #cmd_call = 'ffmpeg -i '+name+' -acodec libmp3lame '+name_final+'.'+format
    #os.system(cmd_call)

output = 'Music/'
if(os.path.exists(output)):
    shutil.rmtree(output)
os.mkdir('Music')
f = open('test.txt','r')  
os.chdir(output) 
index = 1
lines = f.readlines()
f.close()
total_index = len(lines)
current_directory = os.getcwd()


list_of_names = {}

for link in lines:
    new_links = link.split('\n')
    link = new_links[0]
    print('\nYou are downloading ' + str(index) + ' of ' +  str(total_index) + '\n\n')
    name_video = download_videos(link, index)
    if(name_video != ''):
        list_of_names[name_video+'.ogg'] = name_video
    print('The video '+name_video+' was success download.\n')
    index+=1
    
list_of_files_remove = []

for key in list_of_names.keys():
    print('\n\nProcessed\n\n')
    # Eliminamos los simbolos que pueden causar problemas
    final_name = list_of_names[key]#.replace(' ', '_').replace('.','_').replace('&', 'and')
    format_conversion(key, final_name)
    list_of_files_remove.append(key)
    
for i in range(len(list_of_files_remove)):
    os.remove(list_of_files_remove[i])
