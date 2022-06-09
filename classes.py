from functions import *

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
			if self.belly_size < 0 or city.population <= 0:
				print(f"{self.name} has defeated {city.name}.") 
			else:
				people_eaten = round(self.attack_power/city.defence_capability)
				city.population -= people_eaten
				print(f'{self.name} has ate {people_eaten}, {city.population} are left. {city.name} is preparing to attack {self.name}.')
				city.attack_or_defend(self)
class City():
	def __init__(self, name, population, attack_power, defence_capability):
		self.name = name
		self.population = population
		self.attack_power = attack_power
		self.defence_capability = defence_capability

	def __repr__(self):
		return f"This is the city {self.name}. It has a population of {self.population}, attack power of {self.attack_power}, and defence capability of {self.defence_capability}."

	def rebuild(self):
		self.population += 500

	def attack_or_defend(self, lizard):
		attack_or_defend_choice = input("Would you like to attack or defend?")
		while attack_or_defend_choice not in ['attack', 'defend']:
			attack_or_defend_choice = input("Please choose attack or defend")
		if attack_or_defend_choice == 'attack':
			self.attack_lizard(lizard)
		else:
			self.rebuild()
			lizard.attack_city(self)
	def attack_lizard(self, lizard):
		lizard.health -= self.attack_power
		if lizard.health <= 0:
			print(f'{lizard.name} has been defeated and its organs have been donated for medical research.')
		else:
			if lizard.health < 250:
				lizard.dying_roar()
			print(f'{self.name} has removed {self.attack_power} from {lizard.name}\'s health. {lizard.name} has {lizard.health} health remaining.') 
			print(f'{lizard.name} is preparing to attack {self.name}.')
			lizard.attack_city(self)