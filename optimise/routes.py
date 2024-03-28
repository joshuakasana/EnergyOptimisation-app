from flask import render_template, url_for, redirect, flash, request
from optimise import app, db, bcrypt
from optimise.forms import RegistrationForm, LoginForm, changeExpenseBudget
from optimise.models import User, Stats
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
# @app.route("/base")
# @app.route("/index")
def base():
    return render_template('index.html')


@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    first_name = current_user.username
    budget = current_user.budget

    # Temperature
    temperature = 12
    humidity = 48
    form = changeExpenseBudget()
    if form.validate_on_submit():
        current_user.budget = form.expense_budget.data
        db.session.commit()
        flash(f'Expense Budget updated successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title='Action Center', form=form,
                            first_name=first_name, budget=budget, temperature=temperature, humidity=humidity)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(last_name=form.last_name.data, first_name=form.first_name.data, username=form.username.data, email=form.email.data, device_id=form.device_id.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('registerPage.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('loginPage.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('base'))