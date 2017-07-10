#!/usr/bin/python3
import os, sys
import sqlite3 
import cherrypy

DB_STRING = "sample.db"

class injectorDemo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')


@cherrypy.expose
class databaseService(object):
    
    @cherrypy.tools.accept(media='text/plane')
    def GET(self)
        with sqlite3.connect(DB_STRING) as conn:
            cherrypy.session(

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(sys.path[0])
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(injectorDemo(), '/', conf)
