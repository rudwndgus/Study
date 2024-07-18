from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/loginfail')
def loginfail():
    return render_template('loginfail.html')

@app.route('/login_confirm',methods = ['post'])
def login_confirm():
    id_ = request.form['id_']
    pw_ = request.form['pw_']
    if id_ == 'jh122975' and pw_ == 'wndgus':
        return redirect(url_for('layout'))
    else:
        return redirect(url_for('loginfail'))


if __name__ == '__main__':
    app.run(debug=True)
