from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .forms import S200Form, PicoForm, Storag_loc

import json, os, os.path, sys, subprocess, threading

from Codes.complete_trial import atlas_trial, read_file, search, runInParallel


def home(request):

	#form 
	if request.method == 'POST':
		form = S200Form(request.POST)
		form2 = PicoForm(request.POST)
		form3 = Storag_loc(request.POST)
		if form.is_valid() and form2.is_valid() and form3.is_valid():

			#clearing data
			Bit_Depth = form.cleaned_data['Bit_Depth']
			Resolution_horizontal = form.cleaned_data['Resolution_horizontal']
			Resolution_vertical = form.cleaned_data['Resolution_vertical']
			FPS = form.cleaned_data['FPS']
			Sampling_interval = form2.cleaned_data['Sampling_interval']
			Trigger_channel = form2.cleaned_data['Trigger_channel']
			Downsampling_ratio = form2.cleaned_data['Downsampling_ratio']
			location = form3.cleaned_data['location']
			Build_name = form3.cleaned_data['build_name']


			#forming directory and checking if it exists
			save_path = location
			build = Build_name
			path = os.path.join(save_path, build)
			if os.path.isdir(path) == False:
				os.mkdir(path)
			else:
				complete_name = os.path.join(path, 'values.txt')
				print(complete_name)


				#writing in text file
				f = open(complete_name,'a+')
				f.truncate(0)
				f.write('Bit_Depth ' + str(Bit_Depth))
				f.write('\n')
				f.write('Resolution_value_horizontal ' + str(Resolution_horizontal))
				f.write('\n')
				f.write('Resolution_value_vertical ' + str(Resolution_vertical))
				f.write('\n')
				f.write('FPS_value ' + str(FPS))
				f.write('\n')
				f.write('Sampling_interval ' + str(Sampling_interval))
				f.write('\n')
				f.write('Trigger_channel ' + str(Trigger_channel))
				f.write('\n')
				f.write('Downsampling_ratio ' + str(Downsampling_ratio))
				f.write('\n')
				f.write('Saving_location ' + str(location))
				f.close()  


				#to sort strings to particular dictionaries and form json file
				filename = complete_name 
				line1 = [0,1,2,3]
				line2 = [4,5,6]
				dict1 = {}
				dict2 = {}
				name = str(path) + r'\Values2.json'
				print(name)



				#Converting to a json file
				i = 0
				with open(filename) as fh:
					for line in fh:
						if i in line1:
							command,description = line.strip().split(None,1)
							dict1[command] = description.strip()
						elif i in line2:
							command,description = line.strip().split(None,1)
							dict2[command] = description.strip()
						i = i+1
				output = open(name,'w')
				json.dump({'Cam':dict1,'Pico':dict2}, output, indent = 4, sort_keys = False)
				output.close()
				os.startfile(name)
				return HttpResponseRedirect('/submission/')

    #completing the form process and rendering the specific page
	form = S200Form()
	form2 = PicoForm()
	form3 = Storag_loc()
	return render(request, 'home.html', {'form': form, 'form2':form2, 'form3':form3})

	
def submission(request):
	t = threading.Thread(target = runInParallel, name = 'Parallel', args = (atlas_trial, search))
	t.start()
	return render(request, "graph.html")

def fetch_sensor_values_ajax(request):
	data={}
	if request.is_ajax():
		sensor_data=[]
		now=datetime.now()
		ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
	try:

	    # sr=serial.Serial("COM9",9600)
		#sr=serial.Serial(com_port,9600)
		#st=list(str(sr.readline(),'utf-8'))
		#sr.close()
		sensor_val=str(''.join(st[:]))
		if(sensor_val):
			sensor_data.append(str(sensor_val)+','+ok_date)
		else:
			sensor_data.append(str(sensor_val)+','+ok_date)
	except Exception as e:

		sensor_data.append(str(sensor_val)+','+ok_date)
		data['result']=sensor_data
	else:
		data['result']='Not Ajax'
	return JsonResponse(data)



