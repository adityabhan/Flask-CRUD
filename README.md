# Flask-CRUD
This is a basic Flask project that demonstrates CRUD (Create, Read, Update, Delete) operations on an SQLite database. The project utilizes Flask, a Python web framework, and SQLite, a lightweight database engine. It provides a simple API to perform CRUD operations on a database table.


# Prerequisites

Before running this project, make sure you have the following prerequisites installed:

Python 3.x
Flask
Flask Sqlalchemy

# Installation

Clone this repository to your local machine.

Install the required dependencies using pip:

pip install -r requirements.txt


# Usage

Use the following command to start flask server:

python app.py


Once the server is running, you can access the API endpoints using a tool like cURL or a web browser.

API Endpoints<br/>

GET /getAllStudents - Retrieve all students from the database.<br/>
GET /getStudentById?id={} - Retrieve a specific student by its ID.<br/>
GET /getStudentsByName - Retrieve a list of students by name.<br/>
GET /getStudentsByEnrollmentDate - Retrieve a list of students enrolled on or after a specific date. <br/>
POST /addNewStudent - Create a new student entry.<br/>
PUT /updateStudentName - Update an existing student name.<br/>
DELETE /deleteStudentById - Delete an item.<br/>


Refer images folder for more information on API calls.