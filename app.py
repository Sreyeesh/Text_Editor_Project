friends = {'Rolf', 'Jen', 'Ana'}
user_friends = set()
print(user_friends)
user = input("Name of the friend: ")
user_friends.add(user)
 
nearby_people = friends.intersection(user_friends)
print(''.join(nearby_people))