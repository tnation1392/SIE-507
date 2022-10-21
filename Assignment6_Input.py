from collections import Counter

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

def lakecount(lakes): #A function to count the amount of times each lake shows up in the input list
    for x in lakes:
        final = []
        count = lakes.count(x)
        final.append(count)
    unique_count = Counter(lakes)
    return unique_count

#Creating the list of lake ID's via input
n = int(input("Enter number of IDs : "))
print("Enter Lake ID's")
lake_id = []
for i in range(0, n + 1): #A for loop to allow for multiple inputs
    if i != 0:
        id = int(input())
        lake_id.append(id)   # adding the value to lake_id

#Creating list of lake names via input
n2= int(input("Enter Number of Lakes: "))
print("Enter Associated Lake Names:")
lake_name = []
for i in range(0, n2): #A for loop to allow for multiple inputs
    name = input()
    lake_name.append(name) #Adding value to lake_name

#Creating list of fish weights taken from the lakes
n3 = int(input("Enter number of Fish Weights: "))
print("Enter Fish Weights:")
fish_weight = []
for i in range(0, n3):  # A for loop to allow for multiple inputs
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
print("Statistics of input:")
print("Total Number of Fish:", len(fish_weight))
print("Average Fish Weight:",avg_weight(fish_weight))
print("Heaviest Fish:", max(fish_weight))
print("Lightest Fish:", min(fish_weight))

#Printed Star Histogram
print('\n')
Grouped_count = lakecount(lake_name)
star_histogram(Grouped_count)
