

from flask import Flask,render_template,request,session,redirect,url_for,flash
from pymongo import MongoClient # mongodb 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'jaypatel19112001'
client = MongoClient('localhost', 27017) # connection 
db = client.Website # create table
regapi = db.Userdata # triger


@app.route('/login',methods=['GET','POST'])
def LoginPage():
    error =None
    if request.method == "POST":
        email=request.form['loginemail']
        pwd=request.form['loginpss']
        userdata=regapi.find_one({'email':email})
        if not userdata:
            flash("Email id not Founed Please Check Email id ")
            return redirect(url_for('LoginPage'))
        else:
            print("encripted  password:",userdata['password']) 
            print("real password:",pwd) 
            newpwd = pwd[::-1]+pwd[::-1]+pwd
            if userdata['password'] == newpwd:
                print("login done ....")
                session['login_user']={"name":userdata['name'],"email":userdata['email'],"city":userdata['city']}
                return redirect(url_for('HomePage'))

            else:
                flash('Email & Password not match')
                return redirect(url_for('LoginPage'))

    
    return render_template('LoginPage.html')





@app.route('/logout',methods=['GET','POST'])
def Logiout():
    session.clear()
    session['login_user']=''
    print("you are log out")
    flash('You were successfully LOG OUT')
    return redirect(url_for('HomePage'))



@app.route('/register',methods=['GET','POST'])
def RegistrationPage():
    if request.method == "POST":
        name=request.form['fullname']
        city=request.form['mycity']
        email=request.form['myemail']
        pwd1=request.form['pass1']
        pwd2=request.form['pass2']
        print(name,city,email)
        if pwd1==pwd2:
            newpwd = pwd1[::-1]+pwd1[::-1]+pwd1
            senddata = regapi.insert_one({
                "name":name,
                "city":city,
                "email":email,
                "password":newpwd
            })
            flash('You were successfully Register Your Data')
            return redirect(url_for('Logiout'))


        else:
            flash('Some kind of MisMatch Please Check Data')
            return redirect(url_for('RegistrationPage'))

    return render_template('RegistrPage.html')


@app.route('/')
def HomePage():
    session['login_user']=''
    if session['login_user']:
        print(" Log In successfulyy")
        name= session['login_user']['name']
        email= session['login_user']['email']
        city= session['login_user']['city']
        flash(f' hello {name} you are login My Website Welcome')
        return render_template('Home.html',name=name,email=email,city=city)

    else:
        print("not login  In Broo.")
        return render_template('Home.html')
   


@app.route('/test')
def TestPage():
    return render_template('Test.html')



@app.errorhandler(404)
def error404(error=None):
    return "<h1>Page Not Found</h1>"


# _______run_________________
if __name__=='__main__':
    app.run(debug=True)