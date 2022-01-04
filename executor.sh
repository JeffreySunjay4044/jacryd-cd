cd lc-client
docker build -t sneha/lc-client:latest .
docker rm -f sneha
docker run -d -p 0.0.0.0:9191:80 --name sneha sneha/lc-client:latest
cd ../lc-server
docker-compose down --remove-orphans
docker-compose build
docker-compose up -d
docker run -e DOPPLER_TOKEN=$dopplerToken -p 5000:5000 docker_lc -name docker_lc