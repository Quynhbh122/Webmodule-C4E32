from flask import Flask, render_template, request
app = Flask(__name__)

accounts = [{
    'name' : 'name1',
    'pass' : 'pass1'
    },{
    'name' : 'name2',
    'pass' : 'pass2'
    },{
    'name' : 'name3',
    'pass' : 'pass3'
    },{
    'name' : 'name4',
    'pass' : 'pass4'
}]

check_pass = True

@app.route('/')
def login_answer():
    return render_template('pass.html',check_pass = check_pass)

@app.route('/',methods = ['POST'])
def check_account():
    account_name = request.form.get('name0')
    account_pass = request.form.get('pass0')
    check_pass = False
    result = False
    for account0 in accounts:
        if account_name == account0['name'] and account_pass == account0['pass']:
            result = True
            break

    return render_template('pass.html',result_end = result)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000, debug= True)