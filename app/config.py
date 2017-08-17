# encoding:utf-8

# encoding:utf-8

import os
base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    SECRET_KEY = 'jdasouerqwbnn5678jdafsd'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.137.11:3376/myapp'
    DEBUG = True
    # HOST = '0.0.0.0'
    # PORT = 9092

    @staticmethod
    def init_app(app):
        pass


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.137.11:3376/myapp'


class ProductConfig(BaseConfig):
    pass


config = {
    'devlopment': DevConfig,
    'productment': ProductConfig,
    'default': DevConfig
}
