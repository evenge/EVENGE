import webapp2
from webapp2_extras import mako

class index(BaseHandler):
    def get(self):
        self.render_response('/template/index.html')

application = webapp2.WSGIApplication([
    ('/', index),
], debug=True)