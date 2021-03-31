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
git clone https://github.com/peddivarshith/Integrate-an-Optical-Microscope.git
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
- Update the same ip address in static/javascript/script.js as well as in script1.js
![](link)
- Run the server.py from repository folder 
![](link)
or either run the following command in the Integrate-an-optical-microscope folder in command prompt
```bash
python3 server.py
```
## Steps to access the webservice (CLIENT)
- Then open browser(chrome/firefox/edge) and enter the server ip address along with :5000/ (ip address with port number)

Example 
```bash
192.168.10.102:5000/
```
![](link)
- Enter the x value, y value and select the zoom level from the drop down list. (Default lens available are 4x,10x,40x and 100x). The previous x,y and zoom values are displayed at the bottom of the page and submit the page.
![](link)
- On server side in the running console you can see the computed steps.
![](link)
- The captured image of the slide will be displayed in the browser(the image is captured with refernce to previous positions).
![](link)
- To go to another position, click on home button and re-enter the values(you can see at bottom that the previous values have changed to the present values).
![](link)
```bash
Note: Minimum distance that the motors can move is 126 micro meters.
```
## Detailed explanation is given in the below video
[link](url)
