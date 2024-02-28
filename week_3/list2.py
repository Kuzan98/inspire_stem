friends = ["James","jack","Jill","Jeremy","Johnson"]

for friend in friends:
    print(friend)

enemies = friends[:] # copy one list into another

# enemies = friends.append("James")

for enemies in enemies:  
    print(enemies)  


fruits = ["guava","apple","orange","pineapple","lemon"]  

# slice the list ie: get of thr list
print(fruits[0:3])

del fruits[0]

 print(fruits)

 squares = []# initialize an empty list

for x in range(0,11):
    