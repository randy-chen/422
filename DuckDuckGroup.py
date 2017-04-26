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
        output_txt = sys.argv[8]


        subprocess.run(['python3', categories_python, csv_file, '>', categories_txt], stdout=subprocess.PIPE).stdout.decode('utf-8')
        subprocess.run(['python3', reader_python, csv_file, '>', output_txt], stdout=subprocess.PIPE).stdout.decode('utf-8')
        subprocess.check_call(['javac', 'person.java', 'grouping.java'], stdout=subprocess.PIPE)
        subprocess.run(['java', 'grouping', output_txt, 'final.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print('successfully ran java')
        #return str(result)
        #return render_template('app.html')
    #if request.method == 'POST':
        # for column in CSV
        #if request.form["button pressed"] == "displaySliders":
        criteria_list = []
        groups = []
        categories = open(categories_txt, "r")
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
