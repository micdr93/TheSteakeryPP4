# The Steakery - Bake by Day, Steak by Night: Django-Based Steakhouse & Bakery Website

## Project Overview 

**The Steakery** is a web application that serves as the online presence for a fictional steakhouse and bakery located in Dublin. This project combines an interactive frontend with a backend built using Django, allowing customers to explore the restaurant's offerings, make reservations, and manage bookings directly through the website.

![Responsive Mockup](/media/readme_images/tslogo.webp)

[View The Steakery live website here](https://thesteakerypp4-443f2b4046b5.herokuapp.com/)
## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Goals](#project-goals)
3. [Agile Methodology](#agile-methodology)
4. [User Stories](#user-stories-template)
5. [Target Audience](#target-audience)
6. [First Time User](#first-time-user)
7. [Registered User](#registered-user)
8. [Admin User](#admin-user)
9. [Design](#design)
10. [Logo](#logo)
11. [Typography](#typography)
12. [Wireframes](#wireframes)
13. [Data Models for The Steakery](#data-models-for-the-steakery)
14. [Database Scheme](#database-scheme)
15. [Security Features](#security-features)
16. [Existing Features](#existing-features)
17. [Admin Features](#admin-features)
18. [Technologies Used](#technologies-used)
19. [Deployment and Local Development](#deployment-and-local-deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
    * [PostgreSQL Setup](#setting-up-postgresql-on-heroku)
20. [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Lighthouse Testing](#lighthouse-testing)
    * [CI Python Linter](#ci-python-linter)
21. [References](#references)
22. [Acknowledgements](#acknowledgements)
23. [Note to Assessor](#note-to-assessor)



### Project Goals

The main goal of *The Steakery* project is to provide a seamless online experience where users can view the restaurant's offerings and book a table effortlessly. The project is aimed at offering an intuitive and visually appealing platform, focusing on user experience.

### Agile Methodology

Agile was used to organise and prioritise tasks, into ToDo, In Progress, Done & Won't have.
* User stories were created to illustrate what the project must be included, should be included and couldn't be included.
* The Board is set to public
* The Board was used to track progress on the project.

### User Stories Template


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

- Booking

![Booking Wireframe](media/wireframes/Booking.png)

- Home Page

![Home Wireframe](media/wireframes/home.png)

### Data Models for The Steakery

1. **User Model (Django AllAuth)**
   * Django AllAuth handles user authentication and registration, providing a default user model with:
       * `id` (Primary Key)
       * `username` for user identification
   * A user can have multiple bookings (one-to-many relationship)

---

2. **Table Model**
   * The `Table` model represents individual tables in the restaurant with:
       * `id` (Primary Key)
       * `table_number` (Unique Key) for distinct table identification
       * `max_capacity` to specify guest capacity
   * Tables can have multiple bookings over time (one-to-many relationship)

---

3. **SpecialRequest Model**
   * The `SpecialRequest` model manages special requirements with:
       * `id` (Primary Key)
       * `name` to describe the request type
   * Connected to bookings through a many-to-many relationship
   * Examples include dietary restrictions or accessibility needs

---

4. **Booking Model**
   * The `Booking` model manages reservations with:
       * `id` (Primary Key)
       * `date` for reservation date
       * `start_time` and `end_time` for reservation duration
       * `num_guests` for party size
       * `additional_requests` for custom notes
       * `created_at` timestamp
       * `user_id` (Foreign Key) linking to User
       * `table_id` (Foreign Key, Nullable) linking to Table
   * Model validates:
       * Future dates for reservations
       * Guest count against table capacity
       * Special request associations
   * Managed through Django admin panel
   * Users can perform CRUD operations on their bookings
   * Supports many-to-many relationship with SpecialRequest model

Each model is designed for efficient relationship management and data integrity in the restaurant reservation system, with proper foreign key constraints and validation rules.

## Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](media/readme_images/erd_diagram.png)

## Entity Relationship Diagram (ERD) Overview

This document outlines the database schema for our restaurant reservation system, detailing the relationships between users, tables, bookings, and special requests.

### Core Entities

* The **User** entity represents people who can make table reservations in the system. It contains:
  * `id` (Primary Key) - Unique identifier
  * `username` - User's identifier

* The **Table** entity represents individual tables in the restaurant:
  * `id` (Primary Key) - Unique identifier
  * `table_number` (Unique Key) - Unique table identifier
  * `max_capacity` - Maximum number of guests per table

* The **SpecialRequest** entity stores special requirements for bookings:
  * `id` (Primary Key) - Unique identifier
  * `name` - Description of the special request

* The **Booking** entity manages reservations with the following fields:
  * `id` (Primary Key) - Unique identifier
  * `date` - Reservation date
  * `start_time` - Beginning of reservation
  * `end_time` - End of reservation
  * `num_guests` - Party size
  * `additional_requests` - Custom notes field
  * `created_at` - Timestamp of booking creation
  * `user_id` (Foreign Key) - Reference to User
  * `table_id` (Foreign Key, Nullable) - Reference to Table

### Relationships

* User → Booking: One-to-Many ("makes")
* Table → Booking: One-to-Many ("has")
* Booking ↔ SpecialRequest: Many-to-Many ("requested_in")

### System Functionality

This schema enables efficient management of restaurant reservations. Users can make table bookings while specifying:
* Date and time period
* Number of guests
* Special requests
* Additional notes

The system maintains proper relationships between all entities while allowing for flexible booking management through timestamps and optional table assignments.

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

### Existing Features

* Home Page:
   * Displays the navigation bar, with links to Menu, Contact, About and Bookings.
![Steakery Homepage](media/readme_images/home_desktop.png)
   *  Home Page on Desktop
![Steakery Homepage](media/readme_images/home_mobile.png)
   * Home Page on Mobile

* About Page:
   * Displays the About us section of the project, with a brief story and images.
![Steakery About](media/readme_images/about_desktop.png)
   * About Page on Desktop
![Steakery About](media/readme_images/about_mobile.png)
   * About Page on Mobile

* Menu Page:
   * Displays the Menu for the restaurant.
![Steakery Menu](media/readme_images/menu_desktop.png)
   * Menu page on Desktop
![Steakery Menu](media/readme_images/menu_mobile.png)
   * Menu page on Mobile

* Contact Page:
   * Displays the contact page and infoirmation for the restaurant including a submission form for users to send a message.
![Steakery Contact](media/readme_images/contact_desktop.png)
   * Contact page on Desktop
![Steakery Contact](media/readme_images/contact_mobile.png)
   * Contact page on Mobile

* Create Booking Page:
   * Allows users to create bookings, by signing up or logging in.
![Steakery Create Booking](media/readme_images/create_booking_desktop.png)
   * Create Booking on Desktop
![Steakery Create Booking](media/readme_images/create_booking_mobile.png)
   * Create Booking on Mobile

* Delete Booking Page:
   * Allows users to delete existing bookings, by signing up or logging in.
![Steakery Delete Booking](media/readme_images/delete_booking_desktop.png)
   * Delete Booking
![Steakery Delete Booking](media/readme_images/delete_booking_mobile.png)
   * Delete Booking

* Edit Booking Page:
   * Allows users to edit existing bookings, by signing up or logging in.
![Steakery Edit Booking](media/readme_images/edit_Booking_desktop.png)
   * Edit Booking on Desktop
![Steakery Edit Booking](media/readme_images/edit_booking_mobile.png)
   * Edit Booking on Mobile

* Existing Bookings:
   * Allows users to view existing bookings, by signing up or logging in.
![Steakery Existing Booking](media/readme_images/bookings_list_desktop.png)
   * Existing Bookings on Desktop
![Steakery Existing Booking](media/readme_images/bookings_list_mobile.png)
   * Existing Bookings on Mobile
![Steakery Existing Booking](media/readme_images/bookings_list_mobile_2.png)

* Booking Errors:
   * A sample of a couple of error messages users can encounter if they book a table out of hours, the same table twice etc.
![Steakery Booking Error](media/readme_images/booking_error_message_desktop.png)
   * Booking Error on Desktop
![Steakery Booking Error](media/readme_images/booking_error_message_mobile.png)
   * Booking Error on Mobile

* Table Selection:
   * Allows users to select a table with the appropriate capacity within the bookin form.
![Steakery Table Selection](media/readme_images/table_selection_desktop.png)
   * Table Selection on Desktop
![Steakery Table Selection](media/readme_images/table_selection_mobile.png)
   * Table Selection on Mobile

* Log In :
   * When a first time user clicks on the bookings page, they are requested to Log In or Sign Up
![Steakery Booking Login](media/readme_images/bookings_desktop.png)
   * Booking Login on Desktop
![Steakery Booking Login](media/readme_images/bookings_mobile.png)
   * Booking Login on Mobile


* Sign Up:
   * When signing up, users are asked for a Username and a strong password, and to confirm the password.
![Steakery Signup](media/readme_images/signup_desktop.png)
   * Signup Page on Desktop
![Steakery Signup](media/readme_images/signup_mobile.png)
   * Signup Page on Mobile


* Special Requests:
   * When smaking a booking, users can add special requests which are visible to both users and admin when logged in.
![Steakery Special Requests](media/readme_images/special_requests_desktop.png)
   * Special Requests on Desktop
![Steakery Special Requests](media/readme_images/special_requests_mobile.png)
   * Special Requests on Mobile

* Mobile Toggler:
   * When browsing the site, mobile users now have the option of a toggler to allow mobile users to navigate the site properly.
![Steakery Mobile Toggler](media/readme_images/toggler.png)
   * Mobile Toggler

### Admin Features

* Django's built-in admin panel provides full control over the website's data and content.
* Admins can access the admin panel through the navigation bar.
* Admin capabilities include adding, updating, and deleting table reservations and managing restaurant tables.
* Admins can create and manage special requests (e.g., dietary preferences, accessibility needs) linked to bookings.
* Admins can also manage user accounts, delete user data, and view or delete bookings.


### Features To Implement In Future:
* User Reviews: Allow users to leave reviews of The Steakery
* Menu Updates: Allow Admin Users to modify the Menu, Prices etc.

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
* [VS Code](https://code.visualstudio.com/) - Local IDE used to write and develop the code.
* [GitPod](https://www.gitpod.io/) - Cloud-based IDE used to write and develop the code.
* [Heroku](https://www.heroku.com/) - Used to deploy the site as a cloud-based platform.
* [Google Fonts](https://fonts.google.com/) - Used to import the main fonts for the website.
* [Balsamiq](https://balsamiq.com/wireframes/) - Utilized to create wireframes during the planning phase.
* [Mermaid Live](https://mermaid.live/edit) - Used to create the Entity Relationship Diagram (ERD).
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

## Testing

Thorough testing was conducted throughout the development of **The Steakery** to ensure the functionality, usability, and responsiveness of the website across different platforms and devices. The following is a summary of the testing procedures and results:

### Manual Testing

#### 1. **Navigation Bar**
   - **Test**: Ensure that all navigation links work as expected.
   - **Result**: All links navigate to the correct pages (Home, Menu, About, Contact, Bookings).
   - **Devices Tested**: Desktop, Mobile, Tablet.
   - **Browsers Tested**: Chrome, Firefox, Safari.

#### 2. **User Registration & Authentication**
   - **Test**: Users should be able to register, log in, and log out successfully.
   - **Result**: 
     - Registration form properly validates inputs.
     - Users are redirected to the home page after registration or login.
     - Logout functionality works as expected.
   - **Browsers Tested**: Chrome, Firefox, Safari.

#### 3. **Booking Creation**
   - **Test**: Users should be able to create a booking.
   - **Result**: The booking form works, data is saved correctly, and the booking appears in the user’s booking list.
   - **Special Test**: Ensured that the booking date cannot be in the past.
   - **Edge Cases**: Tested with various table capacities to ensure users can't book for more guests than a table can accommodate.

#### 4. **Booking List and Edit/Delete**
   - **Test**: Users should see their bookings and be able to edit or delete them.
   - **Result**: Bookings are displayed in a list with options to edit or delete. Both actions function as expected.
   - **Edge Cases**: Ensured users cannot book overlapping times for the same table.

#### 5. **Form Validation**
   - **Test**: Ensure form validation is functioning properly.
   - **Result**: Forms display appropriate error messages for invalid inputs (e.g., missing required fields, invalid email format, past dates for bookings).
   - **Browsers Tested**: Chrome, Firefox.

#### 6. **Responsiveness**
   - **Test**: Ensure the website is responsive across all device types.
   - **Result**: The layout adjusts properly on mobile devices, tablets, and desktops.
   - **Tools Used**: Chrome DevTools, Responsinator.


### Automated Testing

#### 1. **Django Unit Tests**
   - **Test**: Models and views have been tested using Django's built-in test framework.
   - **Result**: All unit tests pass, ensuring that the models (User, Booking, Table) and views function as expected.

#### 2. **W3C HTML Validator**
   - **Test**: Ensure HTML validation passes without significant issues.
   - **Result**: Minor warnings resolved, no critical errors found.

#### 3. **CSS Validation**
   - **Test**: CSS was validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).
   - **Result**: No significant errors found.

#### 4. **JavaScript Validation**
   - **Test**: JavaScript was validated using JSHint.
   - **Result**: JavaScript passed validation with no critical issues.

### Issues Discovered and Fixed

- **Booking form allowing past dates**: Implemented validation to prevent past dates from being booked.
- **Overlapping bookings**: Added logic to check for table availability and prevent double booking for the same time and table.
- **Broken links in the navigation bar**: Identified and fixed paths for several internal links.
- **CSS rendering issues in production**: Ensured that the static files are correctly handled in the production environment by adjusting `STATIC_URL` and `STATIC_ROOT` settings in `settings.py`.
- **Bookings out of opening hours**: Identified an error where users could book outside of opening hours and implemented validation to prevent this happening.
- **Special Requests**: Identified an issue where special requests from users were not logging correctly.
Implemented a fix for this so that users can view, edit or delete their special requests on bookings.
- **CRUD Functionality Issues**: Discovered CRUD wasn't fully operational for users, this has been fixed.
### Lighthouse Testing

Lighthouse, a popular open-source tool for auditing web performance, accessibility, SEO, and best practices, was used to evaluate **The Steakery**.

#### Key Metrics Assessed:
1. **Performance**: Evaluated the website's loading time and overall speed.
2. **Accessibility**: Tested for screen reader compatibility and ease of navigation for users with disabilities.
3. **SEO**: Ensured that the website follows best practices for search engine optimization.
4. **Best Practices**: Assessed compliance with web development best practices, including security and performance optimizations.

#### Results:
- **Performance**: Scored between 85-90, depending on network speed.
- **Accessibility**: Scored a strong 95
- **SEO**: Scored 100, ensuring that metadata, structured data, and crawlability are optimal.
- **Best Practices**: Scored 100, ensuring no critical security or performance issues.

Recommendations provided by Lighthouse (such as image optimizations and lazy loading) were addressed where possible to further improve performance and accessibility.

### CI Python Linter

The project was also checked using the **Code Institute Python Linter** to ensure adherence to PEP8 standards and best practices in Python coding.

#### Results:

- No critical issues were found during the Python code validation.
- Minor suggestions for improvements were addressed, such as the addition of docstrings to functions and ensuring proper indentation.
- The code is fully compliant with PEP8 standards, ensuring readability, maintainability, and reduced likelihood of bugs.

### Testing Summary

All critical functions were tested, and issues were addressed during the development process. The site performs well across devices and browsers, with form validation and responsive design functioning as expected. Where possible, edge cases were tested to ensure robustness and usability.

# References

### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [Google](https://www.google.com/)
* [W3 Schools](https://www.w3schools.com/)



### Code & Content 
* Code from [Oasis Hotels](https://github.com/Marchopkins96/oasis-hotels/tree/main) was used and modified for this project.
* Images were created using Adobe Express and Adobe Stock.



### Acknowledgements

* I would like to thank my mentor Dan Hamilton, for the continued support and feedback on the project. 
* I would also like to express my gratitude to my nephew Daniel for his valuable contributions to the development of The Steakery concept. 
* I would like to thank Code Institute community and team for their help whenever needed.

