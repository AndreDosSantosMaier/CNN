from routes.cnnRoutes import cnnRoutes
from routes.guiaRoutes import guiaRoutes
from routes.sobreRoutes import sobreRoutes
from routes.tumorRoutes import tumorRoutes
def routeIndex(app):
    cnnRoutes(app)
    guiaRoutes(app)
    sobreRoutes(app)
    tumorRoutes(app)
