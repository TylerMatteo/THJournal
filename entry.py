from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
    title = CharField()
    date = DateField()
    timespent = IntegerField()
    body = TextField()
    resources = TextField()

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Entry], safe=True)
