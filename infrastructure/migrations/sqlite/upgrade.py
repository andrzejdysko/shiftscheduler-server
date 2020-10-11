from  sqlite3 import Connection
from os import path,listdir
from flask import current_app
from typing import List

def upgrade(db:Connection)->None:
    files:List[str] = listdir(path.join(current_app.root_path,'db\\migrations'))
    migrated:List[str]=get_migration_history(db)
    files = list(filter(lambda x:not migrated.__contains__(x) and x.find(".sql")>0,files))
    for file in files:
        with current_app.open_resource(path.join(current_app.root_path,'db\\migrations\\'+file)) as f:
            try:
                db.executescript(f.read().decode('utf8'))
                register_migration(db,file)
            except Exception as err:
                print("Error migrating script "+file+": " + err)
            

def get_migration_history(db:Connection)->List[str]:
    result:List[str]=[]
    script_migrated = db.execute('SELECT * FROM MigrationsHistory WHERE DateExecuted is not null').fetchall()
    for row in script_migrated:
        result.append(row['ScriptName'])
    return result

def register_migration(db:Connection, file:str)->None:
    cmd = "INSERT INTO MigrationsHistory (ScriptName) SELECT '"+file+"';"
    db.execute(cmd)
    db.commit()