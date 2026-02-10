This project showcases end-to-end DevOps practices by building an automated deployment pipeline for a Flask To-Do API application. It demonstrates containerization with Docker, infrastructure provisioning with Terraform, and continuous integration/deployment using GitHub Actions.

## Project Objectives

- Build a REST API using Flask (Python)
- Containerize the application using Docker
- Implement Infrastructure as Code using Terraform
- Set up CI/CD pipeline with GitHub Actions
- Deploy to cloud infrastructure (AWS/Oracle Cloud)
- Implement multi-environment deployment (Staging & Production)

## 🛠️ Technologies Used

- **Programming Language:** Python 3.9
- **Web Framework:** Flask
- **Containerization:** Docker
- **Infrastructure as Code:** Terraform
- **CI/CD:** GitHub Actions
- **Cloud Platform:** AWS / Oracle Cloud
- **Version Control:** Git & GitHub
- **Testing:** pytest

## Project Structuredevops-flask-project/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── .dockerignore         # Docker build exclusions
├── .gitignore           # Git exclusions
└── README.md            # Project documentation

## Features

### API Endpoints

- `GET /` - Health check endpoint
- `GET /health` - Application health status
- `GET /todos` - Retrieve all todos
- `POST /todos` - Create a new todo
- `DELETE /todos/<id>` - Delete a specific todo

### Example API Usage
```bashGet all todos
curl http://localhost:5001/todosAdd a new todo
curl -X POST http://localhost:5001/todos 
-H "Content-Type: application/json" 
-d '{"task": "Learn DevOps"}'Delete a todo
curl -X DELETE http://localhost:5001/todos/1

## Local Development Setup

### Prerequisites

- Python 3.9+
- Docker Desktop
- Git

### Installation Steps

1. **Clone the repository**
```bashgit clone https://github.com/pavansai17/devops-flask-cicd.git
cd devops-flask-cicd

2. **Create virtual environment**
```bashpython3 -m venv venv
source venv/bin/activate  # On Mac/Linux

3. **Install dependencies**
```bashpip install -r requirements.txt

4. **Run the application**
```bashpython app.py

5. **Access the API**http://localhost:5001

## Docker Usage

### Build Docker Image
```bashdocker build -t flask-todo-app .

### Run Docker Container
```bashdocker run -p 5001:5001 flask-todo-app

### Access Containerized Applicationhttp://localhost:5001

## Infrastructure as Code (Coming Soon)

The project will include Terraform configurations to provision:
- EC2 instances for staging and production environments
- Security groups and networking
- Load balancers
- Automated infrastructure deployment

## CI/CD Pipeline (Coming Soon)

GitHub Actions workflow will automate:
- Code testing on every push
- Docker image building
- Pushing images to Docker Hub
- Automated deployment to staging environment
- Manual approval for production deployment

## DevOps WorkflowCode Commit → GitHub Actions Trigger → Run Tests → Build Docker Image
→ Push to Registry → Deploy to Staging → Manual Approval → Deploy to Production

## Learning Outcomes

This project demonstrates proficiency in:
- REST API development with Flask
- Docker containerization best practices
- Infrastructure automation with Terraform
- CI/CD pipeline implementation
- Git version control and branching strategies
- Cloud deployment and management
- DevOps principles and practices

## Security Best Practices

- Environment variables for sensitive data
- .gitignore for credentials
- Docker image security scanning
- IAM roles and permissions management
- Network security groups configuration


- [ ] Add monitoring with Prometheus and Grafana
- [ ] Implement logging with ELK stack
- [ ] Add database persistence (Postgre Sonnet 4.5
