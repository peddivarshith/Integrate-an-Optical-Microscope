# GSOC-caMicroscope
## Requirements
Python - 3.5.
- OpenCV - 
- Numpy -
- Flask - 
- Time -
- Json -
- Logging - 

JavaScript
## Steps to download the repository and setup the server
- Download the github repository using the command 
```bash 
git clone https://github.com/peddivarshith/GSOC-caMicroscope
```
- Go to the command line terminal and find the ip address of host using the following command
 **In windows**
```bash
ipconfig
```
 **In Linux/Raspbian OS**
```bash
ifconfig
```
- Open the cloned repository folder.
- Update the same ip address in static/javascript/script.js
- Run the server.py from repository folder using 
```bash
python3 server.py
```
from the repository folder.
## Steps to access the webservice (CLIENT)
- Open browser(chrome/firefox/edge) and enter the server ip address along with :5000/ (ip address with port number)

Example 
```bash
192.168.10.102:5000/
```
- Enter the x value, y value and select the zoom level from the drop down list. (Default lens available are 4x,10x,40x and 100x). The previous x,y and zoom values are displayed at the bottom of the page.
- Click on submit.
- The captured image of the slide will be displayed in the browser. 
- To go to another position, click on home button and re-enter the values.
```bash
Note: Minimum distance that the motors can move is 126 micro meters.
```
## Detailed explanation is given in the below video
[link](url)
