---

# Running the Django App

Follow these steps to set up and run your Django application. Ensure you have Python amd Docker nstalled on your system.

## Prerequisites

- Python (version 3.12.4)
- Docker (version 26.0.0)


## Installation

1. **Create and activate a virtual environment with Python 3.12.4**:
    ```bash
    python3.12 -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Run the Django application**:
    ```bash
    python manage.py runserver
    ```

5. **Run RabbitMQ**:
    Open a new terminal and start the RabbitMQ container:
    ```bash
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management
    ```

6. **Start Celery worker**:
    Open another terminal and start the Celery worker:
    ```bash
    celery -A todo worker -l info
    ```

7. **Run unit tests**:
    Ensure the Celery worker is running and then execute the unit tests:
    ```bash
    python manage.py test
    ```

## Notes

- **Check the console for emails**: The application logs email information to the console for testing purposes. Ensure to monitor the console output for any email-related logs.

## Task Management API cURL Commands

These commands allow you to interact with your Django REST API for task management using the command line. Replace `http://localhost:8000` with the actual URL of your Django application and adjust the request data as needed for your specific API endpoints and models.

### 1. List all tasks
```bash
curl http://localhost:8000/api/tasks/
```

### 2. Create a new task
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"New Task","description":"This is a new task","due_date":"2023-06-30","status":"TO_DO","profile_id":1}' http://localhost:8000/api/tasks/
```

### 3. Retrieve a specific task
```bash
curl http://localhost:8000/api/tasks/1/
```

### 4. Update a specific task
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Task","description":"This task has been updated","due_date":"2023-07-15","status":"IN_PROGRESS","profile_id":1}' http://localhost:8000/api/tasks/1/
```

### 5. Delete a specific task
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/
```

---


