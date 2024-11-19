from controllers.gliomaController import Glioma
from controllers.putuitaryController import Pituitary
from controllers.meningiomaController import Meningioma

def tumorRoutes(app):
    app.route('/glioma', methods=['GET'])(Glioma)
    app.route('/meningioma', methods=['GET'])(Meningioma)
    app.route('/pituitary', methods=['GET'])(Pituitary)
    
