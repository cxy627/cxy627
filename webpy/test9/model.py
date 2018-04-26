import web
import datetime

db = web.db.database(dbn="mysql", db="webpy", user="root", pw="123456")


def get_posts():
    return db.select("entries", order="id DESC")


def get_post(id):
    try:
        return db.select("entries", where="id=$id", vars=locals())[0]
        # vars是为了传入程序中的变量，这里因为有id，所以得传入，否则会产生valueerror
        # print('db.select("entries",where="id=\$id",vars=locals()) is' % (db.select("entries",where="id=$id",vars=locals())))
    except IndexError:
        return None


def new_post(title, text):
    db.insert("entries", title=title, content=text,
              posted_on=datetime.datetime.utcnow())


def del_post(id):
    db.delete("entries", where="id=$id", vars=locals())


def update_post(id, title, text):
    db.update("entries", where="id=$id",
              vars=locals(), title=title, content=text)
