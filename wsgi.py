from app import app
from app.config import Config


if __name__ == '__main__':
    if Config.DEBUG:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0', debug=False)
