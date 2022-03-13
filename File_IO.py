#CURSOR MOEMENT 
# fil = open('story.txt')
# print(fil.read())
# fil.seek(0)
# print(fil.readline())
# #closethefile
# fil.close()
# print(fil.closed)


#withstatement
# with open('story.txt') as f: 
#     data = f.read()

# #writing into a file
# with open('newstory.txt','w') as w:
#     w.write('hi am wriring my first file \n')

#append into a file 

# with open('newstory.txt','a') as f:
#     f.write(':) \n')
#     f.seek(0)

#r+ - read and write into a file ,  - only works with existing files 
# with open('newstory.txt','r+') as f :
#     f.write(':) :) :)')
#     print(f.read())

#findand replace using replace function : 

# def find_and_replace(filename,old,new):
#     with open(filename,'r+') as file:
#         text = file.read()
#         new_text = text.replace(old,new)
#         file.seek(0)
#         file.write(new_text)


	# 1. File search
	# 	a. Search with some ID in the folder
	# 	b. Open that specific ID Folder
    #     c. In that , open the file with less size with .log extension

# def dymanicpath(foldname):
#     directory = 0
#     foldername = 0
#     filename = 0
#     return directory + foldername + filename
import re
stringie = 'DUMPLOG_NVME_REG'
with open("C:\\Users\\7330728\\Desktop\\NewLogs2\\42081_1597977_6\\DVT_OG-HOST-WDIN167_1597977_setGet_getSetFID02_002_21382A640805.6.83_00_00.0.6934.001.log","r") as myFile:
    for num, line in enumerate(myFile, 1):
        if stringie in line:
            print(num)
            new_num = num-50
            print(new_num)
            print(myFile.readline(num))

    # data = file.read()
    # new_text = data
    #stringie = 'DUMPLOG_NVME_REG'
    #regex = re.compile(r'\={1,}'+stringie+r'\={1,}')
    # output = regex.findall(data)
    # print(output)
    # for i,new_text in enumerate(file):
    #     print(i)

    
    



    
#how to open a folder with knwoing only speicifc string name

# import os
# key = '15f97977'
# with os.scandir('C:\\Users\\7330728\\Desktop\\NewLogs2') as dircontents:
#     for i in dircontents:
#         pass
#         #use regex or stringmethods to pass the key exactly in the middle and open the file
#         # if substr( dircontents:
#         #     print(i)

        