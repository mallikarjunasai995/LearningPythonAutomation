# #lists&AccessingData
# my_stuff = [1, 2, 3, 4, "Camera", 2.5]
# # Define nums
# nums = list(range(1,100))

# #changing value in a list at particular index
# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# # DON'T TOUCH THIS PLEASE!
# #Change "Hanna" to "Hanna"
# people[0] = "Hannah"
# #Change "Geoffrey" to "Jeffrey"
# people[4] = "Jeffrey"


# #listiteration
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s
# result = result.upper()

# #list-Appened,insert&Extend
# instructors.extend(["Colt", "Blue", "Lisa"])
# instructors.append("Mona")
# # vowel list
# vowel = ['a', 'e', 'i', 'u']
# # 'o' is inserted at index 3 (4th position)
# vowel.insert(3, 'o')
# z
# #list-clear,pop,remove
# vowel.clear()
# vowel.pop()   #willremovelastelement
# vowel.pop(2)  #removes3rdposition element
# vowel.remove(3) #removesvalue 3 in the list

# #ListMethods - index,count,reverse,sort
# numbers = [5,6,7,5,8,6,7,8,4,6]
# numbers.index(8,6,8) #first8 -value,2&3 values represent index positions
# numbers.count(5) #how many 5's in the list


# #Comprehension
# friends = ['ashley', 'matt', 'michael']
 
# [friend[0].upper() + friend[1:] for friend in friends] # this actually returns ['Ashley', 'Matt', 'Michael']

# #strings - 


# #aliasing and cloning of list objects

# #cloning - process of creating duplicate object
# #cloning - slicing and copy method will refer to another object



# #lists --- methods which will modify or not
# #how to find duplicate elements in the list
# #how to count duplicate elements
# #how to found duplicate elements in the list - malli .. print output should be - malilililili
# #logical operator - bit programming



#tuple, dictionary - 


# def sum_pairs(lst,num):
#     for i in range(len(lst)-1):
#         # print(lst[i])
#         if lst[i]+lst[i+1] == num:
#             print(lst[i])
#             # print(list[i+1])
#             return lst[i:i+2]
            
#         else:
#             None

# sum_pairs([4,2,3,4,5],6)


A = [1,3,4,5,6,7,8,9,0,2]
# n = len (A)
# print(n)
# for i in range(n):
#     print(i)


print(A)


# def range_in_list(lst,start=0,stop=None):
#     output = 0
#     stop = stop or lst[-1]
#     if stop < lst[-1]:
#         stop = stop+1
#     for i in range(start,stop):
#        output = output + lst[i]
#     print(output)   
#     return output


# range_in_list([1,2,3,4],0,2)


Numbers = [90,78,34,50,100,99]

# for num in Numbers:
#     print(num)



leng = len(Numbers)
for i in range(leng-1):
    print(Numbers[i])










