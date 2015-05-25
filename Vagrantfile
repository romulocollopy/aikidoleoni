$shell = <<SHELL
# sudo apt-get update
# sudo apt-get upgrade -y
# sudo apt-get install docker.io -y
# sudo apt-get install openssh-server openssh-client nginx -y
# sudo apt-get install build-essential python-dev python3-dev python-virtualenv python-pip -y
# sudo useradd deploy -G www-data

# sudo mkdir -p /home/deploy/app/config
# sudo mkdir -p /home/deploy/app/logs
# sudo chown -R deploy:deploy /home/deploy
SHELL

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.host_name = "legere"
  config.vm.network :private_network, ip: "192.168.58.101" 

  config.vm.provision "shell", inline: $shell
end
