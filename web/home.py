from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from sendQueries import SendQueriesHandler
from ResponseHandler import ResponseHandler

class HomeHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("Hello!")

appRoute = webapp.WSGIApplication( [
  ('/', HomeHandler),
  ('/response', ResponseHandler),
  ('/sendQueries', SendQueriesHandler),
], debug=True)

def main():
  run_wsgi_app(appRoute)

if __name__ == '__main__':
  main()
