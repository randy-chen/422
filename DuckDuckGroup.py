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

        # Reads the columns of the CSV file which correspond to the criteria we use to match people together
        subprocess.run(['python3', 'utils/Categories.py', csv_file, '>', 'categories.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        # Takes in the CSV and generates 'output.txt', a file which has the CSV data formatted in a way that allows our algorithm to generate groups.
        subprocess.run(['python3', 'utils/CSVReader.py', csv_file, '>', 'output.txt'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        # Compiles and runs the algorithm which was written in java.
        subprocess.check_call(['javac', 'person.java', 'grouping.java'], stdout=subprocess.PIPE)
        subprocess.run(['java', 'grouping', 'output.txt', 'final.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        # After categories.txt has been created, we store the criteria in a list in the session so the columns can be accessed in app.html
        criteria_list = []
        groups = []
        categories = open('categories.txt', "r")
        for item in categories:
            criteria_list.append(item)

        # After the groups have been generated, we the teams as list in the session so the teams can be accessed in app.html and displayed on the webpage.
        groupings = open("final.txt", "r")
        i = 1
        for group in groupings:
            groups.append([i,group])
            i+=1

        session['num_criteria'] = criteria_list
        session['criteria_count'] = len(criteria_list) # for use by app.html. If no criteria provided, there will not be a button for the user to click to generate groups.
        session['groups'] = groups


        return render_template('app.html')

    return redirect(url_for('error')) # Throws an error in the scenario when an incorrect request type is received.

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
