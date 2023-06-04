import json

def get_data():
    # 假设这是你的返回值
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return data

# 获取返回值
response = get_data()

# 判断返回值是否为JSON格式
try:
    json_data = json.loads(response)
    # 返回值是一个合法的JSON对象
    print("返回值是一个合法的JSON对象")
    # 可以通过json_data访问返回值的属性
    print("Name:", json_data['name'])
    print("Age:", json_data['age'])
    print("City:", json_data['city'])
except ValueError:
    # 返回值不是一个合法的JSON对象
    print("返回值不是一个合法的JSON对象")
