# Spotify API Challenge

Change directory into the challenge directory
```
cd <your-local-system>/Challenges/Spotify_data_ETL_pipeline
```

Run PostgreSQL DB with docker compose
```
docker-compose \
	-f db_docker_compose.yml \
	--project-name spotify_db \
	up -d
```
