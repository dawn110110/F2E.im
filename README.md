## ABOUT PyHack

PyHack 社区, fork from F2E.im

## How to run on your own machine

1. install all required modules:

    ```
    shell> pip install -r requirements.txt
    ```

2. create database and then execute sql file in dbstructure/

    ```
    shell> mysql -u YOURUSERNAME -p

    mysql> create database f2e;
    mysql> exit

    shell> mysql -u YOURUSERNAME -p --database=f2e < dbstructure/f2e.sql
    ```

3. set your mysql user/password and smtp server config in `application.py` and `lib/sendmail.py`.
4. check above, using ``python application.py`` to start server.

    ```
    shell> python application.py --port=9001 --mysql_database=f2e --mysql_host=localhost --mysql_password=YOURPASSWORD --mysql_user=YOURUSERNAME
    ```

## How to set up a production enironment

You need to know a little of supervisor and nginx, all config files are available in conf/

## 相对于F2E.im的修改

- 加了一个django admin的后台（就是默认的，没有任何定制的修改），但是已经足够使用了. 可以编辑Plane/Nodes
- 修改了模版，去掉了很多东西.
- application.py 顶部加一行代码，修改cwd路径到application.py所在目录，以使得通过绝对路径启动application.py也能够正常上传头像.

###django admin 相关

1. 先建好主站，然后配置好dj_admin里的settings中的DATABASE
2. 直接`python manage.py syncdb`
3. 修改django syncdb 建立的表的编码：
    - `ALTER TABLE ``django_admin_log`` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;`
    - `ALTER TABLE django_admin_log MODIFY COLUMN object_repr VARCHAR(255)  CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;`
    - `ALTER TABLE django_admin_log MODIFY COLUMN change_message longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;`
4. 嗯，然后就该咋用咋用.
