
from faker import Faker
fake = Faker()


name=[]
city=[]
occupation=[]
for i in range(5000):
  job=fake.job()
  city_name=fake.address()
  Name=fake.firstname()
  name.append(Name)
  city.append(city_name)
  occupation.append(job)



with open('data/names.txt', 'w+') as f:
 
   #looping over the each ist element
 
    for element in name:
 
         #writing to file line by line
 
        f.write('%s\n' % element)

with open('data/occupation.txt', 'w+') as e:
 
   #looping over the each ist element
 
    for element in occupation:
 
         #writing to file line by line
 
        e.write('%s\n' % element)