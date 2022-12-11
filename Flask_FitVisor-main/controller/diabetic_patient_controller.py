from app import app
from model.diabetic_patient_model import diabeticPatient_model
from flask import request


obj = diabeticPatient_model()

@app.route("/user/assessment", methods=["POST"])
def user_assessment_controller():
    return obj.user_assessment(request.args)