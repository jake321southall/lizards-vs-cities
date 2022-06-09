from classes import Lizard, City

Godzilla = Lizard('Godzilla', 1000, 1000, 500)
MechaGodzilla = Lizard('MechaGodzilla', 1500, 1100, 400)
Toyko = City('Toyko', 1500, 150, 10)
Babylon = City('Babylon', 600, 100, 20)

lizard_list = [Godzilla, MechaGodzilla]
city_list = [Toyko, Babylon]

print("Hi! Welcome to the City Vs Lizards simulator. Here are your Lizard options:")
print(*lizard_list, sep = "\n")
print("Here are your City options:")
print(*city_list, sep = "\n")


city_choice = input('Would you like to be Toyko or Babylon?')
while  city_choice not in ['Toyko', 'Babylon']:	
	city_choice = input('Please choose Toyko or Babylon!')
if city_choice == 'Toyko':
	user = Toyko
else:
	user = Babylon
lizard_choice = input('Would you like to face Godzilla or MechaGodzilla?')
while lizard_choice != 'Godzilla' and lizard_choice != 'MechaGodzilla':
	lizard_choice = input('Please choose Godzilla or MechaGodzilla!')
if lizard_choice == 'Godzilla':
	opponent = Godzilla
else:
	opponent = MechaGodzilla

user.attack_lizard(opponent)






