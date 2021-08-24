import time, os, random
from time import sleep
from multiprocessing import Process

#code to create text files
def atlas_trial():
    print('starting to create file')
    for i in range(3):
        path = (r'C:\Users\Aditya Titus\Desktop\Django\Project 2021')
        name = 'No' + str(i) + '.txt'
        complete_name = os.path.join(path, name)
        print('Creating file = ' + str(complete_name))
        f = open(complete_name,'a+')
        for j in range(5):
            number = random.randrange(15)
            f.write(str(number))
            f.write('\n')
        f.close()
        sleep(5)
    print('files created')


#running the creating text files code
file_values = []

#function to read file and add values
def read_file(file_path):
    j = 0
    f = open(file_path, 'r')
    lines = f.readlines()
    for i in lines:
        j = j + int(i)
    return j

def search():
    path = (r'C:\Users\Aditya Titus\Desktop\Django\Project 2021')
    i = 0
    count = 0
    while count < 4:
            name = ('No' + str(i) + '.txt')
            search = os.path.join(path, name)
            if os.path.exists(search):
                count = 0
                print('loading file = ' + name)
                k = read_file(search)
                file_values.append(k)
                i += 1
                sleep(5)                
            else:
                count += 1
                sleep(5)
                print('waiting')  
             
    print('The values are = ' + str(file_values))
    return(file_values)
                            

if __name__ == '__main__':
    p1 = Process(target = atlas_trial)
    p1.start()
    p2 = Process(target = search)
    p2.start()
    p1.join()
    p2.join()


def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()






