# Migration

```
kubectl cp -n chrissyroshak   cr-wordpress-6c96644b4c-82vfs:/var/www/html/wp-content/ /home/microshak/Source/lab/ChrissyRoshak/migrate/wp-content/ 
kubectl cp -n chrissyroshak   cr-wordpress-6c96644b4c-82vfs:/usr/local/etc/php/conf.d/uploads.ini /home/microshak/Source/lab/ChrissyRoshak/conf.d/uploads.ini 


kubectl cp -n chrissyroshak   cr-mysql-b7c496f5c-msbm8:/var/lib/mysql /home/microshak/Source/lab/ChrissyRoshak/migrate/mysql/
kubectl cp -n chrissyroshak   cr-mysql-b7c496f5c-msbm8:/docker-entrypoint-initdb.d/ /home/microshak/Source/lab/ChrissyRoshak/migrate/docker-entrypoint-initdb.d/init.sql



kubectl cp -n chrissyroshak   cr-mysql-b7c496f5c-msbm8:/docker-entrypoint-initdb.d /home/microshak/Source/lab/ChrissyRoshak/migrate/docker-entrypoint-initdb.d/



kubectl cp -n chrissyroshak   cr-wordpress-6c96644b4c-82vfs:/var/www/html/wp-content/init.sql /home/microshak/Source/lab/ChrissyRoshak/migrate/wp-content/init.sql 




kubectl cp dataaccess:/data data/


```