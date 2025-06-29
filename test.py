import os
import zipfile
# from natsort import natsorted
import re

def natural_sort_key(s):
    """实现特定排序规则：数字按自然���序，但带前导零的数字排在相同值的数字之前"""
    def convert(text):
        if text.isdigit():
            num_val = int(text)
            # 如果是以0开头的数字，返回一个特殊的元组使其排在普通数字之前
            if text.startswith('0') and len(text) > 1:
                return (num_val - 0.5, text)
            return (num_val, text)
        return text.lower()

    return [convert(p) for p in re.split('([0-9]+)', s)]

def batch_rename_images(zip_file_path, txt_file_path, output_dir="output"):
    """
    从ZIP文件中批量重命名PNG图片为TXT文件中的名称

    参数:
        zip_file_path (str): ZIP文件路径
        txt_file_path (str): 包含新文件名的TXT文件路径
        output_dir (str): 输出目录，默认为"output"
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 读取新文件名
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        new_names = [line.strip() for line in f if line.strip()]

    # 解压ZIP文件并处理PNG文件
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 获取所有PNG文件并按原始顺序排序
        # lst = [f for f in zip_ref.namelist() if f.lower().endswith('.png')]
        png_files = sorted([f for f in zip_ref.namelist() if f.lower().endswith('.png')],key=natural_sort_key)
        # png_files = windows_sort_key(lst)

        # 验证文件数量匹配
        if len(png_files) != len(new_names):
            raise ValueError(f"PNG文件数量({len(png_files)})与新文件名数量({len(new_names)})不匹配")

        # 逐个处理并重命名文件
        for i, (old_name, new_name) in enumerate(zip(png_files, new_names)):
            # 构建新文件名（添加.png扩展名）
            new_file_name = f"{new_name}.png"

            # 解压并保存为新名称
            with zip_ref.open(old_name) as src, open(os.path.join(output_dir, new_file_name), 'wb') as dst:
                dst.write(src.read())

            print(f"已重命名: {old_name} -> {new_file_name}")

    print(f"\n✅ 重命名完成！共处理 {len(png_files)} 个文件")
    print(f"👉 处理后的文件保存在: {os.path.abspath(output_dir)}")


if __name__ == "__main__":
    # 配置参数（使用原始字符串避免转义问题）
    ZIP_FILE = r"D:\Desktop\作业.zip"
    TXT_FILE = r"D:\Desktop\作业\新建文本文档.txt"

    # 执行批量重命名
    batch_rename_images(ZIP_FILE, TXT_FILE)