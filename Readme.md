

## Step1: 
- clone the mongodb repo from https://github.com/Arqui-software-grupo03/mongodb.git
- `cd mongodb`
- `docker-compose up`

## Step 2
- Open a new terminal
- go to the users repo 
- `cd posts`
- `docker-compose build` && `docker-compose up`
- `docker exec -it appPosts ./manage.py migrate`
- `docker exec -it appPosts python ./manage.py runserver 0.0.0.0:8100`
- try it:
        http://localhost:8100/admin
