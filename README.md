# golf_score_tracker
Golf Score Tracker is a project to help me learn several technologies that I want to become proficient with as I transition to the next phase of my career. The primary technologies I want to learn and utilize in this project are:
- Python
    - Coding best practices
    - Command-line input/output
    - UX Design
    - Data Visualization and Analysis
    - Package design
    - Test coverage
- GitHub
    - Version control
    - Source control
    - Continuous Integration and Delivery
- Data storage
    - `json` documents 
        - Local Storage
        - MongoDB
    - On-prem RDBMS (SQL Server, Oracle, PostgreSQL)
    - Cloud RDBMS (Azure SQL DB, Snowflake, MongoDB)
- Azure Application Services
    - Hosting as web application

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Data Model](#data_model)

## Features
The features will evolve over time, but the Version 1.0 functionality will include:
- Command line interface with Menu system
- Create/Edit golf courses (from file and user input)
- Create/Edit golf scores (from file and user input)
- Display golf course information
- Display scores
- Data storage in `json` files on file system

Future version functionality of the application will include:
- GUI-based 
- Data storage in local database and in cloud
- Basic data analysis
    - Scoring average (overall, by course)
        - Total strokes, putts
    - Scoring average (by hole type, overall and by course)
    - Tee accuracy
    - Greens in regulation
- Ability to track multiple golfers

Future version design of the application will incorporate:
- Continuous Integration and Delivery
- Hosting in Azure App Services

## Usage
Initially the application will run with a command line based menu system. Over time, it will evolve into a GUI-based system. 

## Data Model
I will focus on utilizing `json` format. I will utilize schema.json files for the course and score data:
- [course.schema.json](/src/golf_score_tracker/data/courses/course.schema.json)
- [score.schema.json](/src/golf_score_tracker/data/scores/score.schema.json)

