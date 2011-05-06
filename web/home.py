from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class HomeHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("Hello!")

# called to add a datapoint to a user's dataset
class ResponseHandler(webapp.RequestHandler):
  def post(self):
    question_id = self.request.get('question')
    user_id = self.request.get('user')
    data = self.request.get('data')

    # get the question from the DB
    # get the user from the DB
    # add a Response object to the DB
    
    user = User.get_by_google_user(user_id)
    question = db.get(question_id) #hmmm

    response = Response(
      text = data,
      question = question,
    )

    response.put()

    self.response.out.write("Got it boss.\n")
    
class SendQueriesHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("Cronning this fucker!")  
    

appRoute = webapp.WSGIApplication( [
  ('/', HomeHandler),
  ('/response', ResponseHandler),
  ('/sendQueries', SendQueriesHandler),
], debug=True)

def main():
  run_wsgi_app(appRoute)

if __name__ == '__main__':
  main()
