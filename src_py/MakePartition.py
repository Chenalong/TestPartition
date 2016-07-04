# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import logging
import random


class MakePartition:
    """
    complete the function of making partition in users and items
    partition_strategy: random,similarity
    """

    def __init__(self, user_related_items_dict, item_related_users_dict, user_partition_num, item_partition_num,
                 partition_strategy="random"):
        """
        :param data_list: The element type is Rating
        :param user_partition_num: the num of user partitions'num
        :param item_partition_num: the numm of item partitions'num
        :param partition_strategy: using string to refer partition strategy
        :return:
        """
        self.user_partition_num = user_partition_num
        self.item_partition_num = item_partition_num
        self.item_related_users_dict = item_related_users_dict
        self.user_related_items_dict = user_related_items_dict
        self.partition_strategy = partition_strategy
        self.user_map_dict = {}
        self.item_map_dict = {}

        ### 获取用户和物品的列表
        logging.debug("The num of users is %d and the num of items is %d\n" % (
                        len(self.user_related_items_dict), len(self.item_related_users_dict)))

    def make_user_partition(self):
        if self.partition_strategy == "random":
            self.random_partition(self.user_related_items_dict, self.user_map_dict, self.user_partition_num)
        else:
            pass

    def make_item_partition(self):
        if self.partition_strategy == "random":
            self.random_partition(self.item_related_users_dict, self.item_map_dict, self.item_partition_num)
        else:
            pass

    def random_partition(self, dict_info, map_dict, partition_num):
        """
        :param set_info: user or item collection
        :param map_dict: map user or item to certain partition
        :param partition_num: the user partition num or item partition num
        :return:
        """
        for key in dict_info:
            hash_val = hash(key)
            map_dict[key] = hash_val % partition_num



