
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request # need a form and get the data from the form

everything = [] #define empty array/list

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #either or
def hello_world():
    if request.method == 'POST':
        data = request.form['message']
        data = data.upper()
        everything.append(data) #array
        file = open('result.txt', 'w') #w=write
        for thing in everything:
            file.write(thing + '\n') #\n intro new line
        file.close() #make changes permanent to the harddisk
        return render_template('index.html', output=everything) #send the processed data back to html #every data stored in array shown
    return render_template('index.html') #get method

