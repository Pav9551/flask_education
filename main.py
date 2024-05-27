from flask import Flask
from flask import render_template
app = Flask(__name__)
def print_name():
    print(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/user/<name>')
def user(name):
    if name == 'pavel':
        print('Hi, pavel')
    #return '<h1>Hello, %s - user!</h1>' % name
    return render_template('index.html', name = name)

if __name__ == '__main__':
    print_name()
    app.run(debug=True)
    #pass
#print_name()
