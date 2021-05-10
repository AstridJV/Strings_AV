# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# First part of the exercise
# wie maakte de doelpunten:
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

#in welke minuut vielen de doelpunten:
goal_0 = 32
goal_1 = 54

# scorers en minuten waarin de doelpunten vielen samen:
scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)

# wie scoorde wanneer in 2 strings
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'

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

#define players name in short: index0 + Make sure the last character of this string is not a space!
name_short = player[0] + '.' + player[player.find(' '): len(player)]
chant = (f'{first_name}! '  * len(player[:player.find(' ')]))[:-1]

# [-1]
print(chant)
# print('***',chant,'***')

# TO DO: good_chant: use !=
# TO DO: good_chant = is the last character of the chant a white space?
# definieer chant boolean, bevestig dat het laatste karakter idd een ! is TRUE, en niet " " FALSE
# zodat de good_chant TRUE wordt.
chant[-1] == "!"
chant[-1] == " "
chant[-1] != " "
good_chant = chant[-1] != " "
print(good_chant)















