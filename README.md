
---

# Running the Django App

Follow these steps to set up and run your Django application. Ensure you have Python, Docker, and RabbitMQ installed on your system.

## Prerequisites

- Python (version 3.x)
- Docker (latest version)
- RabbitMQ (version 3.13.1-management)

## Installation

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

3. **Run RabbitMQ**:
    Open a new terminal and start the RabbitMQ container:
    ```bash
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management
    ```

4. **Start Celery worker**:
    Open another terminal and start the Celery worker:
    ```bash
    celery -A todo worker -l info
    ```

5. **Run the Django application**:
    ```bash
    python manage.py runserver
    ```

6. **Run unit tests**:
    Ensure the Celery worker is running and then execute the unit tests:
    ```bash
    python manage.py test
    ```

## Notes

- **Check the console for emails**: The application logs email information to the console for testing purposes. Ensure to monitor the console output for any email-related logs.

---

Copy and paste the above instructions into your `README.md` file to provide a clear and professional setup guide for your Django application.
