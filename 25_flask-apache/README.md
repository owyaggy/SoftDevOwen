# how-to :: Deploy Flask on Apache #

## Overview ##
Flask needs the help of Apache to serve persistent websites, using configured settings to host Flask apps on its servers.

## Estimated Time Cost: 1.5 hours ##

## Prerequisites ##
* DigitalOcean droplet
* Ubuntu 20.04.3
* Apache2
* A Flask app

## Instructions ##

1. Install WSGI
2. Install FLASKAPP
3. Set up a venv
4. Test app in venv
5. Create `.conf` file
   
```
   <VirtualHost *:80>
    ServerName DROPLET_IP_ADDRESS
    ServerAdmin USERNAME@DROPLET_IP_ADDRESS
    WSGIScriptAlias / /var/www/APP_NAME/APP_NAME.wsgi
    <Directory /var/www/APP_NAME/APP_SCRIPTS/>
        Order allow,deny
    Allow from all
    </Directory>
    Alias /static /var/www/APP_NAME/APP_SCRIPTS/static
    <Directory /var/www/APP_NAME/APP_SCRIPTS/static/>
        Order allow,deny
    Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

6. Create `.wsgi` file

```python
#!/usr/bin/python
import sys
import logging
from os import urandom

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/APP_NAME/")
sys.path.insert(0,"/var/www/APP_NAME/APP_SCRIPTS/")

def application(environ, start_response):
    from app import app as _application
    return _application(environ, start_response)

if __name__ == "__main__":
    _application.run()
```

### AMAZING DO DOCS ###
* [Server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)

* [Installing stack](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04)

* [Setting up python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)

* [Deploying flask](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04)

* [Using sqlite](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application)