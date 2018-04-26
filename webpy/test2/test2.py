import web

import os  
root = os.path.dirname(__file__)   #是我的电脑编译器的原因还是。。
path= root +"/templates/" #保险起见最好都加上绝对路径
render = web.template.render(path)

db = web.database(dbn='mysql', user='root', pw='123456', db='webpy')
db.insert("todo",title="123")


urls =(
        '/', 'index',
        '/add', 'add'
        )  

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

class add:
    def POST(self):
        i =  web.input()
        n = db.insert("todo",title=i.title)
        raise web.seeother("/")

if __name__ =="__main__":
    app = web.application(urls, globals())
    app.run()
