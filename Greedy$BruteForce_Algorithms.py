###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(items,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    items_copy = items.copy()
    items_taken = []
    items_final = []
    items_deleted = items.copy()
    #sort the items dictionary by its keys
    sorted_items = {}
    sorted_keys = sorted(items, key = items.get, reverse = True)
    for w in sorted_keys:
        sorted_items[w] = items_copy[w]
    #iterate on keys and append the ones which fulfill criteria <maxWeight
    total_weight = 0
    
    while items_deleted != {}:
        for i in sorted_items:
            total_weight += sorted_items[i] 
            if total_weight <= limit:
                items_taken.append(i)
                sorted_items[i] = 2*limit
                del(items_deleted[i])
    
            else:
                total_weight -= sorted_items[i] 
        items_final.append(items_taken)
        items_taken = []
        total_weight = 0
    
    
    return  items_final


# Problem 2
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    total_weight = 0
    cows_taken = []
    power_set = []
    for item in (get_partitions(cows)): 
        power_set.append(item)
    flag = False
    counter = 0

    for i in range(1, len(cows)+1):
        for theSet in power_set:
            counter = 0
            if flag:
                cows_taken = []
            if len(theSet) == i:
                for cow_trip in theSet:                        #TAKE AS EXAMPLE FOR FLOW CONTROL: IF ELIF
                    counter += 1
                    for cow in cow_trip:
                        total_weight += cows[cow]
                    if total_weight <= limit:
                        cows_taken.append(cow_trip)
                        total_weight = 0
                        flag = True
                    if len(cows_taken) == i:
                        return cows_taken
                    elif counter == len(theSet):
                        total_weight = 0
                        cows_taken = []
                        flag = False
   

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    
    #count time
    start = time.time()
    cows_by_greedy = greedy_cow_transport(cows, limit)
    end = time.time()
    print("Time needed to execute the greedy algorithm: " + str(end - start))
    
    counter_greedy = 0
    counter_brute = 0
    for trip in cows_by_greedy:
        counter_greedy += 1     
    print("Greedy algorithm: " + str(cows_by_greedy)+ "\n number of trips: " + str(counter_greedy))
     
    
    
    
    
    start = time.time()
    cows_by_brute = brute_force_cow_transport(cows, limit)
    end = time.time()
    print("Time needed to execute the brute force algorithm: " + str(end - start))
    
    for trip in cows_by_brute:
        counter_brute += 1     
    print("Brute force algorithm: " + str(cows_by_greedy)+ "\n number of trips: " + str(counter_greedy))
    
    
    
    

    

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

print(compare_cow_transport_algorithms())


# cows = load_cows("ps1_cow_data.txt")
# limit=10
# print(cows)
# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

# cows_testing ={"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
# print(brute_force_cow_transport({'Horns': 25, 'Milkshake': 40, 'Miss Bella': 25, 'Lotus': 40, 'Boo': 20, 'MooMoo': 50}, 100))
# print(brute_force_cow_transport({'Daisy': 50, 'Buttercup': 72, 'Betsy': 65}, 75))

# print(brute_force_cow_transport(cows_testing, limit))


