def add_time(start, duration, weekday = False):

    weekday_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    c1 = start.split()
    a1 = duration.split(':')
    ampm = c1[1]
    if ampm != 'AM' and ampm != 'PM':
        return 'Error: start variable must have an AM or PM'
    c2 = c1[0].split(':')
    if int(a1[1]) >= 60 or int(c2[1]) >=60:
        return 'Error: Can not have more than 59 minutes'
    if int(c2[0]) > 12 or int(c2[0]) < 1:
        return 'Error: start time must be between 1 and 12'
    if a1[1][0] == '0':
        a1[1] = a1[1][1]

    if c2[1][0] == '0':
        c2[1] = c2[1][1]

    # check if minutes add up to more or equal to 60
    add_hour = 0
    minutes = int(a1[1]) + int(c2[1])
    if minutes >= 60:
        add_hour = 1
        minutes = minutes - 60
    
    minutes = str(minutes)
    if len(minutes) < 2:
        minutes = '0'+minutes
    
    hours = int(a1[0]) + int(c2[0]) + add_hour
    daycount = 0
    if hours >= 12:
        ampmcount = hours // 12
        if ampm == 'PM' and ampmcount%2==1:
            ampm = 'AM'
        elif ampm == 'AM' and ampmcount%2==1:
            ampm = 'PM'
        hours = (hours-ampmcount*12)%13
        if hours == 0:
            hours = 12      
        if c1[1] == 'AM':
            daycount = ampmcount//2
        if c1[1] == 'PM':
            daycount = 1 + (ampmcount-1)//2
    
    if weekday != False:
        current_day = weekday.lower()
        if current_day in weekday_list:
            future_day = weekday_list.index(current_day) + daycount
            future_day = future_day%7
            future_day = weekday_list[future_day]
        else:
            return 'Error: Wrong Weekday'


    new_time = str(hours) + ':' + str(minutes) + ' ' + ampm

    if weekday != False:
        new_time += ', ' + future_day.capitalize()
    
    if daycount == 1:
        new_time+= ' (next day)'
    elif daycount > 1:
        new_time += ' (' + str(daycount) + ' days later)' 
    return new_time