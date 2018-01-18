#!/usr/bin/python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os

# preHTML
preHTML = open('assets/data/template.html', 'r').read()

# script
script = '''
  <script type="text/javascript">
  function init(){
      var prevId = document.getElementsByClassName('active')[0];
      prevId.className = '';
      var currId = document.getElementById("%s");
      currId.className = 'active';
  }
  window.onload = init;
  </script>
'''

class Intro(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/intro.html', 'r').read()
        html = preHTML % ((markup, ''))
        self.response.out.write(html)

class Packing(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/packing.html', 'r').read()
        addJS = script % (('packing'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class PreArrival(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/preArrival.html', 'r').read()
        addJS = script % (('pre-arrival'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class AirportPickup(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/airportPickup.html', 'r').read()
        addJS = script % (('airport-pickup'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class PostArrival(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/post-arrival.html', 'r').read()
        addJS = script % (('post-arrival'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
        
class Housing(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/housing.html', 'r').read()
        addJS = script % (('housing'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class CampusLife(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/campus-life.html', 'r').read()
        addJS = script % (('campus-life'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Food(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/food.html', 'r').read()
        addJS = script % (('food'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Shopping(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/shopping.html', 'r').read()
        addJS = script % (('shopping'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Sports(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/sports.html', 'r').read()
        addJS = script % (('sports'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
        
class Transportation(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/transportation.html', 'r').read()
        addJS = script % (('transportation'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Music(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/music.html', 'r').read()
        addJS = script % (('music'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
        
class Academics(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/academics.html', 'r').read()
        addJS = script % (('academics'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Books(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/books.html', 'r').read()
        addJS = script % (('books'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Courses(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/courses.html', 'r').read()
        addJS = script % (('courses'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Finance(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/finance.html', 'r').read()
        addJS = script % (('finance'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Tuition(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/tuition.html', 'r').read()
        addJS = script % (('tuition'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Lifestyle(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/lifestyle.html', 'r').read()
        addJS = script % (('lifestyle'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class FAQ(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('assets/data/faq.html', 'r').read()
        addJS = script % (('faq'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
    
application = webapp.WSGIApplication([('/', Intro),
                                      ('/packing.html', Packing),
                                      ('/pre-arrival.html', PreArrival),
                                      ('/airport-pickup.html', AirportPickup),
                                      ('/post-arrival.html', PostArrival),
                                      ('/housing.html', Housing),
                                      ('/campus-life.html', CampusLife),
                                      ('/food.html', Food),
                                      ('/shopping.html', Shopping),
                                      ('/sports.html', Sports),
                                      ('/transportation.html', Transportation),
                                      ('/music.html', Music),
                                      ('/academics.html', Academics),
                                      ('/books.html', Books),
                                      ('/courses.html', Courses),
                                      ('/finance.html', Finance),
                                      ('/tuition.html', Tuition),
                                      ('/lifestyle.html', Lifestyle),
                                      ('/faq.html', FAQ),
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
