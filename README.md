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

- `/api/recipes/`: 
  - **GET**: Retrieve a list of all recipes.
  - **POST**: Create a new recipe.
- `/api/recipes/<id>/`: 
  - **GET**: Retrieve details of a specific recipe.
  - **PUT**: Update a specific recipe.
  - **DELETE**: Delete a specific recipe.
- `/api/tags/`: 
  - **GET**: Retrieve a list of all tags.
  - **POST**: Create a new tag.

## Testing
### Running Unit Tests
Run the unit tests using the following command:

    docker-compose run --rm app sh -c "python manage.py test"

### Code Linting
Lint the code using Flake8:

    docker-compose run --rm app sh -c "flake8"
  



