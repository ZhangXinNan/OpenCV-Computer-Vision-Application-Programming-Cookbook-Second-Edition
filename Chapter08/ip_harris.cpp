/*------------------------------------------------------------------------------------------*\
   This file contains material supporting chapter 8 of the cookbook:  
   Computer Vision Programming using the OpenCV Library 
   Second Edition 
   by Robert Laganiere, Packt Publishing, 2013.

   This program is free software; permission is hereby granted to use, copy, modify, 
   and distribute this source code, or portions thereof, for any purpose, without fee, 
   subject to the restriction that the copyright notice may not be removed 
   or altered from any source or altered source distribution. 
   The software is released on an as-is basis and without any warranties of any kind. 
   In particular, the software is not guaranteed to be fault-tolerant or free from failure. 
   The author disclaims all warranties with regard to this software, any use, 
   and any consequent failure, is purely the responsibility of the user.
 
   Copyright (C) 2013 Robert Laganiere, www.laganiere.name
\*------------------------------------------------------------------------------------------*/

#include <iostream>
#include <vector>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
// #include <opencv2/features2d/features2d.hpp>
#include <opencv2/objdetect/objdetect.hpp>
// #include <opencv2/nonfree/features2d.hpp>
#include <opencv2/features2d/features2d.hpp>

#include "harrisDetector.h"

int main()
{
	// Harris:

	// Read input image
	cv::Mat image= cv::imread("../images/church01.jpg",0);
	if (!image.data)
		return 0; 

    // Display the image
	cv::namedWindow("Original");
	cv::imshow("Original",image);

	// Detect Harris Corners
	cv::Mat cornerStrength;
	cv::cornerHarris(image, // input image
					 cornerStrength, // 角点强度的图像
		             3,     // neighborhood size
					 3,     // aperture size
					 0.01); // Harris parameter

   // threshold the corner strengths
	cv::Mat harrisCorners;
	double threshold= 0.0001; 
	cv::threshold(cornerStrength,harrisCorners,
                 threshold,255,cv::THRESH_BINARY_INV);

    // Display the corners
	cv::namedWindow("Harris");
	cv::imshow("Harris",harrisCorners);

	// Create Harris detector instance
	HarrisDetector harris;
    // Compute Harris values
	harris.detect(image);
    // Detect Harris corners
	std::vector<cv::Point> pts;
	harris.getCorners(pts,0.02);
	// Draw Harris corners
	harris.drawOnImage(image,pts);

    // Display the corners
	cv::namedWindow("Corners");
	cv::imshow("Corners",image);

}