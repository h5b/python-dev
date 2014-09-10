# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"
  config.vm.hostname = "python-dev"

  config.vm.network :private_network, ip: "192.168.10.23"

  config.vm.provider "virtualbox" do |v|
    v.name = "python-dev"
    v.memory = 512
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.ssh.forward_agent = true

  config.vm.provision "chef_solo" do |chef|
    chef.cookbooks_path = "chef/cookbooks"
    chef.add_recipe "apt"
    chef.add_recipe "etc"
    chef.add_recipe "python-dev"
  end

end
