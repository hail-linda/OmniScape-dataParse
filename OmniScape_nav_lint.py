import logging, datetime, os
import pandas as pd
import numpy as np


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # 以下两行是为了在jupyter notebook 中不重复输出日志
    if logger.root.handlers:
        logger.root.handlers[0].setLevel(logging.WARNING)

    handler_stdout = logging.StreamHandler()
    handler_stdout.setLevel(logging.DEBUG)
    handler_stdout.setFormatter(logging.Formatter(' %(levelname)s - %(message)s - %(funcName)s'))
    logger.addHandler(handler_stdout)
    
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_file_name = f"./log/{current_time}.log"
    handler_file = logging.FileHandler(log_file_name, encoding='utf-8')
    handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s'))
    logger.addHandler(handler_file)

    return logger

class OmniScapeNavLint:
    def __init__(self):
        self.logger = get_logger(__name__)

    def DB3Check(self, DB3Filename):
        from rosbags.rosbag2 import Reader
        if not os.path.exists(DB3Filename):
            self.logger.error(f"DB3文件路径 {DB3Filename} 不存在")
            raise FileNotFoundError(f"DB3文件路径 {DB3Filename} 不存在")
        else:
            self.logger.info(f"DB3文件路径 {DB3Filename} 正常")
        try:
            with Reader(DB3Filename) as reader:
                pass
        except Exception as e:
            self.logger.error(f"DB3文件路径 {DB3Filename} 存在，但读取失败:"+str(e))
            raise e
        
    def dirExistCheck(self, dirPathList):
        if isinstance(dirPathList, str):
            dirPathList = [dirPathList]
        for dirPath in dirPathList:
            if not os.path.exists(dirPath):
                self.logger.info(f"输出路径 {dirPath} 不存在，创建路径")
                os.makedirs(dirPath)
            else:
                self.logger.info(f"输出路径 {dirPath} 正常")
                
    def topicMsgCheck(self, topicFileMap, topic2msgDict):
        for topic in topicFileMap:
            if topic["topic"] not in topic2msgDict:
                self.logger.error(f"话题 {topic['topic']} 不存在")
                raise ValueError(f"话题 {topic['topic']} 不存在")
                return False
        self.logger.info("话题检查完成,正常")

    def timeLineCheck(self, topicList, timeLine):
        timeLine1e9 = {}
        for topic in topicList:
            timeLine1e9[topic] = [x/1e9 for x in timeLine[topic]]
        # 数据量/时长/平均频率/跳变点个数（超过平均频率1.5倍）/跳变点比例/最大跳变点时长/最大跳变点与频率比例
        timeLineDict = {}
        for topic in topicList:
            timeLineDict[topic] = {}
            timeLineDict[topic]["dataNum"] = round(len(timeLine1e9[topic]),3)
            timeLineDict[topic]["duration"] = round((np.max(timeLine1e9[topic])-np.min(timeLine1e9[topic])),3) if timeLineDict[topic]["dataNum"] > 0 else "无数据"
            timeLineDict[topic]["freq"] = round(timeLineDict[topic]["dataNum"]/timeLineDict[topic]["duration"],3) if timeLineDict[topic]["dataNum"] > 0 else "无数据"
            diff1e9 = np.diff(timeLine1e9[topic])
            timeLineDict[topic]["jumpNum"] = np.sum(diff1e9 > (1/timeLineDict[topic]["freq"])*1.5) if timeLineDict[topic]["dataNum"] > 0 else "无数据"
            timeLineDict[topic]["jumpRatio"] = timeLineDict[topic]["jumpNum"]/timeLineDict[topic]["dataNum"]*100 if timeLineDict[topic]["dataNum"] > 0 else "无数据"
            timeLineDict[topic]["maxJumpTime"] = np.max(diff1e9) if timeLineDict[topic]["dataNum"] > 0 else "无数据"
            timeLineDict[topic]["maxJumpTimeRatio"] = 100*timeLineDict[topic]["maxJumpTime"]/(1/timeLineDict[topic]["freq"]) if timeLineDict[topic]["dataNum"] > 0 else "无数据"
        df = pd.DataFrame(timeLineDict)
        # df 转置
        df = df.T
        df.columns = ["数据量","时长(s)","平均频率(Hz)","跳变点个数","跳变点比例（%）","最大跳变点时长(s)","最大跳变点与频率比例(%)"]
        df.index = topicList
        return df

            