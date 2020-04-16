* As a user I should be able to look up creatures in the database and filter them based on various criteria such as their name

SQL queries:

Retrieving all creatures in the database: SELECT * FROM Creature

Retrieving a specific creature from the database (eg. "goblin"): SELECT * FROM Creature WHERE name = "goblin"

* As an admin I should be able to easily add entries to the database and modify or delete existing entries (partially implemented)


* As an admin I should be able to manage users (partially implemented)

SQL queries:

Changing the username of the user with id = 1 to 'TestUser': UPDATE Account SET username = "TestUser" WHERE id = 1

* As a registered user I should be able to quickly access my favorite creatures (not yet implemented)

SQL queries:

Retrieving a user's (with id = 1) favorited creatures: SELECT * FROM Creature JOIN Account_Creature ON Creature.id = Account.id JOIN Account ON Account.id = Account_Creature.account_id AND Account.id = 1