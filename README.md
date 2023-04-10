# Project - "Cyclic Code Encoder"

## Team: CoDe-N-CoDeRs
- Rajat Singh (2003130) <br>
- Raj Hans Khoiwal (2003129) <br>
- Divyanshi Govil (2003115)

## Course Instructor 
- Dr. Rahul CS

## Course
- CS425 Algebrain Coding Theory and Cryptography

## Tech Stack
1. `Django` - a python web framework that provides a robust set of tools and libraries for building web applications.
2. `Python` - a popular programming language known for its simplicity and versatility.
3. `HTML` - the standard markup language for creating web pages.
4. `CSS` - a stylesheet language used for styling web pages.

## Project Files
1. `settings.py` - configuration file that contains various settings for a Django project.
2. `urls.py` - serves as a central routing configuration file for URL handling in a Django web application.
3. `wsgi.py` - acts as a communication bridge between a web server and a Django application.
4. `manage.py` - a command-line utility that provides a convenient way to manage various aspects of a Django project
5. `views.py` - handles the main back-end component of the project i.e. does the computations.
6. `input.html` - default webpage of the project, accepts user inputs.
7. `output.html` - outputs the encoded message using Cyclic Codes

## About
The Cyclic Code Encoder is a web application built using Django, a Python web framework. <br>
It provides a simple frontend interface for users to input data and encode it using *[n, k]<sub>q</sub>* cyclic codes using a randomly generated Generator Polynomial. <br>
The backend of the application utilizes Django's redirect view to allow users to redirect to a specified URL by clicking on a "Encode" button. <br>
It serves as a basic example of how to implement Cyclic Code Encoder with a GUI using a web application with Django.

## Run
1. Install [*python3*](https://www.python.org/downloads/)

2. Create a virtual environment 
`python -m venv env`

3. Activate the virtual environment
`source env/bin/activate`

4. Install Django using pip
`pip install django`

5. Clone the github repository
`git clone https://github.com/RajatSingh08/Cyclic-Code-Encoder`

6. Open the project folder
`cd Cyclic-Code-Encoder/CyclicCodeEncoder/`

7. Run the following command 
`python manage.py runserver`

8. Open a web browser and search the following url
`http://127.0.0.1:8000/`

9. Input the values of *n, **k, **q, **data* and click "*ENCODE*"

10. To encode new data, click "*GO BACK*" 

## Screenshots
![enter image description here](https://raw.githubusercontent.com/RajatSingh08/Cyclic-Code-Encoder/main/screenshots/input.png)

![](https://raw.githubusercontent.com/RajatSingh08/Cyclic-Code-Encoder/main/screenshots/encode.png)

![](https://raw.githubusercontent.com/RajatSingh08/Cyclic-Code-Encoder/main/screenshots/output.png)
