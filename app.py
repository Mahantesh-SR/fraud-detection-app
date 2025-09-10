import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
import joblib
import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, request, jsonify, render_template

# Local imports
from recamandation_code import recondation_fn

# User lists
gmail_list = []
password_list = []
gmail_list1 = []
password_list1 = []

# Feature names for reference
features_list = [
    'Transaction amount', 'Transaction frequency',
    'Previous transaction history', 'Purchase amount compared to average',
    'CVV', 'Billing address verification', 'Time since last transaction',
    'Average transaction amount', 'Failed attempts',
    'Unusual purchase pattern'
]

features_list1 = [0]*10

# Initialize Flask app
app = Flask(__name__)

# ------------------- Routes ------------------- #

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register_page')
def show_register():
    return render_template('register.html')

@app.route('/logedin', methods=['POST'])
def logedin():
    int_features3 = [str(x) for x in request.form.values()]
    logu = int_features3[0]
    passw = int_features3[1]

    # DB connection
    db = pymysql.connect(host="localhost", user="root", password="", database="ddbb")

    # Fetch users and passwords
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1 = cursor.fetchall()
    for row1 in result1:
        gmail_list.append(str(row1[0]))

    cursor1 = db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2 = cursor1.fetchall()
    for row2 in result2:
        password_list.append(str(row2[0]))

    print("Users:", gmail_list)
    print("Passwords:", password_list)

    try:
        if gmail_list.index(logu) == password_list.index(passw):
            return render_template('home2.html')
    except ValueError:
        return jsonify({'result': 'Invalid Gmail or Password'})
    
    return jsonify({'result': 'Invalid Gmail or Password'})

@app.route('/register', methods=['POST'])
def register():
    int_features2 = [str(x) for x in request.form.values()]
    r1 = int_features2[0]
    r2 = int_features2[1]

    logu1 = r1
    passw1 = r2

    db = pymysql.connect(host="localhost", user="root", password="", database="ddbb")
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1 = cursor.fetchall()
    for row1 in result1:
        gmail_list1.append(str(row1[0]))

    if logu1 in gmail_list1:
        return jsonify({'result': 'This Gmail is already in use'})
    else:
        sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
        val = (r1, r2)
        try:
            cursor.execute(sql, val)
            db.commit()
        except:
            db.rollback()
        db.close()
        return render_template('login.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

# ------------------- Prediction Route ------------------- #
@app.route('/crop/predict1', methods=['POST'])
def predict1():
    '''
    Fraud transaction prediction route
    '''
    try:
        # Get form inputs
        int_features = [str(x) for x in request.form.values()]
        print("User Input:", int_features)

        # Get prediction and probability
        prediction, prob = recondation_fn(*int_features)

        # Format result
        if prediction == 0:
            result = "✅ Safe! Transaction is Legitimate"
        else:
            result = "⚠️ Alert! Transaction is Fraudulent"

        fraud_score = f"Fraud Probability: {prob[1]*100:.2f}%"

        # Render the results page
        return render_template(
            'results.html',
            prediction1_text=result,
            score_text=fraud_score
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error in prediction: {str(e)}"

@app.route('/crop1')
def crop1():
    return render_template('analyse.html')

@app.route('/crop2')
def crop2():
    return render_template('analyse1.html')

# ------------------- Main ------------------- #
if __name__ == "__main__":
    app.run(debug=True)
