
from faker import Faker
fake = Faker()
fake_it = Faker('it_IT')


name=[]
city=[]
occupation=[]
for i in range(200):
  job=fake.job()
  city_name=fake.city(country_code='it')
  Name=fake_it.first_name()
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
        element=element.replace(',', '')
        e.write('%s\n' % element)
    