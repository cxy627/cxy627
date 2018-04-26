# coding:utf-8

import web

db = web.db.database(dbn="mysql", db="webpy", user="root", pw="123456")


def get_pages():
    return db.select("pages", order="id DESC")


def get_page_by_id(id):
    return db.select("pages", where="id=$id", vars=locals())


def get_page_by_url(url):
    return db.select("pages", where="url=$url", vars=locals())


def del_page(id):
    db.delete("pages", where="id=$id", vars=locals())


def update_page(id, url, title, content):
    db.update("pages", where="id=$id", vars=locals(),
              url=url, title=title, content=content)
