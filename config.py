#!/usr/bin/env python
#encoding=utf-8

from tornado.options import define

def setup_config():
    define("address", default = '127.0.0.1', help = "run on the given ip", type = str)
    define("port", default = 8421, help = "run on the given port", type = int)
    define("mysql_host", default = "localhost", help = "community database host")
    define("mysql_database", default = "xx", help = "community database name")
    define("mysql_user", default = "xx", help = "community database user")
    define("mysql_password", default = "xxx", help = "community database password")


