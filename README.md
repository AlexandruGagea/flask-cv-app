# Flask CV App – Alexandru Gagea

A containerized Flask web application that exposes CV data through multiple interfaces:
- **REST API** with JSON responses
- **CLI commands** for terminal access
- **Interactive Swagger documentation**

Built with Docker for easy deployment and development.

---

##  Quick Start

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose v2+](https://docs.docker.com/compose/)

Verify installation:
```bash
docker compose version
```

### Setup & Launch

1. **Clone the repository**
   ```bash
   git clone https://github.com/AlexandruGagea/flask-cv-app.git
   cd flask-cv-app
   ```

2. **Build and run**
   ```bash
   docker compose build
   docker compose up
   ```

3. **Verify it's running**
   
   The application will be available at `http://localhost:5000`

---

##  Accessing CV Data

All API endpoints require authentication using the token: `supersecrettoken123`

###  Web Browser
Direct browser access to JSON endpoints:

- **Personal Info**: http://localhost:5000/personal?token=supersecrettoken123
- **Education**: http://localhost:5000/education?token=supersecrettoken123
- **Experience**: http://localhost:5000/experience?token=supersecrettoken123

###  Interactive Documentation
Explore the API with Swagger UI:

**http://localhost:5000/apidocs**

###  Command Line (cURL)
Quick API testing from terminal:

```bash
# Personal information
curl "http://localhost:5000/personal?token=supersecrettoken123"

# Education history
curl "http://localhost:5000/education?token=supersecrettoken123"

# Work experience
curl "http://localhost:5000/experience?token=supersecrettoken123"

# Using Bearer token in header (alternative)
curl -H "Authorization: Bearer supersecrettoken123" http://localhost:5000/personal
```

###  CLI Commands
Access CV data through Flask CLI:

```bash
# Print complete CV to terminal
docker compose run flask_cv flask print-cv
```

###  Postman Collection
Import the provided collection for easy API testing:

**File**: `Flask_CV_APP.postman_collection.json`

---

##  Testing

### Run Tests
Execute the complete test suite:

```bash
# Run all tests
docker compose exec flask_cv pytest

# Run tests with verbose output
docker compose exec flask_cv pytest -v

```

### Test Categories
- **Unit Tests**: Individual component testing
- **API Tests**: Endpoint functionality and security
- **CLI Tests**: Command-line interface testing
- **Integration Tests**: Full workflow testing
- **Security Tests**: Authentication and input validation

---

##  Authentication

The application uses simple token-based authentication:

- **Token**: `supersecrettoken123`
- **Methods**: 
  - Query parameter: `?token=supersecrettoken123`
  - Authorization header: `Authorization: Bearer supersecrettoken123`

### Security Features
- All endpoints require authentication
- Invalid tokens return 401 Unauthorized
- Case-sensitive token validation
- Input validation for security

---

##  Project Structure

```
flask-cv-app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # API endpoints
│   ├── cli.py               # CLI commands
│   ├── cv_data.py           # CV data structure
│   ├── auth.py              # Authentication logic
│   └── utils.py             # Utility functions
├── tests/
│   ├── conftest.py          # Test configuration
│   ├── test_app.py          # Main test suite
│   └── test_security.py     # Security tests
├── docs/                    # Swagger documentation
├── docker-compose.yml       # Docker services
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
└── Makefile               # Development commands
```

---

##  Development

### Docker Commands
```bash
# View logs
docker compose logs flask_cv

# Access container shell
docker compose exec flask_cv bash

# Rebuild after changes
docker compose up --build

# Stop services
docker compose down
```

---

##  API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/personal` | GET | Personal information | Required |
| `/education` | GET | Education history | Required |
| `/experience` | GET | Work experience | Required |
| `/apidocs` | GET | Swagger documentation | None |

### Response Format
All API responses return JSON with proper HTTP status codes:

- **200**: Success
- **401**: Unauthorized (missing/invalid token)
- **404**: Not Found
- **405**: Method Not Allowed

---

##  CI/CD

The project includes:
- **GitHub Actions** Github repo
- **Docker** containerization for consistent environments
- **Pytest** with comprehensive test coverage
- **Code quality** tools (linting, formatting)

---

##  Contact

**Alexandru Ionut Gagea**
- Email: alexandrugagea@gmail.com
- LinkedIn: [alexandru-gagea-0a3b6377](https://www.linkedin.com/in/alexandru-gagea-0a3b6377/)
- Phone: +40 737 512 634
- Location: Romania

---

*Built with Flask, Docker, and tested with Pyte