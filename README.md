# GUI for ATLAS 

## Overview
The main role of this code is to have a guided user interface for the Atlas which is a 3-D printer. The main objectives are:
- To input sensor configurations.
- Store the data in a folder for each build done by ATLAS.
- Once the printer starts to produce the object, display live data from the sensors.
#### The flowchart below is a summary of the structure of the program
![](Flowchart.jpg)

## Codes written
### 1) Main_page folder
- Views.py consists of the main structure of the program. It consists of functions which perform various operations along with rendering specific pages.
- Forms.py consists of the layout and data type of various settings for the ATLAS printer.
- Urls.py provides a URL for each page.
- The other files are not used/developed.
#### a) Views.py 
Views.py has 3 functions - 'home', 'submission' and 'fetch_sensor_values_ajax'
- 'home' function is for the first page where the user will input data into the form. It uses the POST method along with the forms in forms.py to use the input data and create a json file. Before the json file is created, the values are stored in a text file and from the text file the json file is created. The function also validates if  storage location is created or not. If it is not created then it will create a folder with the build name and store data there. If a folder already exists then it adds files to that folder. It renders the 'home.html' page.
- 'submission' function begins as soon as the user clicks submit on the first page. It renders the 'submissions.html' page while starting the functions - 'atlas_trial' and 'search' from the complete_trial.py code (will be explained in the Codes folder). These functions are run in the background.
- 'fetch_sensor_values_ajax' function will be used to display live data from the sensors. It is currently under development.

#### b) Forms.py
Forms.py consists of the layout and data structure required for various settings. Form 1 is used 

