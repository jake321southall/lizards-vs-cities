class Lizard():
	def __init__(self, name, attack_power, belly_size, health, is_hungry = True):
		self.name = name
		self.attack_power = attack_power
		self.belly_size = belly_size
		self.health = health
		self.is_hungry = is_hungry

	def attack_city(self, city):
		if not self.is_hungry:
			print(f"{self.name} is not hungry. {city.name} is safe.") 
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
				print(f'{self.name} has ate {people_eaten}, {city.population} are left. {city.name} is preparing to attack.')
				city.attack_lizard(self)
class City():
	def __init__(self, name, population, attack_power, defence_capability):
		self.name = name
		self.population = population
		self.attack_power = attack_power
		self.defence_capability = defence_capability

	def attack_lizard(self, lizard):
		lizard.health -= self.attack_power
		if lizard.health < 0:
			print(f'{lizard.name} has been defeated and its organs have been donated for medical research.')
		else:
			print(f'{self.name} has removed {self.attack_power} from {lizard.name}\'s health. {lizard.name} has {lizard.health} health remaining.') 
			lizard.attack_city(self)


Godzilla = Lizard('Godzilla', 1000, 1000, 500)
Toyko = City('Toyko', 1500, 150, 10)
Godzilla.attack_city(Toyko)
