from flask import Flask, render_template, request, session, redirect, url_for
import subprocess
import sys


app = Flask(__name__)

app.secret_key = "CHARCL"

@app.route('/', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':
        file = sys.argv[1]
        result = subprocess.run(['cat', file], stdout=subprocess.PIPE).stdout.decode('utf-8')

        #return str(result)
        #return render_template('app.html')
    #if request.method == 'POST':
        # for column in CSV
        #if request.form["button pressed"] == "displaySliders":
        criteria_list = []
        criteria_list.append(("Time"))
        criteria_list.append(("Space"))
        criteria_list.append(("Broccoli"))
        session['num_criteria'] = criteria_list
        session['criteria_count'] = len(criteria_list)

        #return redirect(url_for('groups'))
        #if request.form["button pressed"] == "displayTeams":
        #    return redirect(url_for('groups'))
        #CodyReadCSV(sysargv[])
        return render_template('app.html')
        #return redirect(url_for('error'))
        
    return redirect(url_for('error'))
    #return 'hey wus gud'
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
