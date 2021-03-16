# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask,render_template,redirect, url_for
App=Flask(__name__)
App.debug=True

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
@App.route('/')
def load():
    return redirect(url_for('myhome'))
@App.route('/home/')
def myhome():
    return render_template('home.html',name='Home')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    App.run(debug=True)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
