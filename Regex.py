#regularexpressions
#quantifiers - one or more , how many times needs to be there that particular word or digit 
#character class and sets - [],{} 
#anchors and boundaries - ^ - start of line , \b - word boundary , $-ends exactly with this symbol
#logical OR and character gorups = | - logical or  , paranthesis ()
#REGULAR expression objects - once compile then use multiple times
#module regex - compile it everytime and search for string
import pythonjson
import re
import os
import glob
import fnmatch
def find_string_linenum(abs_path):
    stringie = 'DUMPLOG_NVME_REG'
    with open(abs_path,"r") as myFile:
        for num, line in enumerate(myFile, 1):
            if stringie in line:
                print('in stringline fucntion',type(num))
                print(line)
                return num
def open_folder(key,input):
    #print(data)
    #print(input)
    #print(key)
    res = re.search(r'\d{5}_'+key+r'_\d', input)
    if res:
        result = res.group()
        #print(result)
        folderfile = os.path.join(DIR_PATH,result)
        #print(folderfile)
        #print(folderfile)
        # for root,dirs,files in os.path.join(DIR_PATH,result):
        #     print(files)
        #files = [f for f in os.listdir(folderfile) if os.path.isfile(f)]
        lists = []
        for filename in os.listdir(folderfile):
            #print(type(filename))
            # print(fnmatch.filter(filename,'.log'))
            # files = glob.glob(".log")
            # print(files)
            abs_path = os.path.join(folderfile,filename)
            testregexfile = re.search(r'\.\d{3}'+'.log',abs_path)
            #print(filename)
            # testregexfile.group()


            #print(testregexfile.group())
            if testregexfile:
                #print(filename)
               # print(abs_path)
                #print(os.stat(abs_path)) 
                listie = os.stat(abs_path).st_size
                #print(listie)
                lists.append(listie)
                minsize = min(lists)
                if  os.stat(abs_path).st_size == minsize:

                     #file1 = open(abs_path,'r')
                     #reading = file1.read()
                     #print(reading)
                    linenum = find_string_linenum(abs_path)
                    # newlinenum = int(linenum)
                    print('in folder function',type(linenum))
                    # print(linenum)
                    # start = linenum-50
                    # for i in range(start,linenum):
                    #     print(i)
                     
                        #  lines = myFile.read()
                        #  print(lines)
                    # with open(abs_path,'r') as file:
                    #     file.readline()              
        #print(type(lists))        
        #return min(lists)     
            #print(abs_path)
            #if abs_path.lower().endswith(r'.'+'\d{3}'+'.log'):
                #print('yes I found one file')
                #filesize =os.stat(abs_path).st_size
                #print(filesize)
                #print(type(filesize))
            # f = open(os.path.join(folderfile,filename),'r')
            #result = f.read()
            #print(result[5])
            #print(filename1)
            # with open(filename1) as f:
            #     result1 = f.read()
            #     print(result1[0])
            
        # for lists in os.walk(folderfile):
        #     files = (lists[2])
        #     for file in files:
        #         print(file)
        #         print(type(file))
        #         # with open(file,'r') as f:
        #         #     reading = f.read()
        #         #     print(reading)
    
DIR_PATH = 'C:\\Users\\7330728\\Desktop\\NewLogs2'
data = next(os.walk(DIR_PATH))[1]
print(pythonjson.failedinstanceID)
keyelements = ['1597977']
#print(data)
#print(keyelements)
#print(type(data))
for key in keyelements:
    for i in data:
        #print(type(i))
        #print(os.path.join(DIR_PATH,KEY))
        open_folder(key,i)
        break
        #if result1:
            #print(type(result1))
            #print(result1)
            #break
            #minfile = min_filesize(result1)
            #print(minfile)
            #print(abs_path)
# import os
# KEY = '1597977'
# print(os.path.join(DIR_PATH,KEY))


# for root,dirs,files in os.walk(DIR_PATH):
#     print(files)
for i in data:
	print(type(i))
	key1 = str(key)
    



