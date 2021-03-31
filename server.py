from flask import Flask, render_template,request
import json
import logging
from Motor3D import hardware_action
import os
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    #now we will create and configure logger
    logging.basicConfig(filename="./static/std.log",format='%(asctime)s %(message)s',filemode='a')
    
    #opening json file		
    f=open("data.json","r")
    #Converting into json object
    f=json.load(f)
    #rendering index page
    return render_template('index.html', x_key=f["x"],y_key=f["y"],z_key=f["z"])




@app.route('/success/')
def success(value):
    
    #rendering caimage page
    return render_template('caimage.html',the_title='Captured Image',the_value=value)

@app.route('/test',methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':
        #taking present values from request form
      x_value = request.form['x_value']
      y_value = request.form['y_value']
      z_value = request.form['z_value']
      
      print(x_value)
      print(y_value)
      print(z_value)
      delete_image()
      #creating a dictionary for current values
      dic={"x":x_value,"y":y_value,"z":z_value}
      #reading json data
      file=open('data.json','r')
      ren=json.load(file)
      #hardware action call
      value=hardware_action(float(ren["x"]),float(ren["y"]),int(ren["z"]),float(x_value),float(y_value),int(z_value))
      file.close()
      #Rewriting json data with current values
      f=open("data.json","w")
      json.dump(dic,f)
      f.close()

    return success(value)

def delete_image():
    for file in os.listdir('./static/images/'):
        os.remove(os.path.join('./static/images/',file))
if __name__ == '__main__':
    app.run(host="0.0.0.0")
