# shellcheck disable=SC2154
git clone $repositoryAddress
export MONGO_CREDS=$mongoPwd
export REDIS_PWD=$redisPwd
export OSM_CMDB_URL=$osmCmdbUrl
export DOPPLER_TOKEN=$dopplerToken
cd $scriptLocationClient
/bin/bash ./executor.sh