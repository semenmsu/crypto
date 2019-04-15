#config.vm.provision "shell", path: "script.sh"
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.6

curl https://bootstrap.pypa.io/get-pip.py | sudo -H python3.6

pip3.6 install websocket-client --user

