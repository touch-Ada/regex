import random

die_one = ['\d', 'E', 'I', 'S', 'A', '[a-z]']
die_two = ['*', '?', '+', '\\b', '{2}', '\\n']
die_three = ['\D', 'N', 'R', 'T', '.', '\s']

print(f"{random.choice(die_one)}{random.choice(die_two)}{random.choice(die_three)}")