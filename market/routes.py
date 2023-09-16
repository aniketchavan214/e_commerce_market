from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, user
from market.forms import RegisterForm
from market import db
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', item_name=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = user(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user : {err_msg}', category='danger')
    return render_template('register.html', form=form)


    
    
@app.route('/about/<username>')
def about(username):
    return f"This page is the about page of {username}"