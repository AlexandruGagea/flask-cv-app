# Flask CV App – Alexandru Gagea

This project is a Flask-based web application that exposes CV data through:
- A JSON REST API
- A Flask CLI command

Everything runs inside Docker — no need to install Python or Flask on your machine.

---

##  Requirements

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose v2+](https://docs.docker.com/compose/)

>  Confirm by running:

docker compose version

### 1. Clone the repository or download manually

git clone https://github.com/YOUR_USERNAME/flask-cv-app.git
cd flask-cv-app

### 2. Build and run the application

docker compose up

### 3. Access the application

Open your browser and navigate to :

http://localhost:5000/personal
http://localhost:5000/education
http://localhost:5000/experience

### 4. Use the CLI command

Run the following command:

docker compose run flask_cv flask print-cv






