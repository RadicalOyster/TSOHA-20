**Dungeons and Dragons Database**

The purpose of this application is to be able to quickly add and retrieve information about creatures from the tabletop game Dungeons and Dragons 5th Edition. This includes basic statistics such as their ability scores and abilities.

**Current Features**

* Listing of creatures in the database, including basic stats and abilities
* Adding new creatures to the database (admins only)
* Individual pages for creatures with additional information
* Editing the ability scores of existing creatures
* Some user management features for admins (deleting users and editing their details)

**App in Heroku**

[https://dnd-database.herokuapp.com/](https://dnd-database.herokuapp.com/)

**Documentation**

* [Database diagram](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/preliminary%20database%20diagram.png)
* [User stories](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/user_stories.md)

* Test users for Heroku:
(admin) username: hello, password: world

(user) username: Odin, password: Harold

**Features to add**

* Better security (encoded passwords, only user should be able to change their own password)
* Implementing attacks with multiple damage rolls (requires restructuring of the database)
* Allowing users to manage their own accounts (eg. change or reset their password)
* Allowing users to add creatures to a list of favorites
* Filtering creatures by different criteria
* Refined interface
* More robust creature statistics such as alignment and spells

**Change Log**

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
