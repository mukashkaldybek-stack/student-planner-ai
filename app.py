py — бастапқы код"}
def create_app():
    from flask import Flask

    app = Flask(name)

    @app.route("/")
    def home():
        return "Student Planner is running!"

    return app


if name == "main":
    app = create_app()
