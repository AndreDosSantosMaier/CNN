from flask import Flask
from routes.routesIndex import routeIndex
from flask_cors import CORS
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

class Main():
    def __init__(self):
        self.app = Flask(__name__, template_folder='templates') 
        CORS(self.app)
        routeIndex(self.app)
        
        
    def runApp(self):
        self.app.run('localhost', 3000, True)
        
        
if __name__ == '__main__':
    a = Main()
    a.runApp()