def ft_count_harvest_recursive():
	i = 0
	day = int(input('Days until harvest: '))
	if i < day:
		return(print('Harvest time!'))
	else:
		ft_count_harvest_recursive(++i)
