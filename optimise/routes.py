from flask import render_template, url_for, redirect, flash
from optimise import app
from optimise.forms import RegistrationForm, LoginForm, changeExpenseBudget
# from optimise.models import User



@app.route("/")
@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/home", methods=['GET', 'POST'])
def home():
    form = changeExpenseBudget()
    if form.validate_on_submit():
        flash(f'Expense Budget updated successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title='Action Center', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('base'))
    return render_template('registerPage.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@satient.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('base'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('loginPage.html', title='Login', form=form)
