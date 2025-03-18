import json
json_data={"id":1,"name":"sowmya","training":"python"}
json_string=json.dumps(json_data)
print(json_string)
json_loads=json.loads(json_string)
print(json_loads)

"""output:
{"id": 1, "name": "sowmya", "training": "python"}
{'id': 1, 'name': 'sowmya', 'training': 'python'}"""
