#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# OpenCV提供了许多边缘检测滤波函数，
# 如Laplacian(), Sobel()以及Scharr(),
# 这些滤滤函数会将非边缘区域转为黑色，将边缘区域转为白色或其他饱和的颜色

# 但它们又很容易将噪声错误地识别为边缘。解决方案就是在找到边缘之前对图像进行模糊处理

# OpenCV提供的模糊滤波函数，
# 如blur(),medianBlur()以及GaussianBlur()

# Canny 边缘检测
# 检测步骤：
# 使用高斯滤波器
# 对图像进行去噪、
# 计算梯度、
# 在边缘上使用非最大抑制（NMS）、
# 在检测到的边缘上使用双（double）阈值去除假阳性，
# 最后分析所有的边缘及其之间的连接，
# 以保留真正的边缘并消除不明显的边缘

import numpy as np
import pandas as pd
import cv2

img = cv2.imread("C.png", 0)
cv2.imwrite(
    "canny.jpg",
    cv2.Canny(img, 200, 300)
)
cv2.imshow(
    "canny",
    cv2.imread("canny.jpg")
)
cv2.waitKey()
cv2.destroyAllWindows()