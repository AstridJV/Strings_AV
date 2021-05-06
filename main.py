# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# wie maakte de doelpunten:
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
#in welke minuut vielen de doelpunten:
goal_0 = 32
goal_1 = 54
# scorers en minuten waarin de doelpunten vielen samen:
scorers = (scorer1) + " " + str(goal_0) + ", " + (scorer2) + " " + str(goal_1)
# wie scoorde wanneer in 2 strings
report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'
# second part of the exercise
# define player
player = 'Hans van Breukelen'
# use slicing to isolate the first name of the player
first_name = player[0:player.find(" ")]
print(first_name)
# define the length of the last name, using 'len', slicing and find
last_name = player[player.find(" ") + 1:]
print(last_name)
last_name_len = len(last_name)
print(len(last_name))
#define players name in short: index0 + 
name_short = player[0:1] + '.' + player[player.find(' '): len(player)]
chant = (f'{first_name}! '  * len(player[0:player.find(' ')]))
# [:-1]
print(chant)

print('***',chant,'***')

# TO DO: good_chant: use !=
print(chant[-1])
good_chant = True
# TO DO: good_chant = is the last character of the chant a white space?
#      good_chant == chant[-1]
#      good_chant != chant
chant = (f'{first_name}! '  * len(player[0:player.find(' ')]))

good_chant = (f'{first_name}! '  * len(player[0:player.find(' ')]))[:-1]
good_chant != chant














