from google.appengine.ext import webapp

class SendQueriesHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("Cronning this fucker!")
