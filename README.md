# VMS - (Backend)

VMS (Visitor Management System) is a web application designed to facilitate visitor registration and management for buildings. It allows visitors to be registered at the entrance, capturing their information along with their check-in and check-out times using timestamps. Additionally, it provides employee details and features a dashboard that tracks visitor and employee activity.

## Table of Contents
- [Features](#features)
- [Prerequistics](#prerequisites)
- [Installation](#installation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Technologies Used](#technologies-used)
- [Author](#author)

## Features
VMS offers the following features:

- Visitor registration and check-in/check-out functionality.
- Detailed visitor information capturing including name, contact details, purpose of visit, and more.
- Employee directory.
- Dashboard for tracking visitor and employee activity.
- Filtering visitors by date.
- Authentication using JWT tokens.
- Change password functionality.
- Email notifications using SMTP.

## Prerequisites
Before running the application, make sure you have the following installed:

- Python (3.7 or higher)
- Django (3.0 or higher)
- Django REST Framework

## Installation
1. Clone the repository to your local machine:`git clone https://github.com/muthuieric/vms-backend`
2. Navigate to the project directory:`cd backend`
3. Install the required dependencies:`pip install -r requirements.txt`
4. Apply migrations:`python manage.py migrate`
5. Start the Django development server:`python manage.py runserver`
This will launch the application at `http://localhost:8000`.

## Deployment
The application can be manually deployed by hosting the Django project on a web server.

Manual Deployment
To start the Django development server:

python manage.py runserver
This will launch the application at `http://localhost:8000`.

For production deployment, you can use services like AWS, Heroku, or DigitalOcean.

## Contributing
Contributions to VMS are welcome. If you find any issues or have improvements to suggest, feel free to create a pull request or open an issue in the repository.

## Technologies Used
- Django
- Django REST Framework


## Author
Author: `Eric Muthui`

Thank you for exploring the VMS repository!