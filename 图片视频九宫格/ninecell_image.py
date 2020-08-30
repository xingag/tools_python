#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: ninecell_image.py 
@time: 2020-08-28 22:20 
@description：九宫格图片朋友圈
"""

from PIL import Image


class ImageObj(object):
    def __init__(self):
        pass

    def start(self, file_path):
        # 1、打开图片
        image = Image.open(file_path)

        # 2、将图片填充为正方形，组成：原图+百底+正方形
        image = self.__fill_image(image)

        # 保存图片
        image.save('temp.jpg')

        # 3、裁剪合成后图片，为9张图片
        nine_images = self.__cut_image(image)

        # 4、保存9张图片到本地
        self.save_images(nine_images)

    def __cut_image(self, image):
        """
        把一张图片裁剪成9张图片的坐标值，然后进行裁剪成小图片
        :return:
        """
        width, height = image.size

        # 6000
        print('原图的宽/高分别为:', width, height)

        # 2000
        # 每张图片的宽度
        item_width = int(width / 3)

        print('裁剪后的宽度为:', item_width)

        box_list = []

        for i in range(0, 3): 
            for j in range(0, 3):
                # 坐标值分别是：左、上、右、底
                box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
                print(box)
                box_list.append(box)

        # 裁剪图片
        image_list = [image.crop(box) for box in box_list]

        return image_list

    def __fill_image(self, image):
        """
        将图片填充为正方形
        :param image:
        :return:
        """
        width, height = image.size

        # 长和宽较大值，作为新图片的宽高
        new_image_length = width if width > height else height

        # 生成新图片[纯白底]
        new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')

        # 将之前的图粘贴在新图上，居中
        # 如果原图宽大于高（横图），则填充图片的竖直维度
        if width > height:
            # (x,y)二元组表示粘贴上图相对下图的起始位置
            new_image.paste(image, (0, int((new_image_length - height) / 2)))
        else:
            # 如果原图宽小于高（竖图），则填充图片的水平纬度
            new_image.paste(image, (int((new_image_length - width) / 2), 0))
        return new_image

    def save_images(self, nine_images):
        """
        保存图片
        :param nine_images:
        :return:
        """
        index = 1
        for image in nine_images:
            image.save('result/' + str(index) + '.jpg')
            index += 1


if __name__ == '__main__':
    # 图片路径
    image_file_path = './raw/pic.jpg'
    image_obj = ImageObj()
    image_obj.start(image_file_path)
