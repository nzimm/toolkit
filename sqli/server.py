#!/usr/bin/python3
import os, sys
import random
import sqlite3
import time
import cherrypy

DB_NAME = "database.db"

class InjectionDemo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

@cherrypy.expose
class DatabaseHandler(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self, selectTerm):

        # NOTE: Constructing SQL querys with string concatenation allows for injection!
        queryString = "SELECT username FROM users WHERE firstname='{}';".format(selectTerm.lower())

        # Connect to database
        with sqlite3.connect(DB_NAME) as connection:
            # Return string for index.html
            display_string = ""

            # Separate into multiple commands
            for query in queryString.split(';'):

                try:
                    # Attempt to execute sqlite3 query
                    responce = connection.execute(query)

                    # Create label for result table
                    display_string += "<span id=\"table_query\">{}</span><br><table>".format(query)

                    # Format output into HTML tables
                    for row in responce.fetchall():
                        display_string += "<tr>"
                        for field in row:
                            display_string += "<td>{}</td>".format(field)
                        display_string += '</tr>'
                    display_string += '</table><br>'

                # Handle improper query strings
                except sqlite3.OperationalError as err:
                    print(err)
                    return "Input error"

            # Report unfound results to user
            if display_string.replace("<table>","").replace("</table>","") == "":
                return "No results found"

            return display_string


def setup_database():
    '''
    Create the `users` table in database when server spins up
    '''
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("CREATE TABLE users (username, firstname, lastname, password)")
        connection.execute("INSERT INTO users VALUES ('dama2741', 'david', 'madison', 'monkey123')")
        connection.execute("INSERT INTO users VALUES ('agnwl390', 'allen', 'mackinzie', 'password1234')")
        connection.execute("INSERT INTO users VALUES ('stwe5528', 'steven', 'west', 'password!')")
        connection.execute("INSERT INTO users VALUES ('rabl4950', 'raquel', 'black', 'tellmeyourname')")
        connection.execute("INSERT INTO users VALUES ('juja1425', 'juliette', 'jabroni', 'secret')")
        connection.execute("INSERT INTO users VALUES ('jodo3849', 'john', 'doe', 'joejoemonkeybo')")
        connection.execute("INSERT INTO users VALUES ('besm4241', 'becky', 'smith', 'qwerty1234')")

def cleanup_database():
    '''
    Drop the `users` table from database on server shutdown
    '''
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("DROP TABLE users")


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(sys.path[0])
        },
        '/database': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    cherrypy.engine.subscribe('start', setup_database)
    cherrypy.engine.subscribe('stop', cleanup_database)

    webapp = InjectionDemo()
    webapp.database = DatabaseHandler()
    cherrypy.quickstart(webapp, '/', conf)

