# ArtResourceCollector

ArtResourceCollector 是一个用于收集图片文件夹中的图片名称，并从维基百科获取相关简介，然后将这些信息保存到 Excel 文件中的工具。

## 依赖

请确保你已经安装了以下依赖：

- `openpyxl`
- `wikipedia-api`

你可以通过以下命令安装这些依赖：

```sh
pip install -r 

requirements.txt


```

## 使用方法

1. 将你的图片文件夹路径更新到 `excle.py` 文件中的 `image_folder` 变量。
2. 运行 `excle.py` 脚本：

```sh
python 

excle.py


```

3. 脚本将会遍历图片文件夹中的所有图片文件，获取文件名并从维基百科获取相关简介，然后将这些信息保存到 `art_resources_0.xlsx` 文件中。

## 文件结构

```
.DS_Store
excle.py
requirements.txt
```

- `excle.py`: 主脚本文件。
- `requirements.txt`: 依赖文件。

## 注意事项

- 请确保你的图片文件夹路径是正确的。
- 请确保你有稳定的网络连接以便访问维基百科 API。

## 许可证
此项目使用 MIT 许可证。有关更多信息，请参阅 LICENSE 文件。
