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
    curl http://localhost:8001/health
```
You can replace the 8001 with 8002 or 8003 to check the other endpoints' health. You should recieve something of the form

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

# Testing

# Project structure
