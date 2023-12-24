```commandline
cd kafka
```

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
```commandline
docker-compose down -v
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic topic_name --partitions 1 --replication-factor 1
```

```commandline
python3 producer_1.py
```

```commandline
python3 device_job_save_flint.py
```

```commandline
python3 consumer_1.py
```


```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job.py -d  
```
