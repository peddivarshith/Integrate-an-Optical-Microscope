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

</br>
**script1.js**
</br>
![](tutorial/step1_1.png)

**script.js**
![](tutorial/step1_2.png)
- Run the **server.py** from repository folder 
![](tutorial/step2.png)
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
![](tutorial/step3.png)
- Enter the x value, y value and select the zoom level from the drop down list. (Default lens available are 4x,10x,40x and 100x). The previous x,y and zoom values are displayed at the bottom of the page and submit the page.
![](tutorial/step4.png)
- On server side in the running console you can see the computed steps.
![](tutorial/step5.png)
- The captured image of the slide will be displayed in the browser(the image is captured with refernce to previous positions).
![](tutorial/step6.png)
- To go to another position, click on home button and re-enter the values(you can see at bottom that the previous values have changed to the present values).
![](tutorial/step7.png)
```bash
Note: Minimum distance that the motors can move is 126 micro meters.
```
## Detailed explanation is given in the below video
[link](url)
