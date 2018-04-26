#coding:utf-8

import web

urls = (
        "/page?","ha",
        "/","index",
        "/test/(.*)","TEST"
        )
        
        #
class index:
    def GET(self):
        return "hello world" 

class TEST(object):
    def GET(self,id):
        return "{0}".format(id)

class ha(object):
    def GET(self):
        i = web.input(num=None)
        return "in ha num is {0}".format(i.num)

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()
