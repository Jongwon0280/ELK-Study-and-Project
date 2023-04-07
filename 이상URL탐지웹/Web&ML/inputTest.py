from flask import Flask, render_template, redirect, request, url_for
from meditate import result_print

app = Flask(__name__)
 
@app.route('/')
@app.route('/<string:num>')
def inputTest(num=None):
    return render_template('main.html', num=num)

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        base_url=request.form['num']
        result=result_print(base_url)

    return render_template('main.html',num=result)

 

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)
