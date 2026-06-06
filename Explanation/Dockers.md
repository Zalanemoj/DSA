\# Dockers important Commands



\### Commands

1. docker build -t my-app .
2. docker
3. docker pull name
4. docker push name
5. docker run -p port mapping name
6. docker ps ----> List running containers
7. docker tag myapp:latest myrepo/myapp:v1 ---->Re-tag an image
8. docker rmi myapp:latest ---->Remove an image



\### Docker file creation instruction

1. From Base image ---->python:3.12-slim
2. WORKDIR ---->/app
3. COPY ----> ./app/
4. EXPOSE port to expose ---->8000
5. RUN pip install -r requirements.txt
6. CMD \["python", "./app.py"]

