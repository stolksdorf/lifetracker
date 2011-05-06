from google.appengine.ext import db
from google.appengine.api import users

class User(db.Model):
  google_user = db.UserProperty()
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  email = db.StringProperty()
  
  @staticmethod
  def get_by_google_user(google_user):
    return User.all().filter('google_user= ', google_user).get()


class Question(db.Model):
  format = db.IntegerProperty(required=True)
  user = db.ReferenceProperty(User)

class Response(db.Model):
  text = db.StringProperty(required=True)
  question = db.ReferenceProperty(Question)
