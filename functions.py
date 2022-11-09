from copy import deepcopy

def battle_is_over(lizard, city):
	if lizard.health <= 0 or not lizard.is_hungry:
		return True
	else:
		return False

def evaluate_playing_field(city, lizard):
  if city.health <= 0:
    return -1
  elif lizard.health <= 0:
    return 1
  else:
    return 0

def minimax(city, lizard, is_maximising):
	if city.health <= 0 or lizard.health <= 0:
		return [evaluate_playing_field(city, lizard), ""]
	if is_maximising:
		best_value = -float("Inf")
		for move in ['attack', 'revive']:
    		new_city = deepcopy(city)
    		new_lizard = deepcopy(lizard)
    		if move == 'attack':
    			new_lizard.health -= new_city.attack_power
    			hypothetical_value = minimax(new_city, new_lizard, not is_maximising)[0]
    			if hypothetical_value > best_value:
      				best_value = hypothetical_value
      				best_move = move
      		if move == 'revive':
      			new_city.health += new_city.revive_power
      			hypothetical_value = minimax(new_city, new_lizard, not is_maximising)[0]
      			if hypothetical_value > best_value:
      				best_value = hypothetical_value
      				best_move = move
    if not is_maximising:
      	best_value = float("Inf")

      	for move in ['attack', 'revive']:
    		new_city = deepcopy(city)
    		new_lizard = deepcopy(lizard)
    		if move == 'attack':
    			new_city.health -= round(self.attack_power/city.defence_capability)
    			hypothetical_value = minimax(new_city, new_lizard, not is_maximising)[0]
    			if hypothetical_value < best_value:
      				best_value = hypothetical_value
      				best_move = move
      		if move == 'revive':
      			new_lizard.health += new_lizard.revive_power
      			hypothetical_value = minimax(new_city, new_lizard, not is_maximising)[0]
      			if hypothetical_value < best_value:
      				best_value = hypothetical_value
      				best_move = move


	return [best_value, best_move]

