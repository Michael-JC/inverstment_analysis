#!/usr/bin/env python
# coding:utf-8

"""
function:
@author: zkang kai
@contact: 474918208@qq.com
"""
import logging
import logging.config
import os

logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logger.conf"))
logger = logging.getLogger()
logger.addHandler(logging.NullHandler())
