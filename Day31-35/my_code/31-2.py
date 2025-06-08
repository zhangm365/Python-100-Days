"""
并发编程
"""

import glob
import os
import threading
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

PREFIX = "thumbnails"

def generate_thumbnail(infile, size, format='PNG'):
    """生成指定图片的缩略图"""
    try:
        # 路径处理
        filename = os.path.basename(infile)
        name, ext = os.path.splitext(filename)

        # 输出目录
        os.makedirs(PREFIX, exist_ok = True)
        outfile = os.path.join(PREFIX, f'{name}_{size[0]}_{size[1]}{ext}')

        with Image.open(infile) as img:
            if not (isinstance(size, (tuple, list)) and len(size) == 2):
                raise ValueError("size 参数必须是包含两个整数的元组")

            img.thumbnail(size, Image.Resampling.LANCZOS)
            img.save(outfile, format=format)

        return True

    except FileNotFoundError:
        print(f"错误：文件{infile}不存在")
        return False
    except Image.UnidentifiedImageError:
        print(f"错误：无法识别的图片格式 - {infile}")
        return False
    except Exception as e:
        print(f"处理文件 {infile} 时发生未知错误：{str(e)}")
        return False


def main():
    """主函数"""

    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [
            executor.submit(generate_thumbnail, infile, (size, size))
            for infile in glob.glob('images/*.png')
            for size in (32, 64, 128)
        ]


if __name__ == '__main__':
    main()
