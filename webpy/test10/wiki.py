# coding:utf-8

import os
import web
import model
import markdown


# urls = (
#     "/", "Index",
#     "/new", "New",
#     "/edit/(\d+)", "Edit",
#     "/delete/(\d+)", "Delete",
#     "/(.*)", "Page",  # 是因为要用英文？
# )

urls = (
    "/", "Index",
)

t_globals = {
    "datastr": web.datestr,
    "markdown": markdown.markdown,
}

path = os.path.dirname(__file__)+"/templates/"
# 因为调试环境当前包非工作目录，所以要换绝对路径
print(path)

render = web.template.Render(path,base="base")
# 一是传模板目录，base是传基本模板，每个模板加载前都要加载它，最后是传入公共变量
# 效果就像from X import XX



class Index:
    def GET(self):
        pages = model.get_pages()
        print(pages)
        for page in pages:
            print(page)
        return render.index(pages)
        # 把数据从数据库调出来传到模板去


class New:
    # 先写好模板，然后把模板传给GET模板，最后填好POST回来
    # 这里的表单是在python里写的，后续能不用html5语言写在base.html里，
    # 后续加载，但这样会不会影响客户端的加载速度

    def not_page_exists(self, url):
        return not bool(model.get_page_by_url(url))
        # 如果数据库提取不到，证明这个url不存在，那就返回True

    page_exists_validator = web.form.Validator(
        "Page already exists", not_page_exists)

    form = web.form.Form(
        web.form.Textbox("url", web.form.notnull, page_exists_validator,
                         size=30, description="Location:"),
        # notnull应该是个验证器的实例，因此不用调用，用来要求textbox必须非空
        # description作为form模块中的实例变量传入render类，从而显示出来
        web.form.Textbox("title", web.form.notnull,
                         size=30, description="Page Title:"),
        web.form.Textarea("content", web.form.notnull, rows=30, cols=80,
                          description="Page content", post="use markdown syntax"),
        web.form.Button("Create Page"),
        # 这个按钮为什么没有接任何行动，就可以直接进行POST，应该是跟模板的from.render()
        # 有关
    )

    def GET(self):
        form = self.form()
        url = web.input(url='').url  # 获得http请求包头的url信息，怕没给，于是设了个默认值
        form.fill({"url": url})  # 前面是form中textbox的id，后面是填充的变量
        return render.new(form)

    def POST(self):
        form = self.form()
        if form.validates():
            return render.new(form)
        model.new_page(form.d.url, form.d.title, form.d.content)
        raise web.seeother("/"+form.d.url)  # 回头把这个改成另一个页面


class Delete:
    def POST(self, id):
        model.del_page(int(id))
        raise web.seeother("/")


class Edit:
    form = web.form.Form(
        web.form.Textbox("url", web.form.notnull,
                         size=30, description="Location:"),
        # 这里不用检测是否存在，那是不是就不应该允许修改
        web.form.Textbox("title", web.form.notnull,
                         size=30, description="Page Title:"),
        web.form.Textarea("content", web.form.notnull, rows=30, cols=80,
                          description="Page content", post="use markdown syntax"),
        web.form.Button("Update Page"),
    )

    def GET(self, id):
        form = self.form()
        page = model.get_page_by_id(id)
        form.fill(page)
        return render.Edit(form)

    def POST(self):
        form = self.form()
        if form.validates():
            return render.Edit(form)
        model.update_page(form.d.id, form.d.url, form.d.title, form.d.content)
        raise web.seeother("/"+form.d.url)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
