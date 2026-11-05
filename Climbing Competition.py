def climb(stamina, obstacles):
    #calculate the difference between obstacles and convert into respective types
    obstacles_Difference = [float(f"{(obstacles[x+1]-obstacles[x]):.2f}") 
                            if int(float(f"{(obstacles[x+1]-obstacles[x]):.2f}")) != float 
                            (f"{(obstacles[x+1]-obstacles[x]):.2f}") 
                            else int(float(f"{(obstacles[x+1]-obstacles[x]):.2f}")) 
                            for x in range(len(obstacles)-1)]
    #convert floats: ceiling for positive floats, floor for negative floats
    stamina_Difference = []
    for x in obstacles_Difference:
        if int(x) != x:
            if x < 0: stamina_Difference.append(int(str(x)[0:len(f"{x:.0f}")])-1)
            else: stamina_Difference.append(int(str(x)[0:len(f"{x:.0f}")])+1) 
        else: stamina_Difference.append(int(x))
    #convert the already named stamina difference into the actually stamina difference (change the name later for clarity or smth)
    stamina_Difference = [x*2 if x > 0 else x*-1 for x in stamina_Difference]
    #calculate how many obstacles the stamina given can pass before it is at 0 or the next obstacle will make it below 0
    passed = 0
    for x in stamina_Difference:
        stamina = stamina - x
        if stamina < 0:
            return(passed)
        elif stamina == 0:
            return(passed+1)
        else:
            passed += 1
    return(passed)
print(climb(10, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]))