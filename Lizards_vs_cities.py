class Lizard():
	def __init__(self, name, attack_power, belly_size, health, is_hungry = True, has_let_out_dying_roar = False, times_revived = 0):
		self.name = name
		self.attack_power = attack_power
		self.belly_size = belly_size
		self.health = health
		self.is_hungry = is_hungry
		self.has_let_out_dying_roar = has_let_out_dying_roar
		self.times_revived = times_revived

	def __repr__(self):
		return f'This is {self.name}. They have {self.attack_power} attack power, {self.belly_size} belly size, and {self.health} health.'

	def dying_roar(self):
		print(f'\"ROARRR!!!\", {self.name} has less than 250 health remaining.')

	def revive(self):
		self.health += 500
		print(f'{self.name} has revived 500 health so that its health is {self.health}.')

	def attack_city(self, city):
		if not self.is_hungry:
			print(f"{self.name} is not hungry. {city.name} is safe.") 
		elif self.health < 500 and self.times_revived < 1:
				self.revive()
				self.times_revived += 1
				print(f'{city.name} is preparing to attack {self.name}.')
				city.attack_lizard(self)
		else:
			self.belly_size -= self.attack_power/city.defence_capability
			if self.belly_size < 0:
				self.is_hungry = False
				city.population -= round(self.attack_power/city.defence_capability) - abs(self.belly_size)
				print(f"{self.name} is satisfied and {city.population} people have survived.")
			else:
				people_eaten = round(self.attack_power/city.defence_capability)
				new_population = city.population - people_eaten
				city.population = new_population
				print(f'{self.name} has ate {people_eaten}, {city.population} are left. {city.name} is preparing to attack {self.name}.')
				city.attack_lizard(self)
class City():
	def __init__(self, name, population, attack_power, defence_capability):
		self.name = name
		self.population = population
		self.attack_power = attack_power
		self.defence_capability = defence_capability

	def __repr__(self):
		return f"This is the city {self.name}. It has a population of {self.population}, attack power of {self.attack_power}, and defence capability of {self.defence_capability}."

	def attack_lizard(self, lizard):
		lizard.health -= self.attack_power
		if lizard.health < 0:
			print(f'{lizard.name} has been defeated and its organs have been donated for medical research.')
		else:
			if lizard.health < 250:
				lizard.dying_roar()
			print(f'{self.name} has removed {self.attack_power} from {lizard.name}\'s health. {lizard.name} has {lizard.health} health remaining.') 
			print(f'{lizard.name} is preparing to attack {self.name}.')
			lizard.attack_city(self)


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
	city_choice = input('Would you like to face Toyko or Babylon?')
	while  city_choice != 'Toyko' and city_choice != 'Babylon':	
		city_choice = input('Please choose Toyko or Babylon!')
else:
	city_choice = input('Would you like to be Toyko or Babylon?')
	while  city_choice != 'Toyko' and city_choice != 'Babylon':	
		city_choice = input('Please choose Toyko or Babylon!')
	lizard_choice = input('Would you like to face Godzilla or MechaGodzilla?')
	while lizard_choice != 'Godzilla' and lizard_choice != 'MechaGodzilla':
		lizard_choice = input('Please choose Godzilla or MechaGodzilla!')




