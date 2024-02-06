# Общая для всего ДЗ настройка

см. block1/Readme.md

# Работа Tumbling, Sliding
```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic sinaya --partitions 1 --replication-factor 1
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe sinaya
```

```commandline
python3 producer_1.py
```

## Tumbling Windows
```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job3.py -d  
```
```commandline
python3 block2/consumer_3.py
```

## Sliding Windows
```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job4.py -d  
```
```commandline
python3 block2/consumer_4.py
```

# Session Windows
джоба создаётся, работает, но консюмер ничего не вытаскивает(

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic sinaya2 --partitions 1 --replication-factor 1
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe sinaya2
```

```commandline
python3 producer_2.py
```


```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic sinaya2 --partitions 1 --replication-factor 1
```

```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job5.py -d  
```

```commandline
python3 block2/consumer_5.py
```

