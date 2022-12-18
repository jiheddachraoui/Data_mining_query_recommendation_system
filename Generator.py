import random
import csv
import time

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


min=18
max=60
nbr_users=2000
data_size=2000
nbr_queries=2000

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

