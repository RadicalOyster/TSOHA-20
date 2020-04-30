**Dungeons and Dragons Database**

This applications is a database of creatures for the tabletop game Dungeons and Dragons 5th Edition. Currently the application supports saving and viewing a creature's
hit points, armor rating, challenge rating, ability scores and saving throws and allows for 

**Current Features**

* Listing of creatures in the database, including basic stats and abilities
* Adding new creatures to the database (admins only)
* Individual pages for creatures with additional information
* Editing the ability scores of existing creatures
* Some user management features for admins (deleting users and editing their details)

**Usage**

Navigation of the application is primarily done from the navigation bar. Upon first opening the home page you will only have the options "List Creatures", "Sign up" and "Login". By default the database is initialized with a user with username "Admin", password "Admin" and admin rights. To change this, open the file application/auth/models.py and change the values in the method initialize_admin() to whatever you want the admin credentials to be.

**List Creatures**

This page lists all the creatures currently in the database. Clicking on the creature's name will take you to the creature's individual page with more detailed information. Creatures can also be sorted by name or damage type associated with their attacks.

**Sign Up**

The sign up link takes you to a form. Simply enter your name, username, password and password again to  create an account, then click login and enter your credentials. By default, new accounts will only have the "USER" role and other roles will need to be added directly to the database

**Login**

The login form is self-explanatory. Enter your username and password and you are now logged in. You now have access to two additional links: "My Favorites" and "Account".

**My Favorites**

Registered users with the "USER" role have access to a few more features than unregistered users. While viewing a creature's individual page there is now an "add to favorites" button that will add the creature to a personal list of favorites for easy access. Clicking on "My Favorites" will bring you to your personal list.

**Account**

Here you can view your account information. Currently You can only change your password by clicking the "Change Password" button and filling in the form. You are then prompted to log in again using your new credentials.

**App in Heroku**

[https://dnd-database.herokuapp.com/](https://dnd-database.herokuapp.com/)

**Documentation**

* [Database diagram](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/preliminary%20database%20diagram.png)
* [User stories](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database/blob/master/documentation/user_stories.md)

* Default admin login Username: Admin, Password: Admin

**Features to add**

* Better security (encoded passwords, randomly generated secure user IDs, CSRF)
* Refined interface
* More robust creature statistics such as alignment and abilities split into traits, actions, reactions and legendary actions
* Beter user management features
* Cleaning up the code

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
