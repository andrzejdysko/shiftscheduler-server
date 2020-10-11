import sqlite3
import click
from flask import current_app, g, Flask
from flask.cli import with_appcontext
from .dbpool import get_dbpool
from .sql_connection import SqlConnection
from .migrations.mysql import upgrade
from flask import current_app

def get_db(database_name:str):
    if 'db' not in g:
        g.db = SqlConnection(current_app.dbpool,database_name)
    return g.db


def close_db(e=None) -> None:
    db = g.pop('db', None)
    if db is not None:
        db.close()

def upgrade_db() -> None:
    db = get_db()
    upgrade(db)

@click.command('upgrade-db')
@with_appcontext
def upgrade_db_command() -> None:
    """Migrating changes."""
    upgrade_db()
    click.echo('Database upgraded.')

def register_dbpool(app: Flask) -> None:
    app.dbpool = get_dbpool(app.config["SCHEDULER_CONFIG"])
    app.teardown_appcontext(close_db)
    
def register_migrations(app: Flask) -> None:
    app.cli.add_command(upgrade_db_command)
