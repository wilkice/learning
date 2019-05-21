# GCP + Vs code remote ssh

Follow these steps to set remote development environment on GCP.

# GCP settings

1. Create computer instance follow [this tutorial](https://github.com/cs231n/gcloud) by CS231N

2. SSH to instance with browser

3. ```shell
   vi /etc/ssh/sshd_config
   ```

   Change the following lines so we can connect to this instance by ssh key not password. If you like, you can use password authentication. Maybe need a restart for ssh `/etc/init.d/ssh restart`

   ```shell
   PubKeyAuthentication yes
   ```

4. Add SSH key to GCP. Following my [reference](https://blog.csdn.net/datadev_sh/article/details/79593360) at the bottom of this page.

5. Connect to instance in terminal

   ```shell
   ssh <your user name in id_rsa.pub>@<instance ip>
   ```

6. Add user to sudo group

   ```shell
   sudo -i
   usermod -aG sudo <username>
   ```

# Vs code settings

1. Download [Vs Code Insider](https://code.visualstudio.com/insiders/).

2. Install [Remote Development Extension Pack](https://aka.ms/VSCodeRemoteExtensionPack)

3. Follow this [docs](https://code.visualstudio.com/blogs/2019/05/02/remote-development). It's detailed with Videos and Images.

   > If you meet some problems when using the internal terminal in vs code, please refer to [this issue](https://github.com/microsoft/vscode-remote-release/issues/220#issuecomment-490374437)

4. You can follow this [Youtube Video](https://youtu.be/lKXMyln_5q4) too.

# FAQ:

1. Can I use us region computer instance if I am in China?

   Sure you can. Maybe you need to set all proxy to https://127.0.0.1:1080.

2. Do I need to install miniconda?

   No, miniconda is preinstalled.

3. How much does it cost?

   n1-highmem-2 (2 vCPUs, 13 GB memory) instance in us:  $ 0.1184/h

   K80 GPU: about $ 0.45/h

   Disk and Internet traffic don't cost much.

# Reference:

[用SSH工具XShell连接谷歌云 root用户或普通用户](https://blog.csdn.net/datadev_sh/article/details/79593360)

[Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)



