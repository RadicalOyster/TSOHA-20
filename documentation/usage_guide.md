**Usage:**

Navigation of the application is primarily done from the navigation bar. Upon first opening the home page you will only have the options "List Creatures", "Sign up" and "Login". By default the database is initialized with a user with username "Admin", password "Admin" and admin rights. To change this, open the file application/auth/models.py and change the values in the method initialize_admin() to whatever you want the admin credentials to be.

**List Creatures**

This page lists all the creatures currently in the database. Clicking on the creature's name will take you to the creature's individual page with more detailed information. Creatures can also be sorted by name or damage type associated with their attacks.

**Sign Up**

The sign up link takes you to a form. Simply enter your name, username, password and password again to  create an account, then click login and enter your credentials. By default, new accounts will only have the "USER" role and other roles will need to be added directly to the database

**Login**

The login form is self-explanatory. Enter your username and password and you are now logged in. You now have access to two additional links: "My Favorites" and "Account". To logout, click the "Logout" link in the top right corner.

**My Favorites**

Registered users with the "USER" role have access to a few more features than unregistered users. While viewing a creature's individual page there is now an "add to favorites" button that will add the creature to a personal list of favorites for easy access. Clicking on "My Favorites" will bring you to your personal list.

**Account**

Here you can view your account information. Currently You can only change your password by clicking the "Change Password" button and filling in the form. You are then prompted to log in again using your new credentials.

**Admin Features**

Most features pertaining to adding, modifying or deleting data from the database are only available to users with the "ADMIN" role. They are as follows.

**Admin Panel**

Clicking the admin panel will bring you to an overview of all registered users. From here, clicking on the user's username will bring you to the user's individual page. From here you can edit the name and username of non-admin users as well as delete them.

**Adding new creatures**

Another option only accessible to admins is the "Add a creature" menu. This brings you to a form. Fill it with your desired creature statistics and check the boxes for saving throws and skills the creature is proficient in. Finally press the "Add creature" button to add the creature to the database. You will then be brought to the list creatures page.

**Editing a creature**

As an admin you will have a few more options on a creature's individual page. The "edit stats" button will bring up a form that is identical to the add creature form. From here you can change its stats and press "modify creature" to save your changes. The "delete creature" button is also available to admins and allows you to remove the creature from the database.

**Adding abilities to creatures**

To add abilities to a creature, press the "new ability" button which opens up another form. First enter the ability's name and description. Then, if your ability is an attack, check the "Attack" box. Enter the ability's to hit bonus, damage formula and select the attack's damage type from the dropdown menu. If the attack has two damage rolls (such as an attack from an enchanted sword that deals 1d6 slashing damage and 1d4 fire damage), check the "second roll" box and enter the damage formula and type for the second attack roll.

**Editing abilities**

Admins can click the name of a creature's ability to go to the ability's individual page. From here you can remove the ability by clicking the "delete ability" button or modify it by editing the form and clicking "update ability". 