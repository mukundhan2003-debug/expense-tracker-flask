import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

#Home page
@app.route('/')
def index():
    return render_template('index.html')

#Add expense
@app.route('/add', methods=['POST'])
def add():
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])

    return redirect('/')
#View expenses
@app.route('/view')
def view():
    data = []

    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except:
        pass

    return render_template('view.html', data=data)

#Graph page

import matplotlib.pyplot as plt

@app.route('/graph')
def graph():
    data = {}

    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[0])

                if category in data:
                    data[category] += amount
                else:
                    data[category] = amount

        plt.bar(data.keys(), data.values())
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.savefig("static/graph.png")
        plt.close()

    except:
        pass

    return render_template('graph.html')

#Run app

if __name__ == '__main__':
    app.run(debug=True)

