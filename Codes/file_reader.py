import os, time
from time import sleep


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

path = (r'C:\Users\Aditya Titus\Desktop\Django\Project 2021')
i = 0
done = False
while done == False:
	k = 0
	count = 0
	name = 'No' + str(i) + '.txt'
	search = os.path.join(path, name)
	if os.path.exists(search):
		print('loading file = ' + name)
		k = read_file(search)
		file_values.append(k)
		i = i+1
	else:
		sleep(5)
		count += 1
		if count > 4:
			print('no more files')
			done = True


print(file_values)




#code to read each file in the directory
# path = (r'C:\Users\Aditya Titus\Desktop\Django\Project 2021')
# os.chdir(path)
# k = 0
# timer = False
# while timer == False:
# 	for file in os.listdir():
# 	    if file.endswith('.txt'):
# 	        file_path = f'{path}\{file}'
# 	        j = read_file(file_path)
# 	        file_values.append(j)
# 	        print(j)
# 	    else:
# 	        sleep(5)
# 	        k += 1
# 	        if k == 5:
# 	            print('No more files')
# 	            timer = True
# 	        