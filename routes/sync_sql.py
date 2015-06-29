# coding=utf-8
__author__ = 'JIE'
import tornado.web
from db import client
import time

class syncTest(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        t = self.runSql()
        print time
        self.write(unicode(t))
        print "over"

    def runSql(self):
        t = time.time()
        db = client.conn()
        db.execute("select * from TABLE_CONSTRAINTS join (CHARACTER_SETS,STATISTICS)")
        # db.execute("select * from PLUGINS join (SESSION_STATUS,SESSION_VARIABLES);")
        db.close()
        return time.time() - t
