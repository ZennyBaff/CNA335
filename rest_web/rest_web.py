from mysql import connector
from flask import Flask, redirect, url_for, request, render_template
import mysql.connector
app = Flask(__name__, static_url_path='')

conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='zipcodes',
                               buffered = True)
cursor = conn.cursor()



@app.route('/searchzipcode/<searchZIP>')
def searchzipcode(searchZIP):
    # Get data from database
    cursor.execute("SELECT * FROM `table 1` WHERE Zipcode=%s", [searchZIP])
    test = cursor.rowcount
    if test != 1:
        return searchZIP + " was not found"
    else:
        searched = cursor.fetchall()
        return 'Success, here you go: %s' % searched

@app.route('/updatezipcode/<updateZIP> <updatePOP>')
def updatezipcode(updateZIP, updatePOP):
    cursor.execute("SELECT * FROM `table 1` WHERE Zipcode=%s", [updateZIP])
    test = cursor.rowcount
    if test != 1:
        return updateZIP + " was not found"
    else:
        searched = cursor.fetchall()
        return 'Success, here you go: %s' % searched


@app.route('/update',methods = ['POST'])
def update():
       user = request.form['uzip']
       user2 = request.form['upop']
       return redirect(url_for('updatezipcode', updateZIP=user, updatePOP=user2))


@app.route('/search', methods=['GET'])
def search():
       user = request.args.get('szip')
       return redirect(url_for('searchzipcode', searchZIP=user))


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