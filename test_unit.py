#!/usr/bin/env python
# encoding: utf-8
import bottle


@bottle.route('/')
def index():
    print '你好'
    return 'Hi!'


if __name__ == '__main__':
    bottle.run()