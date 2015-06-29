# coding=utf-8
__author__ = 'JIE'


# coding=utf-8
__author__ = 'JIE'

import tornado.ioloop
import tornado.web
import os
from routes import async_sql
from routes import sync_sql

class test(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("over")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "public"),
    "template_path": os.path.join(os.path.dirname(__file__), "views"),
    "gzip": True,
    "debug": True,
}

application = tornado.web.Application([
    ("/async", async_sql.async_sql),
    ("/sync", sync_sql.syncTest),
    ("/test", test)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    print 'server start'
    tornado.ioloop.IOLoop.current().start()
