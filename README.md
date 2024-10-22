# Task Management System

This project implements a task management system that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users. The system is built using Django and Django Rest Framework (DRF), and the API can be tested directly through the browser.

## Features

1. **Create a Task**
   - Allows users to create a new task with a name and description.
   - Automatically sets the task status to "pending" upon creation.

2. **Assign Tasks to Users**
   - Assign a task to one or multiple users.
   - Handles invalid user IDs gracefully without failing the entire process.

3. **Retrieve Tasks Assigned to a Specific User**
   - Fetches and displays all tasks assigned to a particular user, including task details.

## Technical Details

- **Tech Stack**: Django Rest Framework (DRF)
- **Database**: SQLite (default), configurable for other databases like PostgreSQL

## API Endpoints and Example Payloads

### 1. **Create a Task**
   - **Endpoint**: `http://127.0.0.1:8000/api/tasks/create/`
   - **Method**: POST
   - **Description**: Create a new task with name and description.
   - **Example Payload**:
     ```json
     {
       "name": "Task Name",
       "description": "Task Description"
     }
     ```

### 2. **Assign Task to Users**
   - **Endpoint**: `http://127.0.0.1:8000/api/tasks/assign/<task_id>/`
   - **Method**: PATCH
   - **Description**: Assign an existing task to one or more users.
   - **Example Payload**:
     ```json
     {
       "user_ids": [1, 2, 3]
     }
     ```
   - **Example URL**: 
     ```
     http://127.0.0.1:8000/api/tasks/assign/1/
     ```

### 3. **Get Tasks Assigned to a Specific User**
   - **Endpoint**: `http://127.0.0.1:8000/api/tasks/user_tasks/<user_id>/`
   - **Method**: GET
   - **Description**: Retrieve all tasks assigned to a specific user, including task details.
   
   - **Example URL**: 
     ```
     http://127.0.0.1:8000/api/tasks/user_tasks/1/
     ```

     **Returns**: A list of tasks assigned to the user with detailed task information.

## Setup Instructions

### Steps to Set Up and Run the Project

1. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   python manage.py runserver
2. **Login steps**
   ```bash
   go to http://127.0.0.1:8000/admin/
   enter user name as hanuman
   password as 1234
