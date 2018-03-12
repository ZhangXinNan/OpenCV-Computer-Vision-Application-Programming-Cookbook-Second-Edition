# test
```
// 创建 Harris 检测器实例
HarrisDetector harris;

// 计算机 Harris 值
harris.detect(image);

// 检测 Harris 角点
std::vector<cv::Point> pts;
harris.getCorners(pts, 0.02);
// 画出 Harris 角点
```

# detect
```

```

# getCorners(std::vector<cv::Point> &points, double qualityLevel)
```
    // Get the corner map
    cv::Mat cornerMap= getCornerMap(qualityLevel);
    // Get the corners
    // getCorners(std::vector<cv::Point> &points, const cv::Mat& cornerMap)
    getCorners(points, cornerMap);
```

