
# The Steakery - Bake by Day, Steak by Night: Django-Based Steakhouse & Bakery Website

## Project Overview 

**The Steakery** is a web application that serves as the online presence for a fictional steakhouse and bakery located in Dublin. This project combines an interactive frontend with a backend built using Django, allowing customers to explore the restaurant's offerings, make reservations, and manage bookings directly through the website.

![Responsive Mockup](/media/readme_images/responive_mockup.png)

[View The Steakery live website here](https://thesteakerypp4-443f2b4046b5.herokuapp.com/)


### Project Goals

The main goal of *The Steakery* project is to provide a seamless online experience where users can view the restaurant's offerings and book a table effortlessly. The project is aimed at offering an intuitive and visually appealing platform, focusing on user experience.

### Agile Methodology

Agile was used to organise and prioritise tasks, into ToDo, In Progress, Done & Won't have.
* User stories were created to illustrate what the project must be included, should be included and couldn't be included.
* The Board is set to public
* The Board was used to track progress on the project.
<details>
<summary> User Stories Template
</summary>

![Project Boards](media/readme_images/project_issues.png)

Please see the following link for the [project board](https://github.com/users/micdr93/projects/2)

### Target Audience

* People in Dublin who either want to grab a coffee and baked goods, or enjoy the steakhouse in the evening.
* Users who want to be able to book, edit, view or delet their reservations.
* Users who want to be able to add special requests, like wheelchair access, and to also select a table with guest capacity.

### First time user
* Users are met with a clean and straight forward homepage, with simple navigation.
* Users can log in or sign up, in order to make bookings.
* Users can view the menu of what the Steakery has to offer.

### Registered User
* Login process is simple.
* Registered users can create, view, edit or delete their bookings.

### Admin user

* Solid Django login portal for site admins.
* Access for admins to manage users, bookings, and tables.
* Admins can add more tables to facilitate more patrons.


### Design

* The Steakery features a clean white and red colour scheme and custom logo, which I created using Adobe Express.
* The logo sits on the navigation bar, ensuring consistent design scheme throughout the site.

### Logo 
* I created the logo myself using Adobe Express.

### Typography 
* Poppins and Serif fonts were used throughout the site, Bebas Neue was considered initially.

### Wireframes 

<details>
<summary> Booking
</summary>

![Booking Wireframe](media/wireframes/Booking.png)

<details>
<summary> Home Page
</summary>

![Home Wireframe](media/wireframes/home.png)

### Data Models for The Steakery

1. **User Model (Django AllAuth)**
    * Django AllAuth handles user authentication and registration. It provides a default user model to manage customer information.
    * A user can have multiple bookings (one-to-many relationship). Each booking is associated with a single user.

---

2. **SpecialRequest Model**
    * The `SpecialRequest` model allows users to include special requests with their table reservations (e.g., vegetarian meals, wheelchair access).
    * Admins can add or update special requests through the Django admin panel.
    * This model has a many-to-many relationship with the `Booking` model, meaning users can associate multiple special requests with a booking.

---

3. **Table Model**
    * The `Table` model represents a table in the restaurant that guests can reserve.
    * Each table has a unique `table_number` and a `max_capacity`, indicating the number of guests the table can accommodate.
    * The model ensures that tables are uniquely identified and helps manage available seating.

---

4. **Booking Model**
    * The `Booking` model stores information related to a table reservation made by a user. This includes the user, table, date, time, and number of guests.
    * The model ensures that:
        * Reservation dates and times are in the future.
        * The number of guests does not exceed the table’s maximum capacity.
        * Special requests (optional) can be linked to each booking.
    * Admins can manage bookings through the Django admin panel, and users can create, edit, or delete their bookings directly from the platform.

### Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](media/readme_images/erd_diagram.png)

* The **SpecialRequest** entity represents any special requests that can be associated with table reservations (e.g., vegetarian, wheelchair access). It contains the `id` as the primary key and the `name` field to describe the request.
* The **Table** entity represents individual tables in the restaurant, with fields including `id` as the primary key, `table_number` to uniquely identify each table, and `max_capacity` to specify how many guests the table can accommodate.
* The **Booking** entity represents a reservation made by a user for a specific table. It includes `id` as the primary key, `table_id` as a foreign key referencing the Table entity, `user_id` as a foreign key referencing the User entity, `date` for the reservation date, `time` for the reservation time, and `num_guests` for the number of guests in the booking. Special requests can also be linked through a many-to-many relationship.

This schema efficiently manages users, tables, and reservations. Users can make reservations for specific tables, and each booking includes relevant details such as the date, time, number of guests, and any special requests.

## Security Features 

### User Authentication

* Django's built-in authentication system is used for managing user registration, login, and account management. It ensures that only authenticated users can access specific features, like managing bookings.

### Login Decorator

* Views such as `create_booking`, `update_booking`, `delete_booking`, and `booking_list` use Django’s `login_required` decorator to restrict access to authenticated users only.
* This ensures that only logged-in users can create, modify, or view their reservations.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are automatically generated for each user session and included in forms to prevent unauthorized state-changing actions.
* When a user logs out, the session and the associated CSRF token are invalidated, making it harder for attackers to perform malicious actions via forged requests.

### Form Validation

* The `create_booking` and `update_booking` views validate form inputs using Django’s `BookingForm` class.
* It checks for multiple conditions, such as ensuring the reservation dates are valid, the number of guests is within table capacity, and that required fields are filled correctly.

### Overlapping Booking Prevention

* The system ensures there are no double bookings by checking for existing reservations for the same table on the selected date and time.
* If an overlapping booking is found, an error message is displayed, preventing users from booking the same table at the same time.

## Existing Features
* Home Page
![Steakery Homepage](media/readme_images/home.png)
* About
![Steakery About](media/readme_images/about.png)
* Menu
![Steakery Menu](media/readme_images/menu.png)
* Contact
![Steakery Contact](media/readme_images/contact.png)
* Create Booking
![Steakery Create Booking](media/readme_images/create_booking.png)
* Delete Booking
![Steakery Delete Booking](media/readme_images/delete_booking.png)
* Edit Booking
![Steakery Edit Booking](media/readme_images/edit_booking.png)
* Existing Bookings
![Steakery Existing Booking](media/readme_images/existing_bookings.png)
* Table Selection
![Steakery Table Selection](media/readme_images/table_Selection.png)
* Booking Login
![Steakery Booking Login](media/readme_images/booking_login.png)
* Booking Login 2
![Steakery Booking Login 2](media/readme_images/booking_login_2.png)


## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used
* [Postgresql](https://www.postgresql.org/)


### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework

### Programs Used

* [GitHub](https://github.com/) - Used for storing the project code online and version control.
* [GitPod](https://www.gitpod.io/) - Cloud-based IDE used to write and develop the code.
* [Heroku](https://www.heroku.com/) - Used to deploy the site as a cloud-based platform.
* [Google Fonts](https://fonts.google.com/) - Used to import the main fonts for the website.
* [Balsamiq](https://balsamiq.com/wireframes/) - Utilized to create wireframes during the planning phase.
* [Lucid Chart](https://lucidchart.com/) - Used to create the Entity Relationship Diagram (ERD).
* [Am I Responsive](https://ui.dev/amiresponsive) - Tool to display how the website appears on different device sizes.
* [Git](https://git-scm.com/) - Version control system used to track changes in the codebase.
* [JSHint](https://jshint.com/) - Used for JavaScript code validation.
* [W3C Markup Validation Service](https://validator.w3.org/) - Used for validating HTML for syntax correctness.
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS for any errors or warnings.
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python code for PEP8 compliance.

## Deployment and Local Developement

Live deployment can be found here [The Steakery](https://thesteakerypp4-443f2b4046b5.herokuapp.com/)

### Local Deployment

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project (https://github.com/micdr93/TheSteakeryPP4)
3. Click the fork button in the top right corner


#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [The Steakery](https://github.com/micdr93/TheSteakeryPP4)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### Heroku Deployment

1. Log into your [Heroku](https://www.heroku.com/) account or create an account if you don't already have one.
2. Click the "New" button at the top right corner and select "Create New App".
3. Enter a unique application name for your app.
4. Select your region.
5. Click "Create App".

#### Prepare environment and settings.py

1. In your local development environment (e.g., GitPod), create an `env.py` file in the root directory.
2. Add the `DATABASE_URL` and your chosen `SECRET_KEY` to the `env.py` file.
3. In your `settings.py`, import the `env.py` file and add the paths for the `SECRET_KEY` and `DATABASE_URL`.
4. Comment out the default SQLite database configuration.
5. Save all files and run migrations to update your database.
6. Update the `STATIC` files settings:
   - Set the URL, storage path, directory path, root path, media URL, and default file storage path for your static and media files.
7. Link the `TEMPLATES_DIR` to the templates directory in Heroku.
8. Add the Heroku app to the `ALLOWED_HOSTS` list in the format: `['your-app-name.herokuapp.com']`.

#### Add the following Config Vars in Heroku:

1. `SECRET_KEY` - Use a Django-generated secret key.
2. `PORT = 8000`
3. `DISABLE_COLLECTSTATIC = 1` - This is temporary and should be removed before final deployment.
4. `DATABASE_URL` - Use the PostgreSQL database URL provided by Heroku's built-in Postgres add-on.

#### Setting up PostgreSQL on Heroku:

1. In the "Resources" tab on your Heroku app dashboard, search for "Heroku Postgres".
2. Once the database is attached, the `DATABASE_URL` will automatically be set in your Heroku config vars.

#### Additional Files Needed for Heroku Deployment:

1. `requirements.txt` - A list of required packages for the project.
2. `Procfile` - Used to specify the commands that are run by Heroku's dynos.

Once these steps are complete, the site should be ready for deployment on Heroku with PostgreSQL.


