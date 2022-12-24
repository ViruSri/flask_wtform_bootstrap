from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import InputRequired,Email,Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = "my key"

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[InputRequired(),Email(check_deliverability=True)])
    password = PasswordField('Password',validators=[InputRequired(),Length(min=6)])
    submit = SubmitField("Log in")




@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    login_form=LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html",form=login_form)




if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)