ARG ELASTIC_VERSION

# https://www.docker.elastic.co/
FROM logstash:${ELASTIC_VERSION}



# Add your logstash plugins setup here
RUN bin/logstash-plugin install --no-verify logstash-filter-json_encode
