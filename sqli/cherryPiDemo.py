#!/usr/bin/python3
import os, sys
import time
import sqlite3 
import cherrypy

DB_NAME = "sample.sqlite"

class injectorDemo(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <title>SQL injection demo</title>
          </head>
          <body>
            <h1>SQLite3 landing page</h1>
            <form method="get" action="query">
              <input type="text" value="SELECT firstName from users" name="queryString" />
              <button type="submit">Query</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def query(self, queryString="SELECT firstName from users"):
        return queryString


@cherrypy.expose
class DatabaseAccessService(object):
    
    @cherrypy.tools.accept(media='text/plain')
    def GET(self, queryString):
        with sqlite3.connect(DB_NAME) as conn:
            queryReturn = conn.execute("SELECT {} FROM users".format(queryString))
            return queryReturn.fetchone()

        

if __name__ == '__main__':
#    conf = {
#        '/': {
#            'tools.staticdir.root': os.path.abspath(sys.path[0])
#        },
#        '/static': {
#            'tools.staticdir.on': True,
#            'tools.staticdir.dir': './public'
#        }
#    }
    cherrypy.quickstart(injectorDemo(), '/')#, conf)
