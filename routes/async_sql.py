# coding=utf-8
__author__ = 'JIE'
import tornado
from tornado import web
from db import client
from tornado import concurrent
import time
from concurrent.futures import ThreadPoolExecutor


class async_sql(web.RequestHandler):
    executor = ThreadPoolExecutor(2)
    io_loop = tornado.ioloop.IOLoop.current()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        # print self.get_query_argument("test11")
        time = yield tornado.gen.Task(self.runSql)
        print time
        self.write(unicode(time))
        print "over"
        self.finish()

    @concurrent.run_on_executor
    def runSql(self):
        t = time.time()
        db = client.conn()
        db.execute("select * from TABLE_CONSTRAINTS join (CHARACTER_SETS,STATISTICS)")
        db.close()
        return time.time() - t
