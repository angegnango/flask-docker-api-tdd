
# Docker Flask 

Service built in top of [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [Flask](http://flask.pocoo.org/) application & a 

### Installation

```bash
git clone https://github.com/angegnango/flask-docker-api-tdd
```

### Build & Launch

```bash
docker-compose up
```

This will expose the Flask application's endpoints on port `http://0.0.0.0:3000` 

### Network coverage Endpoint

.\
to search a network coverage you have to hit the endpoint `http://0.0.0.0:3000/api/v1/search?q={your+query+string+here}`




To shut down:

```bash
docker-compose down
```


To change the endpoints, update the code in [api/server.py](api/server.py)


---

