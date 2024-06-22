from flask import Flask
from flask import render_template
app = Flask(__name__)
def print_name():
    print(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    if name == 'pavel':
        print('Hi, pavel')
    #return '<h1>Hello, %s - user!</h1>' % name
    return render_template('index.html', name = name)

@app.route('/219/')
def page1():
    return render_template('page1.html')
@app.route('/templ')
def template_page():
    return render_template('template_page.html')
if __name__ == '__main__':
    print_name()
    app.run(debug=True)
    #pass
#print_name()
