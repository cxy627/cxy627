import web

urls = (
    "/count", "count",
    "/reset", "reset"
        )

app = web.application(urls, locals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})
    web.config._session = session
else:
    session = web.config._session

class count:
    def GET(self):
        session.count += 1
        return str(session.count)
        
class reset:
    def GET(self):
        session.count = 0
        raise web.seeother("/count")

if __name__ == "__main__":
    app.run()
