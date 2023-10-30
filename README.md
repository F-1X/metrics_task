# metrics_task

Собраны компоненты для взаимодействия 
+ Oncall, ELK, Prometheus, Grafana, custom mectrics

Prometheus собирает материки с Oncall, Oncall также имеет свой кастомный экспортер, метрики отображаются в Grafana.
ELK собирает логи nginx c сервиса oncall: filebeat->logstash->elasticsearch->kibana, через volumes докер контейнера.
