# ssh to an instance on GCP, [reference](https://blog.csdn.net/datadev_sh/article/details/79593360)
1. `ssh-keygen -t rsa -C 'your email'`
2. paste pub key to gcp-computer engine-meta-ssh key
3. save private key to local disk
4. open gcp ssh in browser window
5. `sudo -i`
6. `vi /etc/ssh/sshd_config`
7. `PermitRootLogin yes
PasswordAuthentication yes`
8. `passwd root`
9. `/etc/init.d/ssh restart`


# how to install fastai on Ubuntu
1. Download [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Use `bash Miniconda3-latest-MacOSX-x86_64.sh` to install Miniconda, [reference](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/macos.html)
3. Install [pytorch](https://pytorch.org/get-started/locally/)
4. [CPU only](https://docs.fast.ai/install.html)
5. [Jupyter notebook](https://docs.fast.ai/install.html#jupyter-notebook-dependencies)
