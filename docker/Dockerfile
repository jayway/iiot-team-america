FROM debian:jessie 

RUN apt-get update && apt-get install -y \
   wget \
   openjdk-7-jdk
RUN wget -q https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz && tar xzf logstash-1.4.2.tar.gz

ADD start.sh /opt/logstash/start.sh
ADD logstash.conf /opt/logstash/logstash.conf

EXPOSE 5000
EXPOSE 9200
EXPOSE 9292
CMD ["/opt/logstash/start.sh"]