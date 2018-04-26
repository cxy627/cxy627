import web
import blog

urls =(
        "/blog",blog.app_blog,
        "/(.*)","index"
        )

class index:
    def GET(self,path):
        return "hello"+path

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
