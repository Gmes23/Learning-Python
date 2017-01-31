alien_0 = {'color': 'red', 'power': 5, 'points': 1}

aliens = []
# making 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'red', 'power': 5, 'points': 1}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'red':
       alien['color'] = 'yellow'
       alien['power'] = 10
       alien['points'] = 10

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
    print("...")
# showing how many aliens have been created
print("total numbers of aliens created: " + str(len(aliens)))

# dictionaryception

users = {
    'lupe': {
       'first': 'lupe',
       'color': 'blue',
       'location': 'far away',
    },
    'jack':{
       'first': 'jack',
       'color': 'red',
       'location': 'near',
    },
}

for username, users_info in users.items():
    print("username: " + username)
    full_name = users_info['first'] + " " + users_info['color']
    location = users_info['location']
    print("\tFull name: " + full_name.title())
    print("\tlocation:" + location.title())
