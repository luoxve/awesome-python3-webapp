#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
Default configurations.
'''

__author__ = 'VVL'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': '3306',
        'user': 'www-data',
        'password': 'www-data',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}