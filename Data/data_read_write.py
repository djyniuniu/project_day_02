import yaml
with open('./data.yaml','r',encoding='utf-8') as f:
    data_list = []
    data = yaml.load(f)
    # print(data)
    for i in data.get('Login_in'):
        print(i.keys())
        for o in i.keys():
            data_list.append((o,i.get(o).get('user'),i.get(o).get('passwd'),i.get(o).get('toast_mess'),i.get(o).get('expect_mess'),i.get(o).get('tag')))
        print(data_list)

