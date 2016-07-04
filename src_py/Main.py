# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import logging
import MakePartition
import FileRead
import sys
import PartitionStrategyType
import CalCommunication

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

if __name__ == "__main__":
    """
    The input args is
    args[1]: file_name
    args[2]: user_partition_num
    args[3]: item_partition_num
    args[4]: data sample separation char
    """
    if len(sys.argv) < 2:
        logging.error(
            "\nyou should pass the parameter\nargs[1] : file_name \nand the follow three optional parameters \n"
            "args[2]:user_partition_num \nargs[3]:item_partition_num \nargs[3]: data sample separation char")
        exit(-1)

    # ===================== parameter parsing =====================
    file_name = sys.argv[1]
    user_partition_num = 8
    item_partition_num = 8
    sp = '\t'
    if len(sys.argv) > 2:
        user_partition_num = int(sys.argv[2])
    if len(sys.argv) > 3:
        item_partition_num = int(sys.argv[3])
    if len(sys.argv) > 4:
        sp = sys.argv[4]
    # ===================== end parameter parsing =================

    user_related_items_dict = {}
    item_related_users_dict = {}

    FileRead.read_from_file(file_name, user_related_items_dict, item_related_users_dict, sp)
    logging.debug("load data success\n")

    partition_strategy = "random"

    # ++++++++++++++++++++++ input the partition strategy +++++++++
    while True:
        input_partition_startegy = raw_input("Please input the partition strategy:\n")
        if input_partition_startegy not in PartitionStrategyType.partitionStrategyTypeList:
            logging.info("Please input the right name of partition strategy\n")
            logging.info(str(PartitionStrategyType.partitionStrategyTypeList))
        else:
            break
    # +++++++++++++++++++++ end the partiton strategy +++++++++++++

    # ===================== make partition for user and item ++++++
    make_partition = MakePartition.MakePartition(user_related_items_dict, item_related_users_dict, user_partition_num,
                                                 item_partition_num, partition_strategy)
    make_partition.make_user_partition()
    make_partition.make_item_partition()
    # ===================== end make partition for user and item +++

    logging.info("finish the partition process")

    # =================== cal communication capacity ++++++++++++++

    cal_communication_example = CalCommunication.CalCommunication(user_related_items_dict, item_related_users_dict,
                                                                  make_partition.user_map_dict,
                                                                  make_partition.item_map_dict,
                                                                  user_partition_num, item_partition_num)
    cal_user_vector_communication, cal_item_vector_communication = cal_communication_example.cal_communication()

    logging.info("cal_user_vector_communication is %d and cal_item_vector_communication is %d\n" % (
                cal_user_vector_communication, cal_item_vector_communication))

    logging.debug("End cal communication process")