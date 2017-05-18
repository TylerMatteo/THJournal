from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired

class EntryForm(Form):
	title = StringField(
		'Title',
		validators=[
			DataRequired()
		]
	)
	date = DateField(
		'Date',
		validators=[
			DataRequired()
		]
	)
	timespent = IntegerField(
		'Time Spent',
		validators=[
			DataRequired()
		]
	)
	body = TextAreaField(
		'Body',
		validators=[
			DataRequired()
		]
	)
	resources = TextAreaField(
		'Resources to remember',
		validators=[
			DataRequired()
		]
	)