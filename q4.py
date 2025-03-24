import os
import json

# Check if the file "data.json" exists.
if os.path.isfile("data.json"):
    # If it does, read "data.json" into the variable `data`
    data = {}
    my_file = open("data.json","r").read()
    for character in '{}"':
        my_file = my_file.replace(character,'')

    for line in my_file.split(','):
        pair = line.split(':')
        if len(pair) == 2:
            data[pair[0]]=pair[1]

   
    #### YOUR CODE HERE 
    ####

else:
    # If it doesn't, make an empty dictionary called data
    data = {}

# Get a new recommendation for a new user
name = input("What is your name? ")
recommendation = input("What book/movie/podcast/etc. would you recommend? ")

# Add the new user and recommendation to the `data` dictionary
data[name] = recommendation

# Write the `data` variable to the file "data.json"
my_file = open("data.json","w")
first = True
my_file.write('{')
for key in data.keys():  
    if first:
        my_file.writelines(f'"{key}":"{data[key]}"')
        first = False
    else:
        my_file.writelines(f',"{key}":"{data[key]}"')
my_file.writelines('}')

####
#### YOUR CODE HERE 
####

