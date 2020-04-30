**Dungeons and Dragons Database**

This applications is a database of creatures for the tabletop game Dungeons and Dragons 5th Edition. Currently the application supports saving and viewing a creature's
hit points, armor rating, challenge rating, ability scores and saving throws and allows for 

**Current Features**

* Listing of creatures in the database, including basic stats and abilities
* Adding new creatures to the database (admins only)
* Individual pages for creatures with additional information
* Editing the ability scores of existing creatures (admins only)
* Adding creatures to a list of favorites (all registered users)
* Sorting creatures by name and damage type
* Adding abilities to creatures (admins only)
* Editing and deleting a creature's abilities (admins only)
* Changing a user's password (user only)
* Changing a user's name and username (admins only)
* Deleting users (admins only)
* Some user management features for admins (deleting users and editing their details)

**Features to add**

* Better security (encoded passwords, randomly generated secure user IDs, CSRF)
* Refined interface
* More robust creature statistics such as alignment as well abilities split into traits, actions, reactions and legendary actions
* Beter user management features
* Cleaning up the code

**App in Heroku**

[https://dnd-database.herokuapp.com/](https://dnd-database.herokuapp.com/)

**Documentation**

* [Installation](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/installation_guide.md)
* [Usage guide](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/usage_guide.md)
* [Database diagram](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/database_diagram.png)
* [User stories](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/user_stories.md)
* [Create tables for database](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/create_tables.md)

* Default admin login Username: Admin, Password: Admin

**Known issues**

* When editing a creature's ability the boxes for attack rolls are checked even if the ability has no attacks associated with it
* Some features are lacking error messages and notifications on success

**Change Log**

--30.04.2020--
* Admins can now delete and edit creature abilities
* Creatures can be filtered by name and damage type dealt by the creature
* Modifiers are now shown next to a creature's ability scores

--29.04.2020--
* Database is now initialized with user Admin and the user roles 'Admin' and 'User'
* Database is now initialized with damage types
* Admins can now add abilities to creatures

--26.04.2020--
* Users can now change their password
* Slight visual update
* Users can now add and remove creatures from a list of favorites

--25.04.2020--
* Added ability to create new users
* Fixed a bug with creatures' CON and Animal Handling modifiers not displaying properly

--24.04.2020--
* Updated view for individual creatures to support saving throws and skills
* Updated the creature edit form so all of the creature's statistics can be modified

--23.04.2020--
* Restructured parts of the database and added support for saving throws and skills for creatures (frontend not yet fully updated to support this)
* Added custom CSS to change the appearance of bootstrap elements

--16.04.2020--
* Added support for user roles and role-specific functionality
* Added basic user management for admins (adding new users not implemented yet)
* Updated documentation

--09.04.2020--
* Added tables for creature abilities and damage types (work in progress, some functionality is still missing) and association tables for many-to-many relationships
* Added support for viewing a creature's abilities (no in-browser functionality for managing abilities yet)
* Added a navigation bar using bootstrap
