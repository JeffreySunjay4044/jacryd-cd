# shellcheck disable=SC2154
git clone $repositoryAddress
cd $scriptLocation
docker-compose build --no-cache
docker-compose up