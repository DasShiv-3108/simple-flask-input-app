# Simple Flask Input App

A minimal Flask web application designed for Docker practice.
This project demonstrates how a Flask app takes user input and runs inside a Docker container with proper port mapping.

This repository is intended for DevOps beginners and freshers who want hands-on Docker practice using a simple Python Flask application.

## Application Overview

- Single-page Flask web application
- Accepts text input from the user
- Displays submitted input on the same page
- Runs on port 5000
- Designed to run inside Docker

## Tech Stack

- Python
- Flask
- Docker

## Versions Used

This project is tested with the following versions:

- Python: 3.12
- Flask: 3.0.x
- Docker Engine: 24.x or later

Recommended Docker base image:
python:3.12-slim

## Port Configuration

- Flask application listens on port 5000 inside the container
- Port mapping is required to access the app from the host machine

Container Port: 5000  
Host Port: 5000

## Run the Application Using Docker

Dockerfile is intentionally written by the developer (learner).

Build Docker image:
```bash
docker build -t simple-flask-input-app .

add >docker-compose.yml< file then: 
docker compose up -d
