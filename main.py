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
scorers = f'{scorer1} + {goal_0}, {scorer2} + {goal_1}'
# wie scoorde wanneer in 2 strings
report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'
# second part of the exercise
# define player
player = 'Hans van Breukelen'
# use slicing to isolate the first name of the player
first_name = player [:4]
# define the length of the last name, using 'len'
# 4 plus a space gives 5 till the end of the name, wich should provide us with the length of the last name
last_name_len = len(player[5:])
#define players name in short
name_short = 'H. van Breukelen'
chant = f'{first_name}!'  * 4
print(chant)
# still not possible to seperate the name or add exclamationmark
good_chant = chant
good_chant != chant
# I still don't know what to do here, what is asked.









