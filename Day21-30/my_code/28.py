"""
Python 处理图像
"""

from PIL import Image
image = Image.open('guido.jpg')
# 通过 Image 对象的 format 属性获取图像的格式
print(image.format)
print(image.size)
print(image.mode)
image.show()