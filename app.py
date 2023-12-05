from flask import Flask, request
import pickle

app = Flask(__name__)


model_pickle = open('./artifacts/classifier.pkl')

clf = pickle.load(model_pickle)


@app.route('/ping', methods=['GET'])
def ping():
    return 'HI'


@app.route('/prediction', methods=['POST'])
def prediction():
    loan_req = request.get_json()
    print(loan_req)
    loan_req = request.get_json()
    if loan_req['gender'] == "Male":
        gender = 0
    else:
        gender = 1
    if loan_req['married'] == "Unmarried":
        marital_status = 0
    else:
        marital_status = 1
    if loan_req['credit_history'] == "Unclear Debts":
        credit_status = 0
    else:
        credit_status = 1
    applicant_income = loan_req['applicant_income']
    loan_amt = loan_req['loan_amount']

    result = clf.predict([[gender, marital_status, applicant_income, loan_amt, credit_status]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}




if __name__=='__main__':
    app.run()