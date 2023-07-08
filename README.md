# Lab - Class 32

## Project: Villains API - DRF Permissions & Postgres

---

### Author: Mohamad Shareef Naser

---

### Links and Resources

- [Pull Request](https://github.com/mshnas9/drf-api-permissions-postgres/pull/1)

### Setup

To run this Django project, make sure you have Python 3 installed. If you don't, you can follow the instructions [here](https://wsvincent.com/install-python/#install-python-on-linux) to install Python 3.

### Initialize the Application

1. Navigate to the project directory in your terminal.
2. Activate the virtual environment by running the following command:
   ```bash
   source .venv/bin/activate
   ```
3. Apply the database migrations by running the following command:
   ```bash
   python manage.py migrate
   ```
4. Start the Django development server by running the following command:
   ```bash
   python manage.py runserver
   ```
   This will start the server at `http://127.0.0.1:8000/`.

### Running with Docker

To run the project using Docker, make sure you have Docker and Docker Compose installed on your machine. If not, you can refer to the Docker documentation for installation instructions.

1. Navigate to the project directory in your terminal.
2. Build the Docker image by running the following command:
   ```bash
   docker-compose build
   ```
3. Start the Docker containers by running the following command:
   ```bash
   docker-compose up
   ```
   This will start the Django server and the PostgreSQL database container.
4. Access the application in your web browser at `http://localhost:8000`.

### Tests

To run the tests for this Django project, follow these steps:

1. Activate the virtual environment if it's not already activated by running:
   ```bash
   source .venv/bin/activate
   ```
2. Ensure you are in the root directory of your Django project.
3. Run the tests using the following command:
   ```bash
   python manage.py test
   ```