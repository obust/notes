
```
usermod -a -G www-data <username>

mkdir /var/www
chown -R root:www-data
chmod g+rwxs /var/www
setfacl -d -m group:www-data:rwx /var/www

mkdir /var/repo
chown -R root:www-data
chmod g+rwxs /var/repo
setfacl -d -m group:www-data:rwx /var/repo

cd /var/repo
mkdir <site>.git
cd <site>.git
git init --bare
cd hooks

touch post-receive
chmod +x post-receive
nano post-receive
#!/bin/sh
git --git-dir=/var/repo/<site>.git --work-tree=/var/www/<site> checkout -f
```

```
git remote add production ssh://<username>@<mydomain.com>/var/repo/<site>.git
git push production +master:refs/heads/master

```

## Nginx

```
sudo ufw allow 'OpenSSH'
sudo ufw allow 'Nginx HTTP'
sudo ufw enable
```
