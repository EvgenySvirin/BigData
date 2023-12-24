```commandline
cd ../kafka
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

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic task1 --partitions 3 --replication-factor 1
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic task1_processed --partitions 3 --replication-factor 1
```

```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job_save_flint.py -d  
```

```commandline
python3 producer_1.py
```

```commandline
python3 consumer_1.py
```
