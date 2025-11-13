# Project title: Game Lounge
- A web-hosted system for playing real-time multiplayer turn-based games

# Architecture overview
- This system consists of 3 services:
    1) User service: This service keeps track of user information, such as their favorite games, friends, and login information
    2) Chat service: A real-time messaging service that stores and facilitates communication between multiple users
    3) Game service: This service keeps track of game logic, game state, and saves information about past games for users to watch a replay of a game. This information includes who played and the moves they made each turn.

# Prerequisites
- The only prerequisite needed for this system is Docker (specifically, the ability to use Docker compose).

# Installation & Setup
- Download the entire repository from my GitHub page [here](https://github.com/ajyoung07/CS426-FinalProject). In your terminal, change into the directory where you downloaded the program. From there, run
```docker
    docker-compose up --build -d
```
and the system should be up and running on `http://localhost`. You should see some of the services mentioned in the previous sections show up when you type
```docker
    docker-compose ps
```
# Usage instructions
To check the health of an endpoint, simply use the command
```bash
    curl http://localhost:8080/{service-name}/health
```
Where `{service-name}` is either `user`, `chat`, or `game`. You should recieve something of the form

```json
    {
        "service": <NAME-OF-SERVICE>,
        "status": "healthy",
        "dependencies": {
            <DEPENDECY-NAME>: {
                "status": "healthy",
                "response_time_ms" <TIME_IN_MS>
            }
        }
    }
```
# API Documentation

We have the following endpoints:

- `user/health` will return
```json
    {
        "service": "user-service",
        "status": "healthy" | "unhealthy",
        "dependencies": {
            "redis": {
                "status": "healthy" | "unhealthy",
                "response_time_ms" <TIME_IN_MS>
            }
        }
    }
```
- `chat/health` will return
```json
    {
        "service": "chat-service",
        "status": "healthy" | "unhealthy",
        "dependencies": {
            "redis": {
                "status": "healthy" | "unhealthy",
                "response_time_ms" <TIME_IN_MS>
            },
            "user-service" : {
                "status": "healthy" | "unhealthy",
                "response_time_ms" <TIME_IN_MS>
            }
        }
    }
```
- `game/health` will return
```json
    {
        "service": "game-service",
        "status": "healthy" | "unhealthy",
        "dependencies": {
            "redis": {
                "status": "healthy" | "unhealthy",
                "response_time_ms" <TIME_IN_MS>
            },
            "user-service" : {
                "status": "healthy" | "unhealthy",
                "response_time_ms" <TIME_IN_MS>
            }
        }
    }
```

# Testing
To test the system, I would first try seeing that all services are up and running using `docker-compose ps`. Then, I would test the health endpoints documented above.
# Project structure
Here is the file-tree

```
.
├── architecture-diagram.png
├── chat-service
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
├── docker-compose.yml
├── game-service
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
├── nginx
│   └── nginx.conf
├── README.md
└── user-service
    ├── Dockerfile
    ├── main.py
    ├── models.py
    └── requirements.txt
```
Each directory ending in `-service` corresponds to one of the microservices. They each have a Dockerfile, which is what sets up each microservice, a `main.py` which is where each service's endpoint is set up, and a `models.py` which gives the validation models for what each endpoint recieves/sends.
