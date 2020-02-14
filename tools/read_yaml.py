import os
import yaml
from config import base_url


def read_yaml(filename):
    with open(base_url+os.sep+"data"+os.sep+filename, "r",encoding="utf-8") as f:
        data_list = []
        # 调用方法解析 文件流
        for data in yaml.safe_load(f).values():
            data_list.append(tuple(data.values()))
        return data_list


if __name__ == '__main__':
    print(read_yaml("login.yaml"))

