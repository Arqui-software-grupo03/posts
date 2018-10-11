to run:

    docker-compose build && docker-compose up

    docker exec -it appPosts ./manage.py makemigrations posts

    docker exec -it appPosts ./manage.py migrate

    docker exec -it appPosts python ./manage.py runserver 0.0.0.0:8000

    try it:
        http://localhost:8000/admin