def ft_water_reminder():
    d = int(input('Days since last watering: '))
    if d > 2:
        print('Water the plants!')
    else:
        print('Plants are fine')
