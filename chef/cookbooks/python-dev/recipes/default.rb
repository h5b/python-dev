[
  "build-essential",
  "git-core",
  "vim",
  "python",
  "python-pip",
].each do |p|
  package p
end

bash "install_pipmodules" do
  user "root"
  code <<-EOH
    pip install nose
  EOH
end
