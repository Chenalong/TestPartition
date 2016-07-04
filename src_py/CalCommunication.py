# -*- coding:utf-8 -*-
__author__ = 'Administrator'


class CalCommunication:
    """
    The class function is to calculate the network communication in certain partition strategy
    """

    def __init__(self, user_related_items_dict, item_related_users_dict, user_map_dict, item_map_dict,
                 user_partition_num, item_partition_num):
        self.user_related_items_dict = user_related_items_dict
        self.item_related_users_dict = item_related_users_dict
        self.user_map_dict = user_map_dict
        self.item_map_dict = item_map_dict
        self.user_partition_num = user_partition_num
        self.item_partition_num = item_partition_num

    def cal_communication(self):
        cal_user_vector_communication = self.__cal_communication(self.user_related_items_dict, self.user_partition_num,
                                                                 self.user_map_dict)

        cal_item_vector_communication = self.__cal_communication(self.item_related_users_dict, self.item_partition_num,
                                                                 self.item_map_dict)

        return cal_user_vector_communication, cal_item_vector_communication

    def __cal_communication(self, relation_dict, partition_num, map_dict):
        """
        :param relation_dict: 保存用户/物品 与 物品/用户的相关关系
        :param partition_num: 物品和用户的分区数量
        :param map_dict:  物品和用户id 对应的分区号
        :return: 计算 用户/物品特征向量需要的网络传输量
        """
        communication_total = 0
        partition_related_vectors = []
        for i in range(partition_num):
            partition_related_vectors.append(set())

        for key in relation_dict:
            partition = map_dict[key]
            for value in relation_dict[key]:
                partition_related_vectors[partition].add(value)

        for i in range(partition_num):
            communication_total += len(partition_related_vectors[i])

        return communication_total