#lists&AccessingData
my_stuff = [1, 2, 3, 4, "Camera", 2.5]
# Define nums
nums = list(range(1,100))

#changing value in a list at particular index
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"


#listiteration
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()

#list-Appened,insert&Extend
instructors.extend(["Colt", "Blue", "Lisa"])
instructors.append("Mona")
# vowel list
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

#list-clear,pop,remove
vowel.clear()
vowel.pop()   #willremovelastelement
vowel.pop(2)  #removes3rdposition element
vowel.remove(3) #removesvalue 3 in the list

#ListMethods - index,count,reverse,sort
numbers = [5,6,7,5,8,6,7,8,4,6]
numbers.index(8,6,8) #first8 -value,2&3 values represent index positions
numbers.count(5) #how many 5's in the list


#Comprehension
friends = ['ashley', 'matt', 'michael']
 
[friend[0].upper() + friend[1:] for friend in friends] # this actually returns ['Ashley', 'Matt', 'Michael']

