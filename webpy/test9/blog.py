# coding:utf-8
import web
import model
import os
import datetime

urls = (
    "/", "Index",
    "/view/(\d+)", "View",
    "/new", "New",
    "/delete/(\d+)", "Delete",
    "/edit/(\d+)", "Edit",
)

t_globals = {
    'datestr': web.datestr
}
print("posted_on is %s " % datetime.datetime.utcnow())
print(web.datestr(datetime.datetime.utcnow()))
print(web.datestr(datetime.datetime.utcnow()))
# 定义模板位置，并设置base为基础模板（先加载它，并设置了一个公共变量）
path = os.path.dirname(__file__)+"/templates/"
render = web.template.Render(path, base="base", globals=t_globals)


class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)


class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)


class New:
    # 建立编辑博客的表单
    form = web.form.Form(
        web.form.Textbox("title", web.form.notnull,
                         size=30, description="post title:"),
        web.form.Textarea("content", web.form.notnull,
                          rows=30, cols=80, description="post content:"),
        web.form.Button("post entry")
    )

    def GET(self):
        print("self.form()is%s" % self.form())
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)  # 为什么会多个d
        raise web.seeother("/")


class Delete:
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother("/")


class Edit:
    def GET(self, id):
        print("i get")
        post = model.get_post(int(id))
        print("post is " % post)
        form = New.form()
        form.fill(post)
        return render.edit(post, form)  # 既然填好了form ，为什么还要交post

    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))  # 获取这个是为了假提交时，进入编辑界面
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)  # 这个d的方法会被淘汰吗
        raise web.seeother("/")


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
