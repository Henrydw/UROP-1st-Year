# GUI for ATLAS 

## Overview
The main role of this code is to have a guided user interface for the Atlas which is a 3-D printer. The main objectives are:
- To input sensor configurations
- Store the data in a folder for each build done by ATLAS
- Once the printer starts to produce the object, display live data from the sensors
#### The flowchart below is a summary of the structure of the program
![](Flowchart.jpg)

## Codes written
### 1) Main_page folder
- Views.py consists of the main structure of the program. It consists of functions which perform various operations along with rendering specific pages.
- forms.py consists of the layout and data type of various settings for the ATLAS printer
- urls.py provides a URL for each page
#### a) Views.py 
This function is for the main page. It uses the form layout in 'forms.py
