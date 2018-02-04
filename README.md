# Structlog + ELK stack

A proof of concept for logging structured from Python to an Elasticsearch + Logstash + Kibana environment using [Docker ELK](https://github.com/deviantony/docker-elk), [structlog](https://www.structlog.org/) and [python-logstash](https://github.com/vklochan/python-logstash).

## Setup

1. `cd docker/`
2. `docker-compose up -d`
3. `pip install -r requirements.txt`
4. `FLASK_APP=app.py flask run --port=8888`, default port `5000` is used by logstash
5. As described in the [docker-elk initial setup](https://github.com/deviantony/docker-elk#default-kibana-index-pattern-creation) run the fllowing command to create the initial logstash index

```
$ curl -XPOST -D- 'http://localhost:5601/api/saved_objects/index-pattern' \
    -H 'Content-Type: application/json' \
    -H 'kbn-version: 6.1.0' \
    -d '{"attributes":{"title":"logstash-*","timeFieldName":"@timestamp"}}'
```

6. `curl http://localhost:8888/`, should print "Hello, World" and forward a first entry
7. Visit `http://localhost:5601/` to open up Kibana, click on Discover and you should see two entries under a `logstash-*` index.
8. Visit `http://localhost:8888/boom/` to log an exception.

Depending on how quickly you set start up and visit your app Kibana may complain there is no data. Give it a couple of seconds and refresh the page.
