import yaml
import os
class Op_Data(object):
    def __init__(self,file_name):
        #先定义文件路径
        self.file_path = os.getcwd() + os.sep + 'Data' + os.sep+ file_name
    def read_data(self):
        #读取文件
        with open(self.file_path,'r',encoding='utf-8') as f:
            return yaml.load(f)
    def write_data(self,data):
        #写入数据
        with open(self.file_path,'w',encoding='utf-8') as f:
            return yaml.dump(data,f)