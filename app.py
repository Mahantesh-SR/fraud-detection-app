import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
import joblib
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
#import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

features_list=['Transaction amount', 'Transaction frequency',
       'Previous transaction history', 'Purchase amount compared to average',
       'CVV', 'Billing address verification', 'Time since last transaction',
       'Average transaction amount', 'Failed attempts',
       'Unusual purchase pattern']


features_list1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


from recamandation_code import recondation_fn
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import pymysql
    pymysql.install_as_MySQLdb()



# Open database connection
    db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ddbb"
)


# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('home2.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})
                  
                                               



                          
                     # print(value1[0:])
    
    
    
    

              
              # int_features3[0]==12345 and int_features3[1]==12345:
               #                      return render_template('index.html')
        
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import pymysql
    pymysql.install_as_MySQLdb()


# Open database connection
    db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ddbb"
)


# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login.html')

                      


    
   

@app.route('/crop')
def crop():
     return render_template('crop.html')



@app.route('/crop/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]
    int_features2=['1','2','3','4','5','6']
    a1=int_features1[0]
    a2=int_features1[1]
    a3=int_features1[2]
    a4=int_features1[3]

    
    a5=int_features1[4]
    a6=int_features1[5]
    a7=int_features1[6]
    a8=int_features1[7]
    a9=int_features1[8]
    a10=int_features1[9]
    
    
    
   # int_features21 = np.array(int_features2)




  #  int_features11 = int_features21.reshape(1, -1)
   # prediction1 = model1.predict(int_features11)

    output1 = recondation_fn(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
   # resultcrop = {value:key for key, value in croplist.items()}
    print(output1)

    if output1[0]==0:
      result="Safe! Transaction is Legitimate ✅"
    else:

      result="Alert! Transaction is Fraudulent ☠️"
    
    
 
    

    

    return render_template('crop.html', prediction1_text='  {} '.format(result))

@app.route('/crop1')
def crop1():
     return render_template('analyse.html')

@app.route('/crop2')
def crop2():
     return render_template('analyse1.html')



if __name__ == "__main__":
    app.run(debug=True)
