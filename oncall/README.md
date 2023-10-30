
USE:
    sudo docker-compose stop ; sudo docker-compose rm -f ; sudo docker-compose build ; sudo docker-compose up
    
    !перед запуском скрипта нужно указать в api_confing.yml 
    path_save путь для сохранения файла
    file имя файла
    
    sudo python3 count_enjeneers.py

CHANGES:

    #Дописал прошлый скрипт REST API count_enjeneers.py#
    
    
    nginx теперь проксирует запросы к /metrics

    

FYI:
    для добавление запуска скрипта в задачу cron:

    открыть крон
    crontab -e
    добавить задачу (! пути директории могут отличаться !)
    * * * * * python3 ~/prometeusExersice/oncall/count_enjeneers.py


    # probe параметры (через курл или браузер - открытие пробы)
    localhost:9115/probe?target=oncall:8080&module=http_2xx



useful links:

    # дока по мульти таргетам
    https://prometheus.io/docs/guides/multi-target-exporter/


    # скрипты textfile collector
    https://github.com/prometheus-community/node-exporter-textfile-collector-scripts/blob/master/md_info.sh

    # blackbox github
    https://github.com/prometheus/blackbox_exporter

    # алерты awesome 
    https://samber.github.io/awesome-prometheus-alerts/rules#blackbox

    # redhat статья по блекбоксу
    https://cloud.redhat.com/blog/exposing-custom-metrics-from-virtual-machines


    https://github.com/prometheus/prometheus/blob/release-2.47/config/testdata/conf.good.yml

    https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file




