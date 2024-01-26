#this is the first project that I've written in python outside of school so I'm not that good 
#feel free to write a PR if you think that you've improved it
#    Copyright (C) 2024  Skeleton_craft
#        Distrabuted with permision by Michael Paulsen 
#    This program comes with ABSOLUTELY NO WARRANTY.
#    This is free software, and you are welcome to redistribute it

from json import loads, dumps
from sys import argv, exit
argc = len(argv) 
start_pos = [0,0,0]
end_pos = [0,0,0]
if argc < 2 :
    print("usage", argv[0], "[file path] <startx starty startz> <endx endy endz>")
    print("exiting")
    exit()
#get the start position of the camera path
#if not all three chords are passed in via the command line 
#prompt the user for all three

if argc < 5 :
    start_pos[0] = int(input("enter the start x "))
    start_pos[1] = int(input("enter the start y "))
    start_pos[2] = int(input("enter the start z "))
else: 
    start_pos[0] = float(argv[2])
    start_pos[1] = float(argv[3])
    start_pos[2] = float(argv[4])
#this isn't very DRY code but IDK python well enoug to do it better
if argc < 8 :
    end_pos[0] = int(input("enter the end x "))
    end_pos[1] = int(input("enter the end y "))
    end_pos[2] = int(input("enter the end z "))
else: 
    end_pos[0] = float(argv[5])
    end_pos[1] = float(argv[6])
    end_pos[2] = float(argv[7])

    
    
#print(start_pos) 

#get the path of the file passed in via the command line
file_path = argv[1]

#open that file for reading
file = open(file_path, "r")

#get the contents of the file (i am sure that there's a better way to do this)
file_contents = "" 
for x in file:
    file_contents += x
    
#parse the json data from the file then get the LR keyframes    
camera_data = loads(file_contents)
camera_path = camera_data[''][1]['keyframes']
for kf in camera_path : 
    kf_pos = kf['properties']['camera:position'] 
    posx = (float(kf_pos[0]) - start_pos[0]) + end_pos[0] 
    posy = (float(kf_pos[1]) - start_pos[1]) + end_pos[1]
    posz = (float(kf_pos[2]) - start_pos[2]) + end_pos[2]
    #print(posx, posy, posz);
    kf['properties']['camera:position'] = [ posx, posy, posz] 
    
out_file = open("timelines.json", "w")
#this uses double quotes I hope it works!
out_file.write(dumps(camera_data))