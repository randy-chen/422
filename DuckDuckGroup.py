from flask import Flask, render_template, request, session, redirect, url_for
import subprocess
import sys


app = Flask(__name__)

app.secret_key = "CHARCL"

@app.route('/', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':

        java = sys.argv[1]
        javac = sys.argv[2]
        algorithm_java = sys.argv[3]
        categories_python = sys.argv[4]
        reader_python = sys.argv[5]
        csv_file = sys.argv[6]
        categories_txt = sys.argv[7]

        subprocess.run(['python3', categories_python, csv_file, '>', categories_txt], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(categories_txt)
        #return str(result)
        #return render_template('app.html')
    #if request.method == 'POST':
        # for column in CSV
        #if request.form["button pressed"] == "displaySliders":
        criteria_list = []
        categories = open(categories_txt, "r")
        for item in categories:
            criteria_list.append(item)

        session['num_criteria'] = criteria_list
        session['criteria_count'] = len(criteria_list)
        session['groups'] = [[1, "Cody Abe"], [2, "Randy Hen"], [3, "Jeremy Lin"]]

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
