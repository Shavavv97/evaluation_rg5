from flask import Flask, jsonify, request, render_template, redirect, url_for
import csv

app = Flask(__name__, template_folder="../templates", static_folder="../static")

#Obtain all the employees from the CSV file in a JSON.
@app.route('/', methods=['GET'])
def read_csv():
    employees = []
    with open('data/data.csv', 'r') as table:
        reader = csv.DictReader(table)

        for row in reader:
            employees.append(row)
    
    return jsonify(employees)

#Obtain the employee by ID
@app.route('/<int:id>', methods=['GET'])
def search(id):
    employees = []
    with open('data/data.csv', 'r') as table:
        reader = csv.DictReader(table)

        for row in reader:
            employees.append(row)

    employee = employees[(id - 1)]
    if not employee:
        return "There is not employee with that id"

    return jsonify(employee)

#Rendering a page for the employer
@app.route('/employees', methods=['GET'])
def employees():
    employees = []
    with open('data/data.csv', 'r') as table:
        reader = csv.DictReader(table)

        for row in reader:
            employees.append(row)

    return render_template('index.html', employees=employees)

#Append a new employee
@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        return redirect(url_for('employees'))

    elif request.method == "POST":
        employees = dict(request.form)
        first_name = employees["first_name"]
        last_name = employees["last_name"]
        email = employees["email"]
        ip_address = employees["ip_address"]

        if first_name == "" or last_name == "" or email == "" or ip_address == "":
            return "Please enter a valid employee"
            
        employees = []
        with open('data/data.csv', 'r') as table:
            reader = csv.reader(table)

            for row in reader:
                employees.append(row)

        with open('data/data.csv', 'a') as table:
            data = csv.writer(table)
            data.writerow([(int(row[0]) + 1), first_name, last_name, email, ip_address])

    return redirect(url_for('employees'))

#Error handlings
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_handlers/404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error_handlers/500.html"), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0")
