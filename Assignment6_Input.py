#Todd Nason
#A program to take input data about fish and formulate statistics and create a star histogram
from collections import Counter

# A function to calculate the average of a set of integers or floats
def avg_weight(x):
    avg = f'{(sum(x)/len(x)):.2f}'
    return avg

def star_histogram(lakes): #A function to create a star histogram
    print(f'{"Lake":^10} {"Fish Count":^10}')
    print('-' * 23)
    for key in lakes:
        if lakes[key] != "":
            print(f'{key:^10} {"|"} {int(lakes[key])* "*":^6}')
        else:
            print(f'{key:^8} {"|"} {" "}')

#A function to count the amount of times each lake shows up in the input list
def lakecount(lakes):
    for x in lakes:
        final = []
        count = lakes.count(x)
        final.append(count)
    unique_count = Counter(lakes)
    return unique_count

#Creating the list of lake ID's via input
n = int(input("Enter number of IDs : "))
print("Enter Lake ID's")
lake_id = []  #an empty list for the lake ids
for i in range(0, n + 1):  # A for loop to allow for multiple inputs
    try:
        if i != 0:
            id = int(input())
            lake_id.append(id)  # adding the value to lake_id
    except ValueError:
        print("Invalid input, please re-enter")
        id = int(input())
        lake_id.append(id)

#Creating list of lake names via input
n2= int(input("Enter Number of Lakes: "))
print("Enter Associated Lake Names:")
lake_name = []  #An empty list for lake_names to be appended into
for i in range(0, n2):  #A for loop to allow for multiple inputs
    try:
        name = input()
        if name.isalpha() is True:
            lake_name.append(name)
        else:
            print("Invalid input, please re-enter")
            id = input()
            lake_name.append(id)
    except ValueError:
        print("Invalid input, please re-enter")
        id = int(input())
        lake_name.append(id) #Adding value to lake_name

#Creating list of fish weights taken from the lakes
n3 = int(input("Enter number of Fish Weights: "))
print("Enter Fish Weights:")
fish_weight = []  #An empty list for fish weights to be appended into
for i in range(0, n3):  # A for loop to allow for multiple inputs
    try:
        lbs = float(input())
        fish_weight.append(lbs)  # Adding value to lake_name
    except ValueError:
        print("Invalid input, please re-enter")
        lbs = float(input())
        fish_weight.append(lbs)  # Adding value to lake_name

print('\n')

#Printing all associated input lists
print('Entered Lake IDs:', lake_id)
print("Entered Lake Names:", lake_name)
print("Entered Fish Weights:", fish_weight)
print('\n')

#Printing the neat table of the inputs
print(f'{"Lake ID":^10} {"Lake Name":^12} {"Fish Weight":^8}')
print('-' * 30)
for i in range(len(lake_id)):
    print(f'{lake_id[i]:^8} {"|"} {lake_name[i]:^8} {"|"} {fish_weight[i]:^6}')
print('\n')

#Statistics of the fish

fish_num = len(fish_weight) # The number of fishes entered
avg_list = avg_weight(fish_weight)  #The average weight from the inputs
max_fish = max(fish_weight)  #The maximum weight from the inputs
min_fish = min(fish_weight)  #The minimum weight from the inputs

print("Statistics of Input:")
print("Total Number of Fish:", fish_num)
print("Average Fish Weight:", avg_list)
print("Heaviest Fish:", max_fish)
print("Lightest Fish:", min_fish)

#Printed Star Histogram
print('\n')
Grouped_count = lakecount(lake_name) #Using the Grouped_count function to get a count of the times a lakes name is entered
star_histogram(Grouped_count) #Using the star_histogram function to create the star pattern histogram from the grouped_count results
