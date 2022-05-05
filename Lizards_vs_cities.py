from classes import Lizard, City

Godzilla = Lizard('Godzilla', 1000, 1000, 500)
MechaGodzilla = Lizard('MechaGodzilla', 1500, 1100, 400)
Toyko = City('Toyko', 1500, 150, 10)
Babylon = City('Babylon', 600, 100, 20)

print("Hi! Welcome to the City Vs Lizards simulator. Here are your Lizard options:")
print(Godzilla)
print(MechaGodzilla)
print("Here are your City options:")
print(Toyko)
print(Babylon)

city_or_lizard_choice = input('Would you like to be a Lizard or a City?')
while city_or_lizard_choice != 'Lizard' and city_or_lizard_choice != 'City':
	city_or_lizard_choice = input('Please pick Lizard or City!')

if city_or_lizard_choice == 'Lizard':
	lizard_choice = input('Would you like to be Godzilla or MechaGodzilla?')
	while lizard_choice != 'Godzilla' and lizard_choice != 'MechaGodzilla':
		lizard_choice = input('Please choose Godzilla or MechaGodzilla!')
	if lizard_choice == 'Godzilla':
		user = Godzilla
	else:
		user = MechaGodzilla
	city_choice = input('Would you like to face Toyko or Babylon?')
	while  city_choice != 'Toyko' and city_choice != 'Babylon':	
		city_choice = input('Please choose Toyko or Babylon!')
	if city_choice == 'Toyko':
		opponent = Toyko
	else:
		opponent = Babylon
else:
	city_choice = input('Would you like to be Toyko or Babylon?')
	while  city_choice != 'Toyko' and city_choice != 'Babylon':	
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






