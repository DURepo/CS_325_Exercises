'''
source https://algorithmsandme.com/category/algorithms/greedy-algorithm/

'''

from operator import itemgetter

def min_Lateness(assignments):

   
    sorted_assignments = sorted(assignments, key=itemgetter(2))

    max_lateness = 0
    start_time = 0
    schedule =[]


    for assignment in sorted_assignments:
        finish_time = start_time + assignment[1]

        if(finish_time > assignment[2]):
            max_lateness = max(max_lateness, (finish_time - assignment[2]))
        start_time = finish_time
        schedule.append(assignment[0])
    return max_lateness, schedule

assinnments = [("A",2,2),("B",3,4),("C",1,6),("D",5,7)] #[(S.no, timetaken, deadline)]
print(min_Lateness(assinnments))
