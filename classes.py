from functions import *

class Lizard():
	def __init__(self, name, attack_power, belly_size,  health, revive_power, is_hungry = True, has_let_out_dying_roar = False, times_revived = 0):
		self.name = name
		self.attack_power = attack_power
		self.belly_size = belly_size
		self.health = health
		self.is_hungry = is_hungry
		self.has_let_out_dying_roar = has_let_out_dying_roar
		self.times_revived = times_revived
		self.revive_power = revive_power

	def __repr__(self):
		return f'{self.name}! They have {self.attack_power} attack power, {self.belly_size} belly size, {self.health} health, and revive power of {self.revive_power}.\n'

	def dying_roar(self):
		print(f'\"ROARRR!!!\", {self.name} has less than 250 health remaining.\n')

	def revive(self):
		self.health += self.revive_power
		print(f'{self.name} has revived {self.revive_power} health so that its health is {self.health}.\n')

	def attack_city(self, city):
		if not self.is_hungry:
			print(f"{self.name} is not hungry. {city.name} is safe.\n") 
		else:
			self.belly_size -= self.attack_power/city.defence_capability
			if self.belly_size < 0 or city.health <= 0:
				print(f"{self.name} has defeated {city.name}.\n") 
			else:
				people_eaten = round(self.attack_power/city.defence_capability)
				city.health -= people_eaten
				print(f'{self.name} has ate {people_eaten}, {city.health} are left. {city.name} is preparing to attack {self.name}.\n')
				
class City():
	def __init__(self, name, health, attack_power, defence_capability, revive_power):
		self.name = name
		self.health = health
		self.attack_power = attack_power
		self.defence_capability = defence_capability
		self.revive_power = revive_power

	def __repr__(self):
		return f"{self.name}! It has a health of {self.health}, attack power of {self.attack_power}, defence capability of {self.defence_capability}, and revive power of {self.revive_power}\n"

	def rebuild(self):
		self.health += self.revive_power
		print(f'{self.name} has rebuilt {self.revive_power} health so that its health is {self.health}.\n')

	def attack_or_defend(self, lizard):
		attack_or_defend_choice = input("Would you like to attack or defend?\n")
		while attack_or_defend_choice not in ['attack', 'defend']:
			attack_or_defend_choice = input("Please choose attack or defend\n")
		if attack_or_defend_choice == 'attack':
			self.attack_lizard(lizard)
		else:
			self.rebuild()
			lizard.attack_city(self)
	def attack_lizard(self, lizard):
		lizard.health -= self.attack_power
		if lizard.health <= 0:
			print(f'{lizard.name} has been defeated and its organs have been donated for medical research.\n')
		else:
			if lizard.health < 250:
				lizard.dying_roar()
			print(f'{self.name} has removed {self.attack_power} from {lizard.name}\'s health. {lizard.name} has {lizard.health} health remaining.\n') 
			print(f'{lizard.name} is preparing to attack {self.name}.\n')
			



