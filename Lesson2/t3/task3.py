import yaml

DICTS = {
    '1$': ['this', 'my', 'task'],
    '2€': 9056,
    '3₴': {'sell': 'try', 'not_good': 'why'},
}

with open('file_1.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DICTS, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("file_1.yaml", 'r', encoding='utf-8') as f_out:
    DATA_DICT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DICTS == DATA_DICT)
