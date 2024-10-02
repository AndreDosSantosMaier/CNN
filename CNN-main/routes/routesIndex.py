from routes.cnnRoutes import cnnRoutes
from routes.guiaRoutes import guiaRoutes
from routes.sobreRoutes import sobreRoutes
def routeIndex(app):
    cnnRoutes(app)
    guiaRoutes(app)
    sobreRoutes(app)
