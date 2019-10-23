import yaml

with open('data.yaml','r') as f:
    d = yaml.load(f,Loader=yaml.FullLoader)
    print(d)

# dat = {'data1':{'name':'zdc','pwd':123},'data2':{'name':'aaa'}}
# with open('data2','w') as f:
#     yaml.dump(dat,f)