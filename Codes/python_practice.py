import random, time
from time import sleep
def loop():
    t0 = time.monotonic()
    number = random.randrange(30)
    t0 += 1
    time.sleep(t0 - time.monotonic())
    return(number)


if __name__ == '__main__':
    num = loop(5)
    print(num)


file_values = []
    finish = True 
    i = 0
    while finish == True:
        SUM = 0
        path = (r'C:\Users\Aditya Titus\Desktop\Django\Project 2021')
        name = ('No' + str(i) + '.txt')
        complete_name = os.path.join(path, name)
        j = 0
        while os.path.isdir(complete_name) == False:
            sleep(5)
            j = j + 1
            if j == 10:
                print('No more values')
                finish = False
            else:
                f = open(complete_name, 'r')
                lines = f.readlines()
                for line in lines:
                    SUM = SUM + int(line)
                    file_values.append(SUM)
                    args = {'results' : file_values}

