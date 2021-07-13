#tuples are immutable && faster than lists
#we can use this for months, lcoaitons which are like uninversal facts in nature and won't change throughout the program/produciton code

months = ('january','februaruy','march','april')
locations = {
  (1.03,2.05):"Tokyo office"
  (1.23,2.98):"Chaina"
}

#sets
#use case: to find unique elements or remove duplicates in an registration events
s = {1,2,3,4,4,5,3}
print(set(s))
s.add(8) #will add to the set
s.add(2) #won't add beucase of duplicate item
s.remove(2) #keyerror if not found , discard method we can use to not get the 
#sets use union , and , intersection methods




