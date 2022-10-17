#Todd Nason Assignment 6
#Program to display random samples of fish weights from Maine lakes

sample_lake = ("Chemo", "Greene", "Hopkins","Chemo", "Toddy", "Greene", "Hopkins", "Greene")
    #A dictionary containing the pond ID's and their associated names

sample_fish_lake = [1000, 1010, 1050, 1000, 1100, 1010, 1050, 1010] # a list of the given sample pond ID's
sample_fish_lb = [4.0, 2.0, 1.5, 2.0, 2.2, 1.9, 2.8, 3.5] # a list of the given sample fish weights
avg_weight = f'{sum(sample_fish_lb)/len(sample_fish_lb):.1f}'

#Function to translate the lake ID's in a list to the name
def id_to_name(lake_group):
    lake_name = []
    for i in lake_group:
        if i == 1000:
            translated_id = "Chemo"
            lake_name = lake_name.append(translated_id)
        if i == 1010:
            translated_id = "Greene"
            lake_name = lake_name.append(translated_id)
        if i == 1050:
            translated_id = "Hopkins"
            lake_name = lake_name.append(translated_id)
        if i == 1100:
            translated_id = "Toddy"
            lake_name = lake_name.append(translated_id)
    print(lake_name)

#Histogram Function
def star_histogram(items):
    if items > 0:
        return('*'*items)
    print(star_histogram())

#Neat table of ponds and associated ID's
print(f'{"Lake ID":^10} {"Lake Name":^10} {"Fish Weight:":^8}')
print('-' * 35)
for i in range(len(sample_fish_lake)):
    print(f'{sample_fish_lake[i]:^8} {"|"} {sample_lake[i]:^8} {"|"} {sample_fish_lb[i]:^6}')

#Statistics
print("\n")
print("Total # of Fish:",len(sample_fish_lb))
print("Average Weight of Fish:",avg_weight)
print("Heaviest Fish:", max(sample_fish_lb))
print("Lightest Fish:", min(sample_fish_lb))

#Printed Star Histogram
print('\n')
Chemo_c = sample_lake.count("Chemo")
Greene_c = sample_lake.count("Greene")
Hopkins_c = sample_lake.count("Hopkins")
Toddy_c = sample_lake.count("Toddy")

Star_C = (star_histogram(Chemo_c))
Star_G = (star_histogram(Greene_c))
Star_H = (star_histogram(Hopkins_c))
Star_T = (star_histogram(Toddy_c))

print(f'{"Lake":^10} {"Fish Count":^10}')
print('-' * 23)
print(f'{"Chemo":^8} {"|"} {Star_C:^6}')
print(f'{"Greene":^8} {"|"} {Star_G:^8}')
print(f'{"Hopkins":^8} {"|"} {Star_H:^6}')
print(f'{"Toddy":^8} {"|"} {Star_T:^6}')
