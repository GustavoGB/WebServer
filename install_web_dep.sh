sudo apt-get update -y  && sudo apt-get upgrade -y 
sudo apt install python3-pip -y 
sudo apt install docker.io -y 
sudo apt install virtualenv -y 
virtualenv env
source ./env/bin/activate
sudo pip3 install fastapi
sudo pip3 install uvicorn 
uvicorn webserver:app --reload



