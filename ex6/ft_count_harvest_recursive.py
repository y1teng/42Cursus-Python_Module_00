def ft_count_harvest_recursive_core(day: int, i: int = 1) -> None:
    if i <= day:
        print(f'Day {i}')
        ft_count_harvest_recursive_core(day, i + 1)
    else:
        print('Harvest time!')


def ft_count_harvest_recursive():
    day = int(input('Days until harvest: '))
    ft_count_harvest_recursive_core(day)
