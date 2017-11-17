#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__author__ = 'VVL'

' url handlers '

import re, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
@asyncio.coroutine
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }