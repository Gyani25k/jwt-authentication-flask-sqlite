# jwt-authentication-flask-sqlite
A simple Flask application providing JWT authentication with sign-in and sign-up APIs, using SQLite for data storage.

# JWT Authentication Flask SQLite

This is a simple Flask application that provides JWT authentication along with sign-in and sign-up APIs, using SQLite for data storage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gyani25k/jwt-authentication-flask-sqlite.git
   cd jwt-authentication-flask-sqlite
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-JWT-Extended
   ```

## Usage

Run the application:
```bash
python app.py
```

## API Endpoints

- **POST** `/signup`: Register a new user.
- **POST** `/signin`: Authenticate existing user and retrieve a JWT.

## Requirements
- Python 3.6+
- Flask 2.0+
- Flask-SQLAlchemy
- Flask-JWT-Extended

## License
This project is licensed under the MIT License.
## How to Run

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Use tools like Postman or curl to interact with the API endpoints.

## API Endpoints

- **POST** `/signup`: Register a new user. Pass JSON body with `username` and `password`.
- **POST** `/signin`: Authenticate existing user and retrieve a JWT. Pass JSON body with `username` and `password`.
- **GET** `/protected`: Protected route requires a valid JWT. Use the token in the Authorization header as `Bearer <your_token>`.
## How to Run

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Use tools like Postman or curl to interact with the API endpoints.

## API Endpoints

- **POST** `/signup`: Register a new user. Pass JSON body with `username` and `password`.
- **POST** `/signin`: Authenticate existing user and retrieve a JWT. Pass JSON body with `username` and `password`.
- **GET** `/protected`: Protected route requires a valid JWT. Use the token in the Authorization header as `Bearer <your_token>`.