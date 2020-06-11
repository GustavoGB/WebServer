sudo apt-get update -y  && sudo apt-get upgrade -y 
sudo apt install python3-pip -y 
sudo apt install docker.io
sudo apt install virtualenv
virtualenv env
source ./env/bin/activate
cd /home/ubuntu/
git clone https://github.com/GustavoGB/cloud_project_serveless.git
cd /cloud_project_serveless/
sudo pip3 install fastapi
sudo pip3 install uvicorn 
cd cloud_project_serveless/
uvicorn webserver:app --reload



