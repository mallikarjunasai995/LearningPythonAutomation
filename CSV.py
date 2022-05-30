# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!


from csv import writer
with open('fighters.csv','w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["character","move"])
    csv_writer.writerow(["ryu",'Hadyouken'])




# with open("fighters.csv") as file:
#     data = file.read()

# # Using reader
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader) #To skip the headers
#     for fighter in csv_reader:
#     	# Each row is a list
#     	# Use index to access data
#     	print(f"{fighter[0]} is from {fighter[1]}") 

# # Example where data is cast into a list
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)

# # Reading/Parsing CSV Using a DictReader:
# from csv import DictReader
# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         # Each row is an OrderedDict!
#         print(row['Name']) #Use keys to access data\



# 4 text files - emplname , employee number
import os
import csv

with open('txt1.txt', 'w') as file1:
    file1.write('1 john 100')


with open('txt2.txt', 'w') as file2:
    file2.write('2 john2 101')

with open('txt3.txt', 'w') as file3:
    file3.write('3 john3 102')

with open('txt4.txt', 'w') as file4:
    file4.write('4 john4 103')

fields = ['S.NO','EMPLOYEENAME','EMPLOYEENUMBER']

# csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(fields) 
        
#     # writing the data rows 
#     csvwriter.writerows(rows)

filename = 'output.csv'

with open(filename,'w+') as out:
    for i in range(1,4):
        with open('txt'+str(i)+'.txt','r') as file1:

            # print(os.cwd())
            outputtext = file1.readlines()
            # print(outputtext)
            li = []
            for word in outputtext:
                # print(word)
                # print(type(word))
                outp = word.split(' ')
                li.append(outp)
            print(li)
                # csvwriter = csv.writer(out)
                # csvwriter = csvwriter.writerow(fields)
                # csvwriter = csvwriter.writerow(outp)


            print(outp)
            print(type(outp))
            # print(outs) 
            # print(li)
            # newout = outputtext.split(' ')
            # print(newout)
            # print(outputtext)
            # outputtext = str(outputtext)
            csvwriter = csv.writer(out)
            csvwriter = csvwriter.writerow(fields)
            csvwriter = csvwriter.writerows(outp)

           

            # out.write(outputtext)
            # out.write('\n')
    



# execel contains - serial number , empno, emnumber 







