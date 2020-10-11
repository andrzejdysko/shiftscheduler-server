INSERT INTO Users (UserLogin)
SELECT 'Supervisor';

INSERT INTO Roles (Name, ID_Users_Creator, ID_Users_Modified)
SELECT 'Admin',
U.ID,
U.ID
FROM Users U
WHERE U.UserLogin = 'Supervisor';