import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("ShiftSchedulerApi.default_settings")
        

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile(os.path.join(app.instance_path,'config.py'), silent=True) 
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    with app.app_context():
        configure(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

def configure(app:Flask)->None:
    configure_databases(app)
    register_blueprints(app)

def configure_databases(app:Flask)->None:
    from .infrastructure import db
    db.register_dbpool(app)
    db.register_migrations(app)

def register_blueprints(app:Flask)->None:
    from .router import router
    router.register_blueprints(app)