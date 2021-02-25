def activity_selection(activities, start_times,end_times):
    result = []
    blocked_time = 0
    count = len(activities)
    for i in range(count):
        if(start_times[i] >= blocked_time):
            result.append(activities[i])
            blocked_time = end_times[i]

    return result

result=activity_selection(["Play Golf", "Paint", "Cook", "Sleep", "Jog", "Code", "Eat"],  [1, 3, 1, 3, 4, 6, 8], [3, 4, 4, 6, 6, 9, 9])
print(result)
