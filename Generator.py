import random
import csv
import time
import pandas as pd
import numpy as np

def to_csv(filename, data,header=None):
  with open("./csv/" + filename + ".csv", 'w+', newline='') as file:
    writer = csv.writer(file)

    if header is not None:
      writer.writerow(header)

    writer.writerows(data)


random.seed(time.time())
def name_array(file):
    # open file with names
    with open(file) as fp:
        new_list = []
        # loop through each line in the txt file 
        for line in fp:
            
            new_list.append(line.strip())
    return new_list

# call the function three times to transform names from each
# file into arrays 
file = "data/names.txt"
names = name_array(file)

file = "data/adresses.txt"
adresses = name_array(file)

file = "data/occupation.txt"
occupations = name_array(file)


min=15
max=60
nbr_users=3000
data_size=3000
nbr_queries=3000

def random_profile(i):
    age = random.randint(min, max)
    # randomly choose a profile
    item = [i+1,random.choice(names),age,random.choice(occupations), random.choice(adresses)]
    return item

data=[]


for i in range(data_size):
  data.append(random_profile(i))

data

to_csv("dataset",data,["id", "name", "age" , "occupation","address"])
print("Dataset created ")

##########################
data = []
for i in range(nbr_users):
		user = "U" + str(i+1)
		data.append(user)

with open("./csv/users.csv", "w+") as file:
		for user in data:
			file.write("%s\n" % user)

print("Users set created ")

####################################################################################



dataset= pd.read_csv("csv\dataset.csv")
D=[]
while len(D) < nbr_queries:
    
    queryID = "Q" + str(len(D) + 1)

    randomName, randomAddress, randomAge, randomOccupation = None, None, None, None #attributes that haven't been picked yet
    query = []
    age = str(random.randint(min, max))
    
    if random.randint(0, 1) == 1:#try to pick name for query
      randomName='name=="' + random.choice(names)+ '"'
      query.append('name=="' + random.choice(names)+ '"')
    if random.randint(0, 1) == 1:
      randomAddress='address=="' + random.choice(adresses)+ '"'
      query.append('address=="' + random.choice(adresses)+ '"')
    if random.randint(0, 1) == 1:  
      randomAge='age=="' + random.choice(age)+ '"'
      query.append('age=="' + random.choice(age)+ '"')
      
    if random.randint(0, 1) == 1:
      randomOccupation='occupation=="' + random.choice(occupations)+ '"'
      query.append('occupation=="' + random.choice(occupations)+ '"')
    
    item= [queryID,randomName,randomAge,randomOccupation,randomAddress]
        #query = [queryID,"name="+random.choice(names),"age="+age,"occupation="+random.choice(occupations), "address="+random.choice(adresses)]
    #print(query)
    if (randomName == None and randomAddress == None and randomAge == None and randomOccupation == None):
      continue
    else:
      D.append(item)
to_csv("queries", D)

print("Queries set created ")

######################################################################################


MIN_VOTE, MAX_VOTE = 1, 100
def parse_queries(path: str):
    # Initialize empty lists to store data and indexes
    data = []
    indexes = ["User/Query"]

    # Open the file and read each row
    with open(path) as f:
        for row in f:
            # Strip newline character and split row into values
            values = row.rstrip('\n').split(',')
            # Append first value to indexes list
            indexes.append(values[0])
            # Append remaining values to data list
            
            data.append(values[1:])
    
    # Convert data list to NumPy array and transpose
    data = np.array(data).T
    
    # Create a DataFrame from the transposed array using allowed_features as column names
    df = pd.DataFrame(data)
    #print(data.shape)
    # Return the DataFrame and the indexes list
    return df, indexes

print("Generating partial utility matrix...")
users = pd.read_csv("./csv/users.csv",header=None)

queries, queriesIDs = parse_queries("./csv/queries.csv")
#print(queries, queriesIDs)
randomScores = np.random.randint(low=MIN_VOTE, high=MAX_VOTE, size=( len(users), len(queriesIDs))).astype('O')

print("random scores generated")
mask = np.random.randint(0, 4, size=randomScores.shape).astype(bool)
print("mask generated")
randomScores[np.logical_not(mask)] = ""

print("mask applied")
randomScores = np.concatenate((users, randomScores), axis=1)
print(randomScores)
to_csv("utility_matrix", randomScores, queriesIDs)
print("Partial utility matrix created and saved in /csv/utility_matrix.csv")