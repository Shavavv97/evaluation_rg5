from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def read_csv():
    data = []
    with open('data/data.csv', 'r') as table:
        reader = csv.DictReader(table)

        for row in reader:
            data.append(row)
            
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
