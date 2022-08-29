################################################################################################

print("\n \n Пример 1:")

# Пишем в .yaml

import yaml

kafka = {
    'caRootLocation': 'certs//kafka-ca-root.crt',
    'certLocation': 'certs//kafka-clients.crtt'
}

to_yaml = {'login': 'alisa', 'kafka': kafka}

with open('ex5.yaml', 'w') as f:
    yaml.dump(to_yaml, f)

with open('ex5.yaml') as f:
    print(f.read())

################################################################################################

print("\n \n Пример 2:")


# Читаем .yaml

import yaml

with open('ex5.yaml') as f:
    templates = yaml.safe_load(f)

print(templates)

################################################################################################
