# import yaml
# def ret_yaml(data):
#
#     with open('D:\PO2\Data'+'\\'+data+'.yaml','r') as f:
#         da = yaml.load(f,Loader=yaml.FullLoader)
#         return qda

import yaml
def read_yaml(data):
    with open('D:\PO2\Data'+'\\'+data+'.yaml','r') as f:
        return yaml.load(f,Loader=yaml.FullLoader)