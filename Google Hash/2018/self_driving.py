
import time as timer


        

def join_routes(route):

    possible_routes = []
    route_start_x_cat = int(route[0][0] * divisions /rows)
    route_start_y_cat = int(route[0][1] * divisions /rows)
    route_end_x_cat = int(route[-1][0] * divisions /rows)
    route_end_y_cat = int(route[-1][1] * divisions /rows)
    old_valuation = evaluate(route)
    for i in range(max(route_end_x_cat - 1, 0), min(route_end_x_cat + 2, divisions)):
        for j in range(max(route_end_y_cat - 1, 0), min(route_end_y_cat + 2, divisions)):
            for k in range(len(rides_sorted[i][j])):
                new_route = route.copy()
                new_route.extend(rides_sorted[i][j][k])
                valuation = evaluate(new_route)
                if valuation[1] <= steps and valuation[0]:
                    if valuation[1] == old_valuation[1]:
                        utility = 1000
                    else:
                        utility = (valuation[2] - old_valuation[2]) / (valuation[1] - old_valuation[1])
                        possible_routes.append((new_route, utility, (i, j, k)))
    for i in range(max(route_start_x_cat - 1, 0), min(route_start_x_cat + 2, divisions)):
        for j in range(max(route_start_y_cat - 1, 0), min(route_start_y_cat + 2, divisions)):
            for k in range(len(rides_sorted[i][j])):
                new_route = rides_sorted[i][j][k].copy()
                new_route.extend(route)
                valuation = evaluate(new_route)
                if valuation[1] <= steps and valuation[0]:
                    if valuation[1] == old_valuation[1]:
                        utility = 1000
                    else:
                        utility = (valuation[2] - old_valuation[2]) / (valuation[1] - old_valuation[1])
                        possible_routes.append((new_route, utility, (i, j, k)))
    max_utility = 0
    best_route = []
    if possible_routes:
        index = None
        for pos in possible_routes:
            if pos[1] > max_utility:
                max_utility = pos[1]
                best_route = pos[0]
                index = pos[2]
        if index:
            route = best_route
            rides_sorted[index[0]][index[1]].pop(index[2])
            return route, True
        else:
            return route, False
    else:
        for i in range(0,divisions):
            for j in range(0,divisions):
                for k in range(len(rides_sorted[i][j])):
                    new_route = route.copy()
                    new_route.extend(rides_sorted[i][j][k])
                    valuation = evaluate(new_route)
                    if valuation[1] <= steps and valuation[0]:
                        if valuation[1] == old_valuation[1]:
                            utility = 1000
                        else:
                            utility = (valuation[2] - old_valuation[2]) / (valuation[1] - old_valuation[1])
                            possible_routes.append((new_route, utility, (i, j, k)))
        for i in range(0,divisions):
            for j in range(max(0,divisions)):
                for k in range(len(rides_sorted[i][j])):
                    new_route = rides_sorted[i][j][k].copy()
                    new_route.extend(route)
                    valuation = evaluate(new_route)
                    if valuation[1] <= steps and valuation[0]:
                        if valuation[1] == old_valuation[1]:
                            utility = 1000
                        else:
                            utility = (valuation[2] - old_valuation[2]) / (valuation[1] - old_valuation[1])
                            possible_routes.append((new_route, utility, (i, j, k)))
        if possible_routes:
            index = None
            for pos in possible_routes:
                if pos[1] > max_utility:
                    max_utility = pos[1]
                    best_route = pos[0]
                    index = pos[2]
            if index:
                route = best_route
                rides_sorted[index[0]][index[1]].pop(index[2])
                return route, True
            else:
                return route, False
        else:
            return route, False

def distance2(ride1, ride2):
    return abs(ride1[2] - ride2[0]) + abs(ride1[3] - ride2[1])
def distance1(ride):
    return abs(ride[0] - ride[2]) + abs(ride[1] - ride[3])

#def finish_time(route):
#    earliest_finish = max(abs(0 - route[0][0]) + abs(0 - route[0][1]), route[0][4])
#    earliest_finish += distance1(route[0])
#    if len(route) > 1:
#        for i in range(1, len(route)):
#            earliest_finish = max(distance2(route[i - 1], route[i]) + earliest_finish, route[i][4])
#            earliest_finish += distance1(route[i])
#    return earliest_finish

