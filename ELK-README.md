# Docker ELK stack

## Installation

1. Install [Docker](http://docker.io).
2. Install [Docker-compose](http://docs.docker.com/compose/install/).
3. Clone this repository
4. Update the logstash-configuration in logstash-conf/logstash.conf (test your filters here)
5. docker-compose up
6. nc localhost 10001 < /some/log/file.log
7. http://localhost:10002 to see the messages show up in Kibana 3.
8. http://localhost:10003 to use Kibana 4.

This will create 4 Docker containers with Elasticsearch, Logstash, Kibana 3 and Kibana 4 running in them and connected to each other. Four ports are exposed for access:

* 10001: Logstash TCP input.
* 10000: Elasticsearch HTTP (With Marvel plugin accessible via [http://localhost:9200/_plugin/marvel](http://localhost:10000/_plugin/marvel))
* 10002: Kibana 3 web interface.
* 10003: Kibana 4 web interface.
