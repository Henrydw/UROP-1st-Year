import time, os, random
from time import sleep

#code to create text files
#def atlas_trial():

print('Build starting')
for i in range(3):
    path = (r'C:\Users\Aditya Titus\Desktop\Django\Project 2021')
    name = 'No' + str(i) + '.txt'
    complete_name = os.path.join(path, name)
    print('Making file = ' + name)
    f = open(complete_name,'a+')
    for j in range(5):
        number = random.randrange(15)
        f.write(str(number))
        f.write('\n')
    f.close()
    sleep(10)

print('Done with build')

