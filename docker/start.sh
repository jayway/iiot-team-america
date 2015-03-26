#!/bin/sh
exec /logstash-1.4.2/bin/logstash agent -f /opt/logstash/logstash.conf --debug -- web