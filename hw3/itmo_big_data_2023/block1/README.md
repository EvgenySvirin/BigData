# Общая для всего ДЗ настройка

В начале поднять хадуп, как обычно, два раза неймноду, потом остальное.

```commandline
docker-compose build
```

```commandline
docker-compose up -d
```

```commandline
docker-compose ps
```

```
http://localhost:8081/#/overview
```

Отключить:
```commandline
docker-compose down -v
```

# Работа

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic sinaya --partitions 1 --replication-factor 1
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe sinaya
```

```commandline
python3 producer_1.py
```

```commandline
python3 consumer_1.py
```

##  Cохранять в local dir
```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job1.py -d  
```

##  Cохранять в hdfs
```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job2.py -d  
```