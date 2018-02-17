#!/usr/bin/env python
# -*- encoding: UTF8 -*-

#######################################################################
#
#    Copyright (c) 2018 Stefan Helmert <stefan.helmert@t-online.de>
#
#######################################################################


from deepops import passwordFilter
import logging
import traceback
import re

logger = logging.getLogger('cryptdomainmgr')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s    [%(asctime)s]    %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

def log(msg, options = ['showlocation']):
    if 'notfilterpassword' not in options:
        msg = passwordFilter(msg)
    if 'showlocation' in options:
        trc = traceback.extract_stack()
        return '{}/{}()/{}:    {}'.format(trc[-3][0], trc[-3][2], re.search('[^\(]*\((.*)\)', trc[-3][3]).group(1), msg)
    else:
        return msg 

def debug(msg, options = ['showlocation']):
    logger.debug(log(msg, options))

def info(msg, options = []):
    logger.info(log(msg, options))

def warn(msg, options = []):
    logger.warn(log(msg, options))

def error(msg,options = []):
    logger.error(log(msg, options))

def critical(msg, options = []):
    logger.critical(log(msg, options))

