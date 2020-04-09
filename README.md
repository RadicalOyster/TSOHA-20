**Dungeons and Dragons Database**

The purpose of this application is to be able to quickly add and retrieve information about the tabletop game Dungeons and Dragons 5th Edition. This includes at least items, equipment, spells and creatures. Additionally, users should be able to add specific entries to a list of personal favorites for quick access and filter information based on various criteria such as an item's properties.

**Current Features**

* Listing of creatures in the database, including basic stats
* Adding new creatures to the database
* Editing the ability scores of existing creatures

**App in Heroku**

[https://dnd-database.herokuapp.com/](https://dnd-database.herokuapp.com/)

**Documentation**

* [Database diagram](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/preliminary%20database%20diagram.png)
* [User stories](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/user_stories.md)

* Test user for Heroku: username: hello, password: world

**Change Log**

--09.04.2020--
* Added tables for creature abilities and damage types (work in progress, some functionality is still missing) and association tables for many-to-many relationships
* Added support for viewing a creature's abilities (no in-browser functionality for managing abilities yet)
* Added a navigation bar using bootstrap