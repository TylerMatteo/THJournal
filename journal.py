from flask import Flask, render_template, redirect, url_for
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
    return
    render_template('detail.html', entry=entry)


@app.route('/entries/edit/<entry_id>', methods=('GET', 'POST'))
def edit(entry_id):
    entry = Entry.get(Entry.id == entry_id)
    form = EntryForm(obj=entry)
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.date = form.date.data
        entry.timespent = form.timespent.data
        entry.body = form.body.data
        entry.resources = form.resources.data
        entry.save()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form)


@app.route('/entries/delete/<entry_id>')
def delete(entry_id):
    Entry.get(Entry.id == entry_id).delete_instance()
    return redirect(url_for('index'))


@app.route('/entry', methods=('GET', 'POST'))
def new():
    form = EntryForm()
    if form.validate_on_submit():
        Entry.create(
            title=form.title.data,
            date=form.date.data,
            timespent=form.timespent.data,
            body=form.body.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)

app.run(host='127.0.0.1', port=8080, debug=True)
