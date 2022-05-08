def battle_is_over(lizard, city):
	if lizard.health <= 0 or not lizard.is_hungry:
		return True
	else:
		return False
