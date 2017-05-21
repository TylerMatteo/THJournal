from flask import Flask, render_template, redirect, url_for, request
from forms import EntryForm
from entry import Entry

app = Flask(__name__)
app.secret_key = 'asfhofijofw0923nowf408h23oinfewoihfew'

@app.route('/')
def index():
    entries = Entry.select()
    return render_template('index.html', entries=entries)

@app.route('/entries/<entry_id>')
def details(entry_id):
    entry = Entry.get(Entry.id == entry_id)
    return render_template('detail.html', entry=entry)

@app.route('/entries/edit/<entry_id>')
def edit(entry_id):
    entry = Entry.get(Entry.id == entry_id)
    form = EntryForm(obj=entry)
    return render_template('edit.html', form=form)

@app.route('/entries/delete/<entry_id>')
def delete(entry_id):
    Entry.get(Entry.id == entry_id).delete_instance()
    return redirect(url_for('index'))

@app.route('/entry', methods=('GET', 'POST'))
def new():
    form = EntryForm()
    print('TITLE')
    print(form.title.data)
    if form.validate_on_submit():
        #print('Valid!')
        Entry.create(
            title=form.title.data,
            date=form.date.data,
            timespent=form.timespent.data,
            body=form.body.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    #else:
        # print('Not valid!')
        # print(form)
        # try:
        #     user = models.User.get(models.User.email == form.email.data)
        # except models.DoesNotExist:
        #     flash("Your email or password doesn't match!", "error")
        # else:
        #     if check_password_hash(user.password, form.password.data):
        #         login_user(user)
        #         return redirect(url_for('index'))
        #     else:
        #         flash("Your email or password doesn't match!", "error")
    return render_template('new.html', form=form)

app.run(host='127.0.0.1', port=8080, debug=True)
    
