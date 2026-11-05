def can_see_stage(seats):
    for i in range(len(seats[0])):
        previous_seat = None
        for j in range(len(seats)-1,-1,-1):
            seat = seats[j][i]
            if previous_seat == None:
                previous_seat = seat
                continue
            if previous_seat <= seat:
                return(False)
            previous_seat = seat
    return(True)