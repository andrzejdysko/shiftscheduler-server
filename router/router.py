from flask import Flask


def register_blueprints(app: Flask) -> None:
    register_GUI_blueprint(app)
    register_scheduler_blueprint(app)
    register_admin_blueprint(app)

def register_scheduler_blueprint(app: Flask) -> None:
    from .controllers import scheduler
    app.register_blueprint(scheduler.bp)

def register_GUI_blueprint(app: Flask) -> None:
    from .controllers import index
    app.register_blueprint(index.bp)
    app.add_url_rule("/", endpoint="index")

def register_admin_blueprint(app) -> None:
    print("register_admin_blueprint")
