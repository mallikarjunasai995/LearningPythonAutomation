# positiveindex(starts with 0) and negative index  (first element will be -1 instead of -0 or 0 )
# find and rfind - substrings
# s='abcda'
# print(s.rfind('a'))

# #within the boundary only to search
# s.find('b',3,7) # in between 3 to 7 index only it will search
# s.index('z') #won't throw index error instead it will give -1
# s.count('b') #1
# i = s.find(subs)
# #to find all occurances of substring
# while i!=-1:
#     print('sadfsdf')
#     i = s.find(subs,i+len(subs),len(s))


# #replace : 
# s.replace(' ','')
# s.count(' ')

# split and join
# l = ['durga','software','solutions']
# s = '.'.join(l) #seperator.join()
# print(s)

# #startswith and endswith
# s.startswith(subs)
# s.endswith(subs)

# #typechecking
# s.islower(),s.isupper(),s.isalnum()

# # reverse a string
# s = 'durgasoft'
# output = s[::-1] 
# print(output)
# rev =reversed(s)
# rev = ''.join(rev)
# print(rev)

# #reverse orders of word present in given string
# s1 = 'how are you'
# l = s1.split(' ')
# l = l[: : -1]
# l1 = ' '.join(l)
# print(l1)

# reverse internal content of each word
# s1 = 'how are you'
# l = s1.split(' ')
# output = ''
# for i in l:
#     # print(i)
#     i = reversed(i)
#     i1 = ''.join(i)
#     output = output + ' ' + i1
#     # print(i1)
# print(output)
# # l = l[: : -1]
# # l1 = ' '.join(l)
# # print(l1)
# import string
# inp = list(string.ascii_lowercase)

# list of int elements to string
# my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_lst_str = ''.join(map(str, my_lst))
# print(my_lst_str)


# def count_code(strig):
#     countie=0
#     for i in inp:
#         substring = 'co'+i+'e'
#         # print(substring)
#         # print(strig)
#         m=strig.find(substring)
#         print(m)
#         if m == -1:
#             continue
        
#         while strig != -1:

#             if strig.find(substring,m+len(substring),len(strig)):

#             # i = s.find(subs,i+len(subs),len(s))
#                 countie = countie+1
#     return countie

# def count_code(str):
#     count = 0
#     for i in range(len(str)-3):
#         cur = str[i:i+4]
#         print(cur)
#         if cur[0:2] == "co" and cur[3] == "e": count += 1
#     return count


# count = count_code('cooebccoie')
# print(count)


# def xyz_there(str):
#   substr = "xyz"
#   i = len(substr)
#   for l in range(len(str)):
#     cur = str[l:l+3]
#     # print(cur)
#     # print(str.index(cur))
#     check = str.index(cur) -1
#     if cur == substr:
#         if str[check] == '.':
#             return False
#         return True
#     if l != len(str)-1:
#         continue
#     else:
#       if l != len(str)-1:
#         continue
#       else:
#         return False


# print(xyz_there('abc.xyz'))


# wap - input - aaaabbcc -4a2b2c
# remove duplicate characters from given string
# string = 'aaaabbcc'
# output = ''
# previous = 0
# for ch in string:
#     if ch not in output:
#         output = output + ch
# print(output)


# count the duplicate characters in a string 
# string = 'aaabbcccc'
# c=1
# nextpos = string[0]
# i=1
# cur = 0
# while i < len(string):

#     if string[i] == nextpos:
#         c= c+1
    
#     else:
#         # cur = cur+1
#         print(c)
#         nextpos = string[i]
#         c=1
#     if i == len(string)-1:
#         print(c)

#     i=i+1

# print half of the string
# def first_half(str):
#   l = len(str)
#   output = ''
#   l1 = int(l/2)
#   for i in range(l1):
#       output = output + str[i]
#   return output


# answer = first_half('WooHoo') 
# print(answer)
# def make_abba(a,b):
#     output = ''
#     output = output+a+b*2+a
#     return output

# print(make_abba('Hi', 'Bye'))
# check_string = 'am who am and my name is mallik'
# count = {}
# for s in check_string:
#   if s in count:
#     count[s] += 1
#   else:
#     count[s] = 1

# for key in count:
#   if count[key] > 1:
#     print (key, count[key])


# def big_diff(nums):
#     max = nums[0]
#     for i in nums:
#         if i > max:
#             max = i
#     print(max)

# big_diff([10, 11, 5, 6])

# def string_match(a, b):
#     lia = []
#     lib=[]
#     for i in range(len(a)-1):

#       current =a[i:i+2]
#       lia.append(current)
#     for i in range(len(b)):

#       current =b[i:i+2]
#       lib.append(current)
#     print(lia)
#     print(lib)



# string_match('xxcaazz', 'xxbaaz')



