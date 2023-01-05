import random
import pandas as pd
import numpy as np

def list(file):
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
names = list(file)

file = "data/cities.txt"
cities = list(file)

file = "data/occupation.txt"
jobs = list(file)


min=19
max=65
nbr_users=2000
data_size=2000
nbr_queries=2000

def random_profile():
    age = random.randint(min, max)
    # randomly choose a profile
    item = [random.choice(names),age,random.choice(jobs), random.choice(cities)]
    return item

data=[]


for i in range(data_size):
  data.append(random_profile())




datadf=pd.DataFrame(data,columns=["name", "age","occupation","address"])
datadf.to_csv('./csv/dataset.csv',index=False)

print("Dataset created ")

##########################
users = []
for i in range(nbr_users):
		user = "U" + str(i+1)
		users.append(user)

usersdf=pd.DataFrame(users,columns=['Used_Id'])
usersdf.to_csv("./csv/users.csv",index=False)

print("Users set created ")

####################################################################################
queries=[]
d=0
while d < nbr_queries:
    
    queryID = "Q" + str(d + 1)
    query = ''
    
    if random.randint(0, 1) == 1:#try to pick name for query
      if len(query)>0: query+=','
      query+=('name=' + random.choice(names))
    if random.randint(0, 1) == 1:
      if len(query)>0: query+=','
      query+=('city=' + random.choice(cities))
    if random.randint(0, 1) == 1:
      if len(query)>0: query+=','
      query+=('age=' + str(random.randint(19, 65)))
    if random.randint(0, 1) == 1:
      if len(query)>0: query+=','
      query+=('job=' + random.choice(jobs))
    
    if len(query)>0:
      queries.append({"queryID":queryID,"query":query})
      d+=1

queries=pd.DataFrame(queries, columns =['queryID','query'])
queries.to_csv('./csv/queries.csv',index=False)

print("Queries set created ")

######################################################################################



MIN_VOTE, MAX_VOTE = 1, 100
queries=pd.read_csv("./csv/queries.csv",index_col=False)
queriesIDs=queries['queryID'].values.tolist()
users = pd.read_csv("./csv/users.csv",index_col=False)
users=users['Used_Id'].values.tolist()
randomScores = np.random.randint(low=MIN_VOTE, high=MAX_VOTE, size=( len(users), len(queriesIDs))).astype(str)
mask = np.random.randint(0, 3, size=randomScores.shape).astype(bool)
randomScores[np.logical_not(mask)] = ""
randomScoresdf=pd.DataFrame(randomScores,columns=queriesIDs,index=users)
randomScoresdf.to_csv("./csv/utility_matrix.csv")
print("Partial utility matrix created and saved in /csv/utility_matrix.csv")
