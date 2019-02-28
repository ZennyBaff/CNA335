from mysql import connector
from flask import Flask, redirect, url_for, request, render_template
import mysql.connector
app = Flask(__name__, static_url_path='')

#conn = mysql.connector.connect(user='root', password='1234',
#                                  host='10.22.1.240:8080',
#                                  database='zipcodes',
#                               buffered = True)



@app.route('/searchzipcode/<szip>')
def searchZIP(searchzip):
    # Get data from database
    return 'Fetching data\n Population for %s is 1000' % searchzip

@app.route('/updatezipcode/<uzip>')
def updateZIP(updatezip):
    # Get data from database
    return 'Fetching data\n Population for %s is 2000' % updatezip


@app.route('/update',methods = ['POST', 'GET'])
def up():
   if request.method == 'POST':
       user = request.form('uzip')
       return redirect(url_for('updatezipcode', updatezip=user))
   else:
       user = request.args.get('uzip')
       return redirect(url_for('success', name=user))

@app.route('/search', methods=['POST', 'GET'])
def sea():
   if request.method == 'POST':
       user = request.args.get['szip']
       return redirect(url_for('searchzipcode', searchzip=user))

#@app.route('/update',methods = ['POST', 'GET'])
#def update():
#   if request.method == 'POST':
#     user = request.form['updatezip']
#      return redirect(url_for('updatezipcode',updatezip = user))
#   else:
#       pass



@app.route('/')
def root():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)