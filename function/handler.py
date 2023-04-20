def handle(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from OpenFaaS!"
    }


# 在代码中调用其他云函数
#
# 您可以在代码中通过发送HTTP请求的方式调用其他云函数。在组件库页面，可以查看每个云函数的基本信息，
# 其中的“测试调用地址”即为该云函数的HTTP调用地址。
#
# 当您需要在代码中调用其他云函数时，请确保被调用的云函数已在开发空间部署成功，且有正在运行的实例。


# import requests

# def handle(event, context):
#     # 函数调用请求的payload
#     payload = {
#       "key1": "value1",
#       "key2": 0
#     }

#     # 函数的调用地址，可以在组件库中点击具体的云函数查看其“测试调用地址”
#     func_url = "http://example/function/url"

#     # 发送HTTP请求
#     res = requests.post(func_url, json=payload)

#     # 处理响应
#     data = {
#       "status_code": res.status_code,
#       "text": res.text
#     }

#     return {
#         "statusCode": 200,
#         "body": data
#     }