def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == 'packets':
		print(f'{str.capitalize(seed_type)} seeds: {quantity} packets available')
	elif unit == 'grams':
		print(f'{str.capitalize(seed_type)} seeds: {quantity} grams total')
	elif unit == 'area':
		print(f'{str.capitalize(seed_type)} seeds: covers {quantity} square meters')
	else:
		print('Unknown unit type')