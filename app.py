def create_app():
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Student Planner is running!"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
