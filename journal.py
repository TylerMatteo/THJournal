from flask import Flask, render_template, redirect, url_for
from forms import EntryForm
import entry


@app.route('/')
def index():
	entries = entry.select()
	return render_template('index.html', entries=entries)

@app.route('/entries/<entryid>')
def details(entry_id):

@app.route('/entries/edit/<entryid>')
def edit(entry_id):

@app.route('/entries/delete/<entryid>')
def delete(entry_id):

@app.route('/entry', methods=('GET', 'POST'))
def new()
	form = EntryForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match!", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match!", "error")
    return render_template('login.html', form=form)  
	
