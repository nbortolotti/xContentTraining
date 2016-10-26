import webapp2 as webapp2
import settings
import urls


app = webapp2.WSGIApplication(urls.urlpatterns,
                              debug=settings.DEBUG, config=settings.CONFIG)

