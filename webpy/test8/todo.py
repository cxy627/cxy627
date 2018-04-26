import web
import model
import os

urls = (
        "/","Index",
        "/del/(\d+)","Delete",
        )

root = os.path.dirname(__file__)   #是我的电脑编译器的原因还是。。
path= root +"/templates/" #保险起见最好都加上绝对路径

render = web.template.render(path,base="base")

class Index:
    form =web.form.Form(
        web.form.Textbox("title", web.form.notnull,description="I need to:"),
        web.form.Button('Add to do'),
        )

    def GET(self):
        todos = model.get_todos()
        form = self.form()
        return render.index(todos,form)

    def POST(self):
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')

class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
