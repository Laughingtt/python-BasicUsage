

### 编译proto文件
```shell
python -m grpc_tools.protoc -I./protos --python_out=./rpc_package --grpc_python_out=./rpc_package ./protos/transfer.proto

```
# 框架图
![](resource/img.png)