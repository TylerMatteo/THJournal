from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
    title = CharField()
    timestamp = DateTimeField()
    body = TextField()
