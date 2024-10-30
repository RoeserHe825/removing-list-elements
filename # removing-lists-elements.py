# removing-lists-elements
# Henry Roeser
# 10/30/24

superbowl_snacks = ['popcorn,','chips','salsa','nuts','cheese','guacamole']
print(superbowl_snacks)
last_snack = superbowl_snacks.pop()
print(superbowl_snacks)
last_snack = superbowl_snacks.pop(0)
print(superbowl_snacks)
superbowl_snacks.remove('nuts')
print(superbowl_snacks)
del superbowl_snacks[2]
print(superbowl_snacks)

people = ['Lil Tecca','Michael Jackson','Lospollostv','Jaxsen Cano','Michael C. Hall']
print(f'You are invited to my dinner party {people[0]}!')
print(f"Sorry you can't make it to my dinner party {people[1]}!")
print(f'You are invited to my dinner party {people[2]}!')
print(f'You are invited to my dinner party {people[3]}!')
print(f'You are invited to my dinner party {people[4]}!')
people.remove('Michael Jackson')
print(f'{people} are all still invited to my dinner party!')
print(f'I can only invite two people to my dinner party now!')
people.pop(1)
print(f"Sorry Jaxsen Cano that you can't go to the dinner party!")
people.pop(2)
print(f"Sorry Michael C. Hall that you can't go to the dinner party!")
print(f'{people} are still invited to my dinner party!')
del people [0]
del people [0]
print(people)