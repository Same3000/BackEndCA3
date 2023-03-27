# Webnovel Retail App
This is a Django web application that allows users to browse and purchase webnovels. It includes CRUD functionality for managing novels and authors, as well as a login system to protect certain areas of the site.

# Requirements

To run this project, you will need to have the following software installed on your system:
```
Python 3
Django 3.2
```
# Installation
* Clone this repository to your local machine.
* Navigate to the project directory.
* Install the required Python packages using pip:
* Run the Django development server:
```
python manage.py runserver
```
Open your web browser and navigate to [localhost](http://localhost:8000/) to view the app.
# Usage
## Authentication
The app includes a login system that allows users to create an account, log in, and log out. Certain areas of the site are protected and can only be accessed by authenticated users.

## WebNovel Management
The app allows authenticated users to create, read, update, and delete novels and their corresponding authors or tags. To manage WebNovels, navigate to the /webnovels URL.

## Author and Tag Management
The app allows authenticated users to create, read, update, and delete authors. To manage authors or tags, go to the corresponding urls to fill the forms and create them.

# Tests
Testing is an important aspect of software development that helps ensure the reliability and stability of our application. In this Django project, we have added comprehensive automated tests to cover various aspects of our application, including unit tests and integration tests. These tests are located in the "tests" directory and can be run using the command 

```python manage.py test WebNovels```

## <ins> Testing Forms, Views, and Models: </ins>

This Django project includes automated tests for the forms, views, and models used in the application. These tests help ensure that the application behaves correctly and responds appropriately to user input and system events.

### Testing Forms
Forms are an essential part of any web application, and it's essential to ensure that they work correctly. The tests for forms are located in the "tests/test_forms". These tests check whether the forms can validate and handle various types of user input, such as invalid or missing data, and they ensure that the form's behavior is consistent with the application's requirements.

### Testing Views
Views are responsible for handling user requests and returning responses. The tests for views are located in the "tests/test_views". These tests verify that the views are returning the correct HTTP response status codes, handling invalid input data appropriately, and rendering the correct templates.

### Testing Models
Models are the backbone of the application's data management. The tests for models are located in the "tests/tests_models". These tests verify the behavior of the models, including whether they can be created, updated, and deleted correctly, and whether they correctly validate input data and enforce constraints.

### Conclusion

Writing automated tests is an essential part of ensuring the reliability and stability of your Django application. By testing your forms, views, and models, you can ensure that your application is functioning as intended, even as it evolves and changes over time. We encourage all developers to write tests for any new features or changes they make to the codebase to maintain the high quality of our application.

# Credits
This app was created by Same3000. If you have any questions or feedback, please contact me at samy.yacef@epita.fr

# License
This project is licensed under the MIT License. See the LICENSE file for details.
