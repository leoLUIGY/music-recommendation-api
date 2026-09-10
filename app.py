from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

info = Info(title="Music Preference API", version="1.0.0")

app = OpenAPI(__name__, info=info)

CORS(app)

import Routes.Music_Preference_Rotas

if __name__ == "__main__":
    app.run( host="0.0.0.0", port=5001)