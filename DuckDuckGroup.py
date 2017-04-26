from flask import Flask, render_template, request, session, redirect, url_for
import subprocess
import sys


app = Flask(__name__)

app.secret_key = "CHARCL"

@app.route('/', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':
        #CSV of the student survey
        csv_file = sys.argv[1]

        subprocess.run(['python3', 'utils/Categories.py', csv_file, '>', 'categories.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        subprocess.run(['python3', 'utils/CSVReader.py', csv_file, '>', 'output.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        subprocess.check_call(['javac', 'person.java', 'grouping.java'], stdout=subprocess.PIPE)
        subprocess.run(['java', 'grouping', 'output.txt', 'final.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print('successfully ran java')
        #return str(result)
        #return render_template('app.html')
    #if request.method == 'POST':
        # for column in CSV
        #if request.form["button pressed"] == "displaySliders":
        criteria_list = []
        groups = []
        categories = open('categories.txt', "r")
        print(categories)
        for item in categories:
            criteria_list.append(item)

        groupings = open("final.txt", "r")
        i = 1
        for group in groupings:

            groups.append([i,group])
            i+=1


        session['num_criteria'] = criteria_list
        session['criteria_count'] = len(criteria_list)
        session['groups'] = groups

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
