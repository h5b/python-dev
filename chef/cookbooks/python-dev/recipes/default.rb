[
  "build-essential",
  "git-core",
  "vim",
  "pylint",
  "python",
  "python-pip",
].each do |p|
  package p
end

bash "install_pipmodules" do
  user "root"
  code <<-EOH
    pip install coverage
    pip install flake8
    pip install nose
  EOH
end
