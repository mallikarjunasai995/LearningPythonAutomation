#simpleconversionofstring2dict
def multiple_letter_count(string):
	    #return {letter: string.count(letter) for letter in string}
	    dicti = {}
	    for letter in string:
	        dicti[letter] = string.count(letter)
	    return dicti
	    
multiple_letter_count('stringgg')

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')

#spotify_Playlist_Example #nested dictionary

#dictionary_Comprehension
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}

#how to access dictionraies, lists by different ways