colors = ['red', 'blue', 'yellow']

print(sorted(colors))

lencolors = len(colors)

print(lencolors)

for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

minsquare = min(squares)
print(minsquare)
maxsquare = max(squares)
print(maxsquare)

print(525/65)

players = ['ana', 'lupe', 'star', 'jack']
player_two = players[:]
print(players[0:2])
print(players[1:2])
print(players[3])
players.append('red')
player_two.append('blue')
print(players)
print(player_two)
favorite_languages = {
    'jen': 'python',
    'dave': 'java',
    'steve': 'C',
    'lupe': 'javascript',
    }
friends = ['jen', 'lupe']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + " , I see you favorite language is " +
        favorite_languages[name].title() + " !")
