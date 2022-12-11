import json
import os
# import pandas as pd
import mysql.connector
from flask import make_response
class diabeticPatient_model():
    #Constructor
    def __init__(self):
        #This try and check blocks have been written for checking if the connection is established or not 
        #if yes then then Connection established will be shown in terminal and if not then it will print Error
        try:
            self.con = mysql.connector.connect(host="sql.freedb.tech",user="freedb_fitvisorRoor",password="c73F*CfR5CCgFSE",database="freedb_fitvisorproject")
            # self.con = mysql.connector.connect(host="localhost",user="root",password="@dataBase123",database="fitvisorproject")
            #For Commit
            self.con.autocommit=True   #This commit statement is for post when we want to save the changes in db made by sql queries
            #curosr
            self.cur = self.con.cursor(dictionary=True) # Curosr helps to perform dml operations
            print("Connection Established")
        except:
            print("Error")

    
    def user_assessment(self, data):
        self.cur.execute(f"INSERT INTO diabetic_patient(blood_pressure, cholesterol, diabetic_family, hba1c_date, hba1c_ranges, systolic_ranges,diastolic_ranges, cholesterol_ranges, married, other_diseases, pregnant) VALUES('{data['blood_pressure']}', '{data['cholesterol']}', '{data['diabetic_family']}', '{data['hba1c_date']}', '{data['hba1c_ranges']}', '{data['systolic_ranges']}', '{data['diastolic_ranges']}', '{data['cholesterol_ranges']}', '{data['married']}', '{data['other_diseases']}', '{data['pregnant']}')")
        res= make_response({"message": "Assessment conducted successfully",
                            "status" : "SUCCESS",
                            "code" : 200}, 200)
        res.headers['Access-Control-Allow-Origin'] = "*"   

        data=pd.read_csv(os.path.join(BASE_DIR ,"data/foodDiabetesChanged.csv"))
        data.head()
        return res

