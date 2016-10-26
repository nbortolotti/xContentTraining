from webapp2_extras.routes import RedirectRoute as Route

from views import MainPage

urlpatterns = [
    Route('/', MainPage),
]
