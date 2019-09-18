#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

'''
创建一个滑动条来控制检测直线的长度阈值，即大于该阈值的检测出来，小于该阈值的忽略
注意：这里用的函数是HoughLinesP而不是HoughLines，
因为HoughLinesP直接给出了直线的断点，在画出线段的时候可以偷懒
'''
import cv2
def HoughLinesP(minLineLength):
    global minLINELENGTH
    minLINELENGTH = minLineLength + 1
