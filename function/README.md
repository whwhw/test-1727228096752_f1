# python3-http-debian云函数模板

## 使用方法

python3-http-debian模板文件结构如下：
```
.
|-- Dockerfile
|-- function
|   |-- handler.py
|   |-- handler_test.py
|   |-- requirements.txt
|   `-- tox.ini
|-- index.py
`-- requirements.txt
```
使用IDE工具时，在高级模式下，可以看到和编辑所有文件；在简单模式下，仅可以看到和编辑function目录下的文件。

通常情况下，仅需要在`function/handler.py`的`handle`函数中编写代码处理HTTP请求，并在`function/requirements.txt`中添加依赖，即可部署和使用云函数。若对HTTP服务端和镜像的环境有更多的自定义需求，可以在高级模式下编辑`index.py`和`Dockerfile`等文件。
