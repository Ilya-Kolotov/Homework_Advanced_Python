"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os
import shutil


def sorted_files(source_dir: str):
    video_extensions = ['.mp4', '.avi', '.mov']
    image_extensions = ['.jpg', '.png', '.gif']
    text_extensions = ['.txt', '.doc', '.pdf']
    for file in os.listdir(source_dir):
        filename, extension = os.path.splitext(file)
        if extension.lower() in video_extensions:
            destination_dir = 'Video'
            if not os.path.exists(os.path.join(source_dir, destination_dir)):
                os.mkdir(os.path.join(source_dir, destination_dir))
        elif extension.lower() in image_extensions:
            destination_dir = 'Image'
            if not os.path.exists(os.path.join(source_dir, destination_dir)):
                os.mkdir(os.path.join(source_dir, destination_dir))
        elif extension.lower() in text_extensions:
            destination_dir = 'Text'
            if not os.path.exists(os.path.join(source_dir, destination_dir)):
                os.mkdir(os.path.join(source_dir, destination_dir))
        else:
            continue
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(source_dir, destination_dir, file)
        shutil.move(source_path, destination_path)


source_dir = '.\Test1'
sorted_files(source_dir)
