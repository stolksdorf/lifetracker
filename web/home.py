from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class HomeHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("Hello!")

appRoute = webapp.WSGIApplication( [
  ('/', HomeHandler),
], debug=True)

def main():
  run_wsgi_app(appRoute)

if __name__ == '__main__':
  main()
