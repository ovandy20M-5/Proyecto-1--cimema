from flask import Flask
from flask_mysqldb import MySQL

from config import config

app=Flask(__name__)

conexion=MySQL(app)


@app.route("/film")
def list_movies():
    try:
        return "OK"
        except Exception as ex:
            return "Error"


def Page not found(Error):
    return "<hi> the page you are trying to find does not exist...</hi>"


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404, the page you are trying to find does not exist)
    app.run()

