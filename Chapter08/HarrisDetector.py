#encoding=utf8

import numpy as np
import cv2

class HarrisDetector:
    '''Harris 角点检测器类'''
    __cornerStrength = None    # Mat   角点强度图像
    __cornerTh = None           # Mat   阈值化角点图像
    __localMax = None           # Mat   局部最大值图像
    __neighbourhood = 3         # int   平滑导数的邻域尺寸 
    __aperture = 3              # int   梯度计算的口径
    __k = 0.01                  # double Harris 参数
    __maxStrength = 0.0         # double 阈值计算的最大强度
    __threshold = 0.01          # double 计算得到的阈值
    __nonMaxSize = 3            # int    非极大抵制的领域尺寸
    __kernel = None             # Mat    非极大抑制的内核

    def __init__(self, neighbourhood=3, aperture=3, k=0.1,
                    maxStrength=0.0, threshold=0.01, nonMaxSize=3):
        self.__neighbourhood = neighbourhood
        self.__aperture = aperture
        self.__k = k
        self.__maxStrength = maxStrength
        self.__threshold = threshold
        self.__nonMaxSize = nonMaxSize
        self.setLocalMaxWindowSize(nonMaxSize)

    def setLocalMaxWindowSize(self, nonMaxSize):
        '''创建用于非最值抑制的内核'''
        self.__nonMaxSize = nonMaxSize
        # C++
        # kernel.create(nonMaxSize, nonMaxSize, CV_8U)
        # PYTHON ???

    def detect(self, image):
        '''计算harris角点'''
        # 计算Harris
        self.__cornerStrength = cv2.cornerHarris(image, self.__neighbourhood, self.__aperture, self.__k)
        # 计算内部阈值
        _, self.__maxStrength, _, _ = cv2.minMaxLoc(self.__cornerStrength)

        # 检测局部最大值
        kernel = np.uint8(np.zeros((3, 3)))
        for i in range(3):
            kernel[1, i] = kernel[i, 1] = 1
        dilated = cv2.dilate(self.__cornerStrength, kernel)
        self.__localMax = cv2.compare(self.__cornerStrength, dilated, cv2.CMP_EQ)
    
    def getCornerMap(self, qualityLevel):
        '''用Harris值得到角点分布图'''
        # 对角点强度阀值化
        threshold = qualityLevel * self.__maxStrength
        _, self.__cornerTh = cv2.threshold(self.__cornerStrength, threshold, 255, cv2.THRESH_BINARY)

        # 转换成8位图像
        cornerMap = self.__cornerTh.astype(np.uint8)

        # 非极大值抑制
        cornerMap = cv2.bitwise_and(cornerMap, self.__localMax)
        return cornerMap
    
    def getCorners(self, cornerMap):
        points = []
        for y in range(cornerMap.shape[0]):
            for x in range(cornerMap.shape[1]):
                if cornerMap[y, x]:
                    points.append((x, y))
        return points
    
    def drawOnImage(self, image, points, color=(255, 255, 255), radius=3, thickness=1):
        for pt in points:
            cv2.circle(image, pt, radius, color, thickness)
        return image

if __name__ == '__main__':
    filename = "../images/church01.jpg"

    image = cv2.imread(filename, 0)
    image_show = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    harris = HarrisDetector()
    # 计算Harris角点
    harris.detect(image)
    # 检测Harris角点
    cornerMap = harris.getCornerMap(0.2) # 0.02
    pts = harris.getCorners(cornerMap)
    # 画出Harris角点
    harris.drawOnImage(image_show, pts, color=(0, 0, 255), radius=7)
    cv2.imshow('src gray', image)
    cv2.imshow('corners', image_show)
    cv2.waitKey(15000)
    cv2.destroyAllWindows()
