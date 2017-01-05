
## Get SSL Certificate

The Webroot plugin works by placing a special file in the /.well-known directory within your document root, which can be opened (through your web server) by the Let's Encrypt service for validation.

### Nginx config

Explicitly allow access to the `/.well-known` directory.

```
root /var/www/domain.com/public_html;

location ~ /.well-known {
    allow all;
}
```

### Request SSL certificate using letsencrypt's webroot plugin

```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/domain.be/public_html -d domain.com -d www.domain.com
```

NB: the `root` directive in Nginx config file and `--webroot-path` argument in the letsencrypt command should match

The certificate and chain are saved at :

`/etc/letsencrypt/live/<domain.com>/fullchain.pem`

### Certificate Files

The certificate files are saved at : `/etc/letsencrypt/live/<domain.com>/`

- `cert.pem`: Your domain's certificate
- `chain.pem`: The Let's Encrypt chain certificate
- `fullchain.pem`: `cert.pem` and `chain.pem` combined
- `privkey.pem`: Your certificate's private key

## Use SSL Certificate

Nginx config

```
server {
    listen 80;
    server_name domain.com www.domain.com;
    return 301 https://domain.com$request_uri;
}

server {
    listen 443 ssl;

    server_name www.domain.com;
    return 301 https://domain.com$request_uri;
}

server {
    # HTTPS configuration

    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    server_name domain.com; # domain names to serve for

    # SSL configuration
    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    include snippets/ssl-params.conf; # strong SSL settings


    ...
}
```

Restart Nginx

```
sudo systemctl restart nginx
```

Assess security quality at : https://www.ssllabs.com/ssltest/analyze.html?d=<domain.com>

## Auto Renewal SSL Certificate

NB: The renewal is executed only if the certificate is **less than 30 days away from expiration**.

Manually trigger renewal process for all domains

```
sudo letsencrypt renew
```

Automatically trigger renewal process for all domains with cron : `sudo crontab -e`

```
# Renew SSL certification: mondays at 2:30am
30 2 * * 1 /usr/bin/letsencrypt renew >> /home/romain/logs/letsencrypt-renew.log
35 2 * * 1 /bin/systemctl reload nginx

```
