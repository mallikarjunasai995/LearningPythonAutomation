# -*- coding: utf-8 -*-
import re
import os
import pythonjson
import sys
def find_string_linenum(abs_path):
    stringie = 'DUMPLOG_NVME_REG'
    perf_io = 'FillDisk FAILED!'
    smart_verify = 'Smart Data Verification failed.'
    with open(abs_path,"r") as myFile:
        for num, line in enumerate(myFile, 1):
            if perf_io in line:
                print(num)
                print('Hello am here finally - perfio command')
                return num
            if stringie in line:
                # print('in stringline fucntion',type(num))
                # print(line)
                #for error keyword do soemthing here
                fin_num = finderrorkey(abs_path,num,)

                return fin_num
            if smart_verify in line:
                return num
        newnum = num -1
        return newnum
        # sys.exit(0)
        # num = myFile.seek()
            # else:
            #     print('seriously am here sir now')
            #     sys.exit(0)
def filesizelist(folderfile):
    lists = []
    for filename in os.listdir(folderfile):
            abs_path = os.path.join(folderfile,filename)
            testregexfile = re.search(r'\.\d{3}'+'.log',abs_path)
            if testregexfile:
                listie = os.stat(abs_path).st_size
                lists.append(listie)
    return min(lists) if lists else None
def finderrorkey(abs_path,num):

    newlinenum = num - 50
    with open(abs_path,'r') as file:

            # for i,line in enumerate(file):
            #     for i in range(newlinenum,linenum):
            #         print(line)
        content = file.readlines()
        failure_content = content[newlinenum:num]
        newstring = 'Error:'
        flag = 0
        for line in failure_content:
            if newstring in line:
                flag = 1
                print('string found')
                break

        if flag == 1:
            # print ('string found')
            return num
        else:
            failure_content = 'mallik'
            print('still not found - search for the error: keyword in file')
            errorkeyword = content[:newlinenum][::-1]
            # print(type(content[:newlinenum][::-1]))
            count = 0
            lists = []
            for i in errorkeyword:
                if newstring in i:
                    count = count + 1
                    lists.append(i)
                    # print('\n')
                    if count >2:
                        break
            # print(lists[0])
            for index,line in enumerate(content):
                if lists[0] == line:
                    # print(index)
                    break
            # failure_content = content[index-50:index]
            print(index)
            return index+3
                
def failpoint_text(full_path,linenum,testnm,key):
    if linenum:
        newlinenum = linenum - 50
        with open(full_path,'r') as file:
            # for i,line in enumerate(file):
            #     for i in range(newlinenum,linenum):
            #         print(line)
            content = file.readlines()
            failure_content = content[newlinenum:linenum]
            
        with open('failureresult.txt','a') as file1:
            file1.write('\n \n')
            file1.write('Test Name: '+testnm+ ' Test ID: '+ str(key)+' Launch ID: '+ str(pythonjson.launchID))
            file1.write('------------------======------------------------------------------------------------------\n')
            file1.write('\n')
            for i in failure_content:
                file1.write(i)
            file1.write('------------------======------------------------------------------------------------------\n')
            file1.write('------------------======------------------------------------------------------------------\n')
            file1.write('\n')
    else:
        with open('failureresult.txt','a') as file2:
            file2.write("Could be setup issue/drive issue - din't find dump logs")
            file2.write('Test Name: '+testnm+ 'Test ID: '+str(key)+'Launch ID: '+ str(pythonjson.launchID))
            file2.write('\n')
            file2.write('------------------======------------------------------------------------------------------\n')
            file2.write('\n')

def open_folder(key,input,testnm):
    res = re.search(r'\d{5}_'+str(key)+r'_\d', input)
    if res:
        result = res.group()
        #print(result)
        folderfile = os.path.join(DIR_PATH,result)
        print(folderfile)
        minsize = filesizelist(folderfile)
        # print(minsize)
        for filename in os.listdir(folderfile):
            abs_path = os.path.join(folderfile,filename)
            if minsize == None:
                print('think what to do man')
                failpoint_text(abs_path,0,testnm,key)
                # sys.exit(0)
            if os.stat(abs_path).st_size == minsize:
                        full_path = abs_path
                        linenum = find_string_linenum(abs_path)
                        # if linenum == None:
                        #     print('log generated but not sure setup/drive issue')
                        #     # sys.exit(0)
                        #     failpoint_text(full_path,linenum,testnm,key)
                        # newlinenum = int(linenum)
                        #print('in folder function',type(linenum))
                        #print(type(linenum))
                        failpoint_text(full_path,linenum,testnm,key)
                 
DIR_PATH = 'D:\\tests\\NewLogs2'
data = next(os.walk(DIR_PATH))[1]
# print(data)
# sys.exit(0)
# print(pythonjson.failedinstanceID)
keyelements = pythonjson.failedinstanceID
tst_names = pythonjson.test_names

# print(type(keyelements))
for key,testnm in zip(keyelements,tst_names):
    # print(key)
    # print(testnm)
    for i in data:
        # print(type(i))
		# print(type(key))
        open_folder(key,i,testnm)

# import re
# import os
# def find_string_linenum(abs_path):
#     stringie = 'DUMPLOG_NVME_REG'
#     with open(abs_path,"r") as myFile:
#         for num, line in enumerate(myFile, 1):
#             if stringie in line:
#                 # print('in stringline fucntion',type(num))
#                 # print(line)
#                 return num
# def filesizelist(folderfile):
#     lists = []
#     for filename in os.listdir(folderfile):
#             abs_path = os.path.join(folderfile,filename)
#             testregexfile = re.search(r'\.\d{3}'+'.log',abs_path)
#             if testregexfile:
#                 listie = os.stat(abs_path).st_size
#                 lists.append(listie)
#     return min(lists)

# def failpoint_text(full_path,linenum):
#     newlinenum = linenum - 50
#     # print(newlinenum)
#     # print(os.stat(full_path))
#     with open(full_path,'r') as file:
#         # for i,line in enumerate(file):
#         #     for i in range(newlinenum,linenum):
#         #         print(line)
#         content = file.readlines()
#         #print(content[linenum-1])
#         failure_content = content[newlinenum:linenum]
#         #print(failure_content)
#     print(failure_content)
#     with open('failureresult.txt','a') as file1:
#         for i in failure_content:

#             file1.write(i)
#         file1.write('-------------------\n\n')
#         file1.write('------------------======-------')

# def open_folder(key,input):
#     res = re.search(r'\d{5}_'+key+r'_\d', input)
#     if res:
#         result = res.group()
#         #print(result)
#         folderfile = os.path.join(DIR_PATH,result)
#         minsize = filesizelist(folderfile)
#         #print(minsize)
#         for filename in os.listdir(folderfile):
#             abs_path = os.path.join(folderfile,filename)
#             if os.stat(abs_path).st_size == minsize:
#                         full_path = abs_path
#                         linenum = find_string_linenum(abs_path)
#                         # newlinenum = int(linenum)
#                         #print('in folder function',type(linenum))
#                         #print(type(linenum))
#                         failpoint_text(full_path,linenum)


        
                  
# DIR_PATH = 'C:\\Users\\7330728\\Desktop\\NewLogs2'
# data = next(os.walk(DIR_PATH))[1]
# keyelements = ['1597977','1597978']
# for key in keyelements:
#     for i in data:
#         #print(type(i))
#         #print(os.path.join(DIR_PATH,KEY))
#         open_folder(key,i)