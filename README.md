<H1>Run Docker</H1>
<H3>Create a Docker Image:</H3>
docker build -t my-python-app .
<H3>Run the Container:</H3>
docker run -it my-python-app

<H1>Run Docker-compose</H1>
<H3>Building a Docker Image:</H3>
docker-compose build
<H3>Applying Migrations:</H3>
docker-compose exec app python manage.py migrate
<H3>Running Containers:</H3>
docker-compose up
