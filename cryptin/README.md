docker build --tag cryptin .
docker run -it -e coinmarketcap=MYKEY -e bootstrapserver=MyKafkaBootStrap -t cryptin /bin/bash

docker tag cryptin:latest microshak/cryptin:latest


docker push microshak/cryptin:latest