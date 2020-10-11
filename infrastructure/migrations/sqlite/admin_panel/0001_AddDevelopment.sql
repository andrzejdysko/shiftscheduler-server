DROP TABLE IF EXISTS Apps;
DROP TABLE IF EXISTS Forms;
DROP TABLE IF EXISTS Controls;
DROP TABLE IF EXISTS Fields;
DROP TABLE IF EXISTS SqlCommands;
DROP TABLE IF EXISTS ControlsSources;

CREATE TEMP TABLE IF NOT EXISTS Variables (Name TEXT PRIMARY KEY, Val TEXT);
INSERT INTO Apps(AppName) SELECT 'Development';
INSERT INTO Variables (Name,Val) SELECT 'ID_Apps',last_insert_rowid()

INSERT INTO Forms(FormName,ID_Apps)
SELECT 'Apps',Val
from Variables 
WHERE Name = 'ID_Apps'
UNION
SELECT 'Forms',Val
from Variables 
WHERE Name = 'ID_Apps'
UNION
SELECT 'Controls',Val
from Variables 
WHERE Name = 'ID_Apps'
UNION
SELECT 'Types',Val
from Variables 
WHERE Name = 'ID_Apps';

INSERT INTO ControlTypes(Name,Value)
SELECT 'Grid','grid'
UNION 
SELECT 'Card','card';

INSERT INTO Controls(ControlName, ID_Forms, ID_ControlTypes)
SELECT F.FormName+'_'+ct.Name,F.ID, CT.ID
FROM Forms F
JOIN ControlTypes CT ON 1=1;

INSERT INTO FieldTypes (Name,Value)
SELECT 'Text', 'text'
UNION
SELECT 'Date','date'
UNION
SELECT 'Checkbox','checkbox'
UNION
SELECT 'Dropdown','dropdown';

INSERT INTO Fields(ID_Controls,FieldName,Label,ID_FieldTypes)
SELECT C.ID, 'App_'+CT.Name+'_AppName','App name',FT.ID
FROM Controls c
JOIN FieldTypes FT ON FT.Name = 'Text' 
JOIN ControlTypes CT ON 1=1
JOIN Forms F on F.Name = 'Apps' and F.ID = C.ID_Forms;

INSERT INTO Fields(ID_Controls,FieldName,Label,ID_FieldTypes)
SELECT C.ID, 'Form_'+CT.Name+'_FormName','Form name',FT.ID
FROM Controls c
JOIN FieldTypes FT ON FT.Name = 'Text' 
JOIN ControlTypes CT ON 1=1
JOIN Forms F on F.Name = 'Forms' and F.ID = C.ID_Forms;

INSERT INTO Fields(ID_Controls,FieldName,Label,ID_FieldTypes)
SELECT C.ID, 'Form_'+CT.Name+'_FormApp','App',FT.ID
FROM Controls c
JOIN FieldTypes FT ON FT.Name = 'Text' 
JOIN ControlTypes CT ON ct.Name = 'Grid'
JOIN Forms F on F.Name = 'Forms' and F.ID = C.ID_Forms;

INSERT INTO Fields(ID_Controls,FieldName,Label,ID_FieldTypes,DropdownSource)
SELECT C.ID, 'Form_'+CT.Name+'_FormApp','App',FT.ID
FROM Controls c
JOIN FieldTypes FT ON FT.Name = 'Dropdown' 
JOIN ControlTypes CT ON ct.Name = 'Card'
JOIN Forms F on F.Name = 'Forms' and F.ID = C.ID_Forms;