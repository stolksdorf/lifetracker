from google.appengine.ext import webapp

# called to add a datapoint to a user's dataset
# To hit this, send a post to "{base-url}/response" with
# data question_id, user_id, data, and a timestamp
class ResponseHandler(webapp.RequestHandler):
  def post(self):
    question_id = self.request.get('question')
    user_id = self.request.get('user')
    data = self.request.get('data')
    time = self.request.get('time', '')

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
