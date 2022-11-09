from classes import Lizard, City
#from functions import minimax

Godzilla = Lizard('Godzilla', 1000, 1000, 500, 50)
MechaGodzilla = Lizard('MechaGodzilla', 1500, 1100, 400, 50)
Toyko = City('Toyko', 1500, 150, 10, 50)
Babylon = City('Babylon', 600, 100, 20, 50)

lizard_list = [Godzilla, MechaGodzilla]
city_list = [Toyko, Babylon]


print("Hi! Welcome to the City Vs Lizards simulator. Here are your Lizard options:\n")
print(*lizard_list, sep = "\n")
print("Here are your City options:\n")
print(*city_list, sep = "\n")


city_choice = input('Would you like to be Toyko or Babylon?\n')
while  city_choice not in ['Toyko', 'Babylon']:	
	city_choice = input('Please choose Toyko or Babylon!\n')
if city_choice == 'Toyko':
	user = Toyko
else:
	user = Babylon
lizard_choice = input('Would you like to face Godzilla or MechaGodzilla?\n')
while lizard_choice != 'Godzilla' and lizard_choice != 'MechaGodzilla':
	lizard_choice = input('Please choose Godzilla or MechaGodzilla!\n')
if lizard_choice == 'Godzilla':
	lizard = Godzilla
else:
	lizard = MechaGodzilla

print('Let the battle begin!\n')

while user.health > 0 and lizard.health > 0:
	attack_or_rebuild = input('Would you like to attack or rebuild?')
	while attack_or_rebuild not in ['attack', 'rebuild']:
		attack_or_rebuild = input('Please choose attack or rebuild!')
	if attack_or_rebuild == 'attack':
		user.attack_lizard(lizard)
	else:
		user.rebuild()
	print(f'{lizard.name} is preparing to make its move on {user.name}.\n')
	#applying the minimax algorithm, cities are always the maximising players and lizards are always minimising
	lizard_attack_or_revive = minimax(user, opponent, is_maximising = False)[1]
	if lizard_attack_or_revive == 'attack':
		lizard.attack_city(user)
	else:
		lizard.revive()






print('End!')

#user.attack_lizard(opponent)






