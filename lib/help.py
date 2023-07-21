#!/bin/bash/env python
# -*- coding: UTF-8 -*-

from argparse import ArgumentParser

def init_parser():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="source_file",
                        required=True,
                        help="FILE path to be converted", metavar="SOURCE FILE")
    # parser.add_argument("-q", "--quiet",
    #                     action="store_false", dest="verbose", default=True,
    #                     help="don't print status messages to stdout")
    parser.add_argument("-tc", "--target-encoding", dest="target_code",
                        help="目标文件编码", default='utf-8')
    parser.add_argument("-v", "--verbose", help="调试模式",
                        action="store_true")

    args = parser.parse_args()
    return args