# metrics_task

Собраны компоненты для взаимодействия 
+ Oncall, ELK, Prometheus, Grafana, custom mectrics

Prometheus собирает материки с Oncall, Oncall также имеет свой кастомный экспортер, метрики отображаются в Grafana.
ELK умеет импортировать логи nginx c сервиса oncall, через volumes докер контейнера.
