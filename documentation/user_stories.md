**User Stories**

* As a user I should be able to easily see all the creatures in the database

  * sql query:
```
SELECT * FROM CREATURE
```

* As a user I should be able to filter creatures by name

  * sql query (finding all creatures with the string "go" in their name:
```
SELECT * FROM CREATURE WHERE Creature.name LIKE %go%
```

* As a user I should be able to add creatures to my favorites

  * sql query for user with id=1 adding creature with id=1 to favorites:
```
INSERT INTO account_creature (account_id, creature_id) VALUES (1, 1);
```

* As an admin I should be able to add creatures to the database

  * sql query for user with id=1 adding creature with id=1 to favorites (simplified with fewer attributes to make the example easier to read, in the database creatures actually have far more attributes):
```
INSERT INTO creature (name, hp, ac) VALUES ("Goblin", 15, 13);
```

* As an admin I should be able to add abilities to creatures

  * sql query for adding new ability
```
INSERT INTO ability (name, description, toHit) VALUES ("Scimitar", "Melee Weapon Attack", 4);
```

* sql query creating an attack with damage type id=1 to link to ability id=1 (damage types are initialized when the application launches so the user does not have to worry about that)
```
INSERT INTO attack (damageFormula, ability_id, damagetype_id) VALUES ("1d6+2", 1, 1);
```

* Linking ability with id=1 to creature with id=1

```
INSERT INTO creature_ability (ability_id, creature_id) VALUES (1, 1);
```

* As a user I should be able to see a creature's abilities
 * sql_query for finding a creature id=1's abilities:

```
SELECT * FROM Ability LEFT JOIN creature_ability ON creature_ability.ability_id = ability.id
LEFT JOIN Creature ON creature.id = creature_ability.creature_id WHERE creature.id = 1;
```

* sql query for finding the attacks linked to ability id=1:
```
SELECT * FROM Attack WHERE ability_id = 1
```

* sql query for finding creatures with attacks of damage type id=1:
```
SELECT * FROM CREATURE
LEFT JOIN Creature_Ability ON Creature.id = Creature_Ability.creature_id
LEFT JOIN Ability ON Ability.id = Creature_Ability.ability_id
LEFT JOIN Attack ON Attack.ability_id = Ability.id
LEFT JOIN Damage_Type ON Damage_Type.id = Attack.DamageType_id
WHERE DamageType_id = 1
```

* As an admin I should be able to edit the stats of creatures:
  * sql query for updating creature id=1's stats (simplified with fewer attributes)
```
UPDATE Creature
SET name="Goblin Two", hp=15, ac=10
WHERE id = 1
```

* As an admin I should be able to delete creatures:
  * sql query for deleting creature with id=1
```
DELETE FROM Creature WHERE id=1
```

* deleting references to creature id=1 from other tables:
```
DELETE FROM Account_Creature WHERE creature_id=1
```
```
DELETE FROM Creature_Ability WHERE creature_id=1
```

* As an admin I should be able to delete users:
  * sql query for deleting user with id=1
```
DELETE FROM Account WHERE id=1
```

* deleting references of user id=1 from other tables:
```
DELETE FROM Account_Creature WHERE account_id=1
```
```
DELETE FROM Account_Role WHERE account_id=1
```

* As a user I should be able to change my password
  * sql query for changing password of user with id=1
```
UPDATE Account
SET password="NewPassword"
WHERE ID =1
```

* As an admin I should be able to change a user's username and name
  * sql query for changing username of user with id=1
```
UPDATE Account
SET username="NewUsername"
WHERE ID =1
```
  * sql query for changing name of user with id=1
```
UPDATE Account
SET name="NewUsername"
WHERE ID =1
```