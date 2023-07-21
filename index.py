#!/env/bin/python3
# -*- coding: UTF-8 -*-

import urllib.request as request
import chardet
from lib import help
import sys
import logging
import coloredlogs
from argparse import ArgumentParser

parser = ArgumentParser()
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
coloredlogs.install(level=logging.DEBUG)

def convert():
    # rawdata = request.urlopen('https://www.bing.com/').read()

    args = help.init_parser()
    if not args.verbose:
        coloredlogs.install(level=logging.INFO)
    # logger.info("命令行参数为:{args}".format(args=args))

    # file_path = '/test/test2.txt'
    file_path = args.source_file
    fr = open(file_path, "rb")
    raw_data = fr.read()
    res = chardet.detect(raw_data)
    logger.info('探测结果是:{res}'.format(res=res))
    if not args.test_only:
        write_data = raw_data.decode(res['encoding'], errors='ignore').encode(encoding=args.target_code, errors='ignore')
        fw = open(file_path, "wb")
        fw.write(write_data)
        logger.info("写入完成")
        fw.close()
    fr.close()


    # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
    # {'confidence': 0.98999999999999999, 'encoding': 'GB2312'}


if __name__ == '__main__':
    try:
        logger.info("Start converting ... ")
        convert()
    except Exception as e:
        logger.error(e)