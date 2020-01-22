#!/bin/bash

eval "$(ssh-agent -s)" &&
ssh-add -k ~/.ssh/id_rsa &&
cd /var/www/backend #helloworld
git pull

source ~/.profile
echo "$DOCKERHUB_PASS" | docker login --username $DOCKERHUB_USER --password-stdin
docker stop hijub
docker rm hijub
docker rmi purnamasftr/hijub:deployment2
docker run -d --name hijub -p 5000:5000 purnamasftr/hijub:deployment2