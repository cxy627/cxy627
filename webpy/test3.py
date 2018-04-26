import web

urls =  (
        "/(.*)/","redirect",
        "/.*", "hello"
        )

class redirect:
    '''
    预处理所有带/结尾的网址
    '''
    def GET(self,path):
        web.seeother("/"+path)

class hello:
    def GET(self):
        return "hello,world"

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()
