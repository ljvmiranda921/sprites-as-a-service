# Sprite-as-a-Service Backend

This folder contains the backend component of Sprite-as-a-Service. In order to
set-up your development environment *just* for this part, run the following
commands:

```sh
git clone git@github.com:ljvmiranda921/sprite-as-a-service.git
cd backend
make dev
```

This creates a development environment consisting of a virtualenv, and it
installs all dependencies found in `requirements-dev.txt`. This then allows you
to run the tests in your local machine:

```sh
cd backend/
make test
```

## Running the application

Before running your application, please ensure that you have the virtualenv
activated:

```sh
source venv/bin/activate
```

You can confirm it by running `which python3`, and it must show the path
to your project directory, rather than the system-installed Python. Now, to run
the application, execute the following command:

```sh
uvicorn sprites.main:app --reload
```

## Running the Docker images

You can also build and run the application within a Docker image. First, build
the image by running the following command:

```sh
docker build -t sprite-backend:dev .
```

Once the image has been built, you can run the application via:

```sh
docker run -d -p 8080:8080 sprite-backend:dev
```
