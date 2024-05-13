# Recipe App API
Course code for: Build a Backend REST API with Python &amp; Django - Advanced: Take the course here: https://londonapp.dev/c2

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Django](https://img.shields.io/badge/Django-3.2-green)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-3.12-red)
![Flake8](https://img.shields.io/badge/Flake8-lint-orange)
![Docker](https://img.shields.io/badge/Docker-20.10-orange)

This is a RESTful API built with Django and Django REST Framework for managing recipes. Users can register, login, and manage their recipes with ease. The API allows for tagging recipes, filtering recipes based on various criteria, and uploading images for each recipe.

## Features

- **User Authentication:** Users can register, login, and manage their accounts securely.
- **Recipe Management:** Create, read, update, and delete recipes.
- **Tagging:** Assign tags to recipes for categorization and easy retrieval.
- **Filtering and Searching:** Filter recipes by ingredients, tags, or other criteria.
- **Image Uploading:** Upload images for each recipe to provide visual representation.

## Installation

### Prerequisites

- Docker installed on your system.

### Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/NohaGad/recipe-app-api.git

2. Navigate to the project directory:

    ```bash
    cd recipe-app-api

3. Build the Docker image:

   ```bash
   docker-compose build

4. Run the Docker container:
   
   ```bash
   docker-compose up -d

5. Access the API at `http://localhost:8000/api/`.

## Usage
### Authentication
To access protected endpoints, users need to obtain an access token by sending a POST request to the /api/token/ endpoint with valid credentials. Use the obtained token in the Authorization header for subsequent requests.

### Endpoints

- `/api/user/`
- `/api/user/token/`
- `/api/recipe/recipe/`
- `/api/recipe/recipe/{id}/`
- `/api/recipe/ingredient/`
- `/api/recipe/ingredient/{id}/`
- `/api/recipe/recipe/{id}/upload-image/`
- `/api/recipe/tag/`
- `/api/recipe/tag/{id}/`

## Testing
### Running Unit Tests
Run the unit tests using the following command:

    docker-compose run --rm app sh -c "python manage.py test"

### Code Linting
Lint the code using Flake8:

    docker-compose run --rm app sh -c "flake8"
  
## Deployment
This project has been deployed on an AWS EC2 instance. Here are some screenshots:
<img width="1008" alt="Screenshot 2024-04-23 at 21 38 34" src="https://github.com/NohaGad/recipe-app-api/assets/37811490/9080b9c3-5e98-48aa-b298-2d33d9f3401d">
<img width="1008" alt="Screenshot 2024-04-23 at 21 38 46" src="https://github.com/NohaGad/recipe-app-api/assets/37811490/d8f7170a-ab26-4f54-a77a-50817d2bdd15">






