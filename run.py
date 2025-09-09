from app.init import create_app
from flask_cors import CORS
app = create_app()
app.config['JSON_AS_ASCII'] = False
CORS(app)
if __name__ == '__main__':
    app.run(debug=True)