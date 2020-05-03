![](assets/header.png)

![Github Pages](https://github.com/ljvmiranda921/sprites-as-a-service/workflows/Github%20Pages/badge.svg)
![Frontend CI](https://github.com/ljvmiranda921/sprites-as-a-service/workflows/Frontend%20CI/badge.svg)
![Backend CI](https://github.com/ljvmiranda921/sprites-as-a-service/workflows/Backend%20CI/badge.svg)

**Try the interactive demo [here](ljvmiranda921.github.io/sprites-as-a-service)**

## Running the development server 

The easiest way to run Sprites-as-a-service locally is via [docker
compose](https://docs.docker.com/compose/). First, clone this repository:

```sh
git clone git@github.com:ljvmiranda921/sprites-as-a-service.git
```

then build the images:

```sh
cd sprites-as-a-service
docker-compose build
```

This will then build two images, `sprites-backend` and `sprites-frontend`, for
the backend and frontend services of the web app. You can then run them with
the command:

```sh
docker-compose -d up
```

You should be able to see the application running at
[localhost:8080](localhost:8080). Close these services using:

```sh
docker-compose down
```

## Production server and deployment

*In progress*

## License

The content of this project itself is licensed under the [Creative Commons
Attribution 4.0 license](https://creativecommons.org/licenses/by/4.0/deed.ast), and the underlying source code used to generate the
sprites and build the website is licensed under the [MIT license](https://github.com/ljvmiranda921/sprites-as-a-service/blob/master/LICENSE).