def evaluate(route):
    time = 0
    #start = timer.perf_counter()
    score = 0
    legal = True
    if route[0][4] > abs(route[0][0]) + abs(route[0][1]):
        score += bonus
        time += route[0][4]
    else:
        time += abs(route[0][0]) + abs(route[0][1])
    time += distance1(route[0])
    if time > route[0][5]:
        legal = False
    score += distance1(route[0])
    #end = timer.perf_counter()
    #print(end - start)
    if len(route) > 1:
        for i in range(1, len(route)):
            if route[i][4] > distance2(route[i - 1], route[i]) + time:
                time = route[i][4]
                score += bonus
            else:
                time += distance2(route[i - 1], route[i])
            score += distance1(route[i])
            time += distance1(route[i])
            if time > route[i][5]:
                legal = False
    return legal, time, score

def find_first_route():
    min_distance = 100000000
    min_starttime = 100000000
    chosen_route = None
    found = False
    for i in range(divisions):
        for j in range(divisions):
            for k in range(len(rides_sorted[i][j])):
                if abs(rides_sorted[i][j][k][0][0]) + abs(rides_sorted[i][j][k][0][1]) < min_distance and\
                        rides_sorted[i][j][k][0][4] <= abs(rides_sorted[i][j][k][0][0]) + abs(rides_sorted[i][j][k][0][1]) and\
                        evaluate(rides_sorted[i][j][k])[0]:
                    min_distance = abs(rides_sorted[i][j][k][0][0]) + abs(rides_sorted[i][j][k][0][1])
                    chosen_route = i, j, k
                    found = True
    if found == False:
        for i in range(divisions):
            for j in range(divisions):
                for k in range(len(rides_sorted[i][j])):
                    if rides[i][0][4] < min_starttime and evaluate(rides_sorted[i][j][k])[0]:
                        min_starttime = rides_sorted[i][j][k][0][4]
                        chosen_route = i, j, k
                        found = True
    return chosen_route




def solve(input_file, output_file):
    input = open(input_file, "r")
    data = input.readline().strip().split(" ")
    global rows
    rows = int(data[0])
    global columns
    columns = int(data[1])
    vehicles = int(data[2])
    global bonus
    bonus = int(data[4])
    global steps
    steps = int(data[5])
    global rides
    rides = []
    counter = 0
    data = input.readline().strip()
    while data != "":
        splitted = data.split(" ")
        for i in range(len(splitted)):
            splitted[i] = int(splitted[i])
        rides.append([])
        rides[-1].append(splitted)
        rides[-1][0].append(counter)
        data = input.readline().strip()
        counter += 1
    input.close()
    sort_rides()
    result = []
    solved = 0
    while len(result) < vehicles and rides:
        new_route = find_first_route()
        if not new_route:
            break
        result.append(rides_sorted[new_route[0]][new_route[1]][new_route[2]])
        rides_sorted[new_route[0]][new_route[1]].pop(new_route[2])
        can_optimize = True
        solved += 1
        rides_included = 1
        print("Routes found:", solved)
        while evaluate(result[-1])[1] < steps and can_optimize and rides:
            result[-1], can_optimize = join_routes(result[-1])
            rides_included += 1
            print("Rides incluseded:", rides_included)
        # check to see if we can join 2 rides without losing any score
        # Check to see if we can join an earlier ride
    final_score = 0
    for route in result:
        final_score += evaluate(route)[2]
    print("Final Score:", final_score)
#    output = open(output_file, "w")
#    for i in range(len(result)):
#        output.write(str(i))
#        for j in range(len(result[i])):
#            output.write(" " + str(result[i][j][6]))
#        output.write("\n")
    return final_score

def sort_rides():
    global rides_sorted
    global divisions
    divisions = int((rows / 500) + 1)
    rides_sorted = [[[] for i in range(divisions)] for j in range(divisions)]
    for ride in rides:
        rides_sorted[int(ride[0][0] / 500)][int(ride[0][1] / 500)].append(ride)

score = 0
#score += solve("a.in", r"C:\Users\John Nguyen\Desktop\Online Courses\coding\Google Hash\2018")
#print("Total Score:", score)
#score += solve("b.in", "C:/Users/Peleg/Downloads/self_driving.output")
#print("Total Score:", score)
score += solve("c.in", "C:/Users/Peleg/Downloads/self_driving.output")
print("Total Score:", score)
#score += solve("C:/Users/Peleg/Downloads/qualification_round_2018.in/d_metropolis.in", "C:/Users/Peleg/Downloads/self_driving.output")
#print("Total Score:", score)
#score += solve("C:/Users/Peleg/Downloads/qualification_round_2018.in/e_high_bonus.in", "C:/Users/Peleg/Downloads/self_driving.output")