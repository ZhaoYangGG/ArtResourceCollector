import os
import wikipediaapi
from openpyxl import Workbook

# 定义图片路径
image_folder = '/Volumes/One Touch'

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active
# 定义保存的Excel文件名称
excel_filename = 'art_resources_0.xlsx'

# 设置表头
ws.append(['序号', '作品名称', '作品简介'])
print("Excel表头已设置")

# 初始化维基百科API，添加用户代理
wiki_wiki = wikipediaapi.Wikipedia('ART (YOUR WIKI ACCOUNT)', 'en')
print("维基百科API已初始化")

# 遍历图片文件夹
for idx, filename in enumerate(os.listdir(image_folder), start=1):
    # 跳过隐藏文件
    if filename.startswith('.'):
        continue
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
        # 去掉文件名的后缀
        name_without_extension = os.path.splitext(filename)[0]
        
        # 获取维基百科页面
        page = wiki_wiki.page(name_without_extension)
        
        # 获取简介
        summary = page.summary if page.exists() else '无简介'
        
        # 插入数据到Excel
        ws.append([idx, name_without_extension, summary])
        print(f"已处理文件: {filename}, 序号: {idx}, 作品名称: {name_without_extension}")

# 保存Excel文件
wb.save(excel_filename)
print(f"Excel文件已保存为 {excel_filename}")