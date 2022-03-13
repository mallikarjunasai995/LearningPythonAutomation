import re
import os
def find_string_linenum(abs_path):
    stringie = 'DUMPLOG_NVME_REG'
    with open(abs_path,"r") as myFile:
        for num, line in enumerate(myFile, 1):
            if stringie in line:
                # print('in stringline fucntion',type(num))
                # print(line)
                return num
def filesizelist(folderfile):
    lists = []
    for filename in os.listdir(folderfile):
            abs_path = os.path.join(folderfile,filename)
            testregexfile = re.search(r'\.\d{3}'+'.log',abs_path)
            if testregexfile:
                listie = os.stat(abs_path).st_size
                lists.append(listie)
    return min(lists)  

def failpoint_text(full_path,linenum):
    newlinenum = linenum - 50
    # print(newlinenum)
    # print(os.stat(full_path))
    with open(full_path,'r') as file:
        # for i,line in enumerate(file):
        #     for i in range(newlinenum,linenum):
        #         print(line)
        content = file.readlines()
        #print(content[linenum-1])
        failure_content = content[newlinenum:linenum]
        #print(failure_content)
    print(failure_content)
    with open('failureresult.txt','a') as file1:
        for i in failure_content:

            file1.write(i)
        file1.write('-------------------\n\n')
        file1.write('------------------======-------')

def open_folder(key,input):
    res = re.search(r'\d{5}_'+key+r'_\d', input)
    if res:
        result = res.group()
        #print(result)
        folderfile = os.path.join(DIR_PATH,result)
        minsize = filesizelist(folderfile)
        #print(minsize)
        for filename in os.listdir(folderfile):
            abs_path = os.path.join(folderfile,filename)
            if os.stat(abs_path).st_size == minsize:
                        full_path = abs_path
                        linenum = find_string_linenum(abs_path)
                        # newlinenum = int(linenum)
                        #print('in folder function',type(linenum))
                        #print(type(linenum))
                        failpoint_text(full_path,linenum)


        
                  
DIR_PATH = 'C:\\Users\\7330728\\Desktop\\NewLogs2'
data = next(os.walk(DIR_PATH))[1]
keyelements = ['1597977','1597978']
for key in keyelements:
    for i in data:
        #print(type(i))
        #print(os.path.join(DIR_PATH,KEY))
        open_folder(key,i)
        