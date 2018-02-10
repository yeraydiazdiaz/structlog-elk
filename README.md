# Structlog + ELK stack

A proof of concept of structured logging from Python to an Elasticsearch + Logstash + Kibana environment using [Docker ELK](https://github.com/deviantony/docker-elk), [structlog](https://www.structlog.org/) and [python-logstash](https://github.com/vklochan/python-logstash).

## Setup

1. `docker-compose up`, and wait for a bit, the app will start up first, then Elasticsearch and Kibana and finally Logstash
2. As described in the [docker-elk initial setup](https://github.com/deviantony/docker-elk#default-kibana-index-pattern-creation) run the fllowing command to create the initial logstash index

```
$ curl -XPOST -D- 'http://localhost:5601/api/saved_objects/index-pattern' \
    -H 'Content-Type: application/json' \
    -H 'kbn-version: 6.1.0' \
    -d '{"attributes":{"title":"logstash-*","timeFieldName":"@timestamp"}}'
```

3. `curl http://localhost:8888/`, should print "Hello, World" and forward a first entry. You should see Logstash output in the terminal.
4. Visit [`http://localhost:5601/`](http://localhost:5601/) to open up Kibana, click on Discover and you should see two entries under a `logstash-*` index.
5. Visit [`http://localhost:8888/boom/`](http://localhost:8888/boom/) to log an exception.
