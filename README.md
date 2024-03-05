# Dockerize Flask
This Repo dockerize Flask framwork of Python, alongside with Mysql

## Initilize
First docker up to create images and containers
```
docker compose up -d
```

Then check whether python and mysql container is up

## First Database migration
Go inside python container
```
docker compose exec -it python bash
```

Then execute these command to migrate DBs
```
flask db stamp head
flask db migrate
flask db upgrade
```