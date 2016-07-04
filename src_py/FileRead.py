# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import codecs
import logging


class Rating:
    """ this is Rating data format """

    def __init__(self, userId, itemId):
        self.userId = userId
        self.itemId = itemId


def read_from_file(file_name, user_related_items_dict, item_related_users_dict, sep=' '):
    """
    :param file_name:  file name to read
    :param user_related_items_dict: 保存每个用户对物品打分列表
    :param item_related_users_dict：保存对该物品有过行为的用户列表
    :return: none
    """
    file_read = codecs.open(file_name)

    invalid_data_num = 0
    for line in file_read:
        line = line.split(sep)
        if len(line) != 3:
            invalid_data_num += 1
        else:
            user_related_items_dict.setdefault(line[0], set())
            item_related_users_dict.setdefault(line[1], set())
            user_related_items_dict[line[0]].add(line[1])
            item_related_users_dict[line[1]].add(line[0])

    if invalid_data_num != 0:
        logging.warning("the data format may be wrong,the application separation is %s "
                        "and the wrong data line num is %d" % (sep, invalid_data_num))


