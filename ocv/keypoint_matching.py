#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Detect keypoints with KAZE/AKAZE/BRISK/ORB.
No need for opencv-contrib module.
# keypoint_matching.py
"""

import cv2
from ocv.keypoint_base import KeypointMatching
from airtest.aircv.error import *  # noqa


class KAZEMatching(KeypointMatching):
    """KAZE Matching."""

    pass


class BRISKMatching(KeypointMatching):
    """BRISK Matching."""

    METHOD_NAME = "BRISK"  # 日志中的方法名

    def init_detector(self):
        """Init keypoint detector object."""
        self.detector = cv2.BRISK_create()
        # create BFMatcher object:
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING)  # cv2.NORM_L1 cv2.NORM_L2 cv2.NORM_HAMMING(not useable)


class AKAZEMatching(KeypointMatching):
    """AKAZE Matching."""

    METHOD_NAME = "AKAZE"  # 日志中的方法名

    def init_detector(self):
        """Init keypoint detector object."""
        self.detector = cv2.AKAZE_create()
        # create BFMatcher object:
        self.matcher = cv2.BFMatcher(cv2.NORM_L1)  # cv2.NORM_L1 cv2.NORM_L2 cv2.NORM_HAMMING(not useable)


class ORBMatching(KeypointMatching):
    """ORB Matching."""

    METHOD_NAME = "ORB"  # 日志中的方法名

    def init_detector(self):
        """Init keypoint detector object."""
        self.detector = cv2.ORB_create()
        # create BFMatcher object:
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING)  # cv2.NORM_L1 cv2.NORM_L2 cv2.NORM_HAMMING(not useable)


"""
Detect keypoints with BRIEF/SIFT/SURF.
Need opencv-contrib module.
keypoint_matching_contrib.py
"""


def check_cv_version_is_new():
    """opencv版本是3.0或4.0以上, API接口与2.0的不同."""
    if cv2.__version__.startswith("3.") or cv2.__version__.startswith("4."):
        return True
    else:
        return False


class BRIEFMatching(KeypointMatching):
    """FastFeature Matching."""

    METHOD_NAME = "BRIEF"  # 日志中的方法名

    def init_detector(self):
        """Init keypoint detector object."""
        # BRIEF is a feature descriptor, recommand CenSurE as a fast detector:
        if check_cv_version_is_new():
            # OpenCV3/4, star/brief is in contrib module, you need to compile it seperately.
            try:
                self.star_detector = cv2.xfeatures2d.StarDetector_create()
                self.brief_extractor = cv2.xfeatures2d.BriefDescriptorExtractor_create()
            except:
                import traceback
                traceback.print_exc()
                print("to use %s, you should build contrib with opencv3.0" % self.METHOD_NAME)
                raise NoModuleError("There is no %s module in your OpenCV environment !" % self.METHOD_NAME)
        else:
            # OpenCV2.x
            self.star_detector = cv2.FeatureDetector_create("STAR")
            self.brief_extractor = cv2.DescriptorExtractor_create("BRIEF")

        # create BFMatcher object:
        self.matcher = cv2.BFMatcher(cv2.NORM_L1)  # cv2.NORM_L1 cv2.NORM_L2 cv2.NORM_HAMMING(not useable)

    def get_keypoints_and_descriptors(self, image):
        """获取图像特征点和描述符."""
        # find the keypoints with STAR
        kp = self.star_detector.detect(image, None)
        # compute the descriptors with BRIEF
        keypoints, descriptors = self.brief_extractor.compute(image, kp)
        return keypoints, descriptors

    def match_keypoints(self, des_sch, des_src):
        """Match descriptors (特征值匹配)."""
        # 匹配两个图片中的特征点集，k=2表示每个特征点取出2个最匹配的对应点:
        return self.matcher.knnMatch(des_sch, des_src, k=2)


class SIFTMatching(KeypointMatching):
    """SIFT Matching."""

    METHOD_NAME = "SIFT"  # 日志中的方法名

    # SIFT识别特征点匹配，参数设置:
    FLANN_INDEX_KDTREE = 0

    def init_detector(self):
        """Init keypoint detector object."""
        # BRIEF is a feature descriptor, recommand CenSurE as a fast detector:
        if check_cv_version_is_new():
            # OpenCV3/4, sift is in contrib module, you need to compile it seperately.
            try:
                self.detector = cv2.xfeatures2d.SIFT_create(edgeThreshold=10)
            except:
                import traceback
                traceback.print_exc()
                raise NoModuleError(
                    "There is no %s module in your OpenCV environment, need contribmodule!" % self.METHOD_NAME)
        else:
            # OpenCV2.x
            self.detector = cv2.SIFT(edgeThreshold=10)

        # # create FlnnMatcher object:
        self.matcher = cv2.FlannBasedMatcher({'algorithm': self.FLANN_INDEX_KDTREE, 'trees': 5}, dict(checks=50))

    def get_keypoints_and_descriptors(self, image):
        """获取图像特征点和描述符."""
        keypoints, descriptors = self.detector.detectAndCompute(image, None)
        return keypoints, descriptors

    def match_keypoints(self, des_sch, des_src):
        """Match descriptors (特征值匹配)."""
        # 匹配两个图片中的特征点集，k=2表示每个特征点取出2个最匹配的对应点:
        return self.matcher.knnMatch(des_sch, des_src, k=2)


class SURFMatching(KeypointMatching):
    """SURF Matching."""

    METHOD_NAME = "SURF"  # 日志中的方法名

    # 是否检测方向不变性:0检测/1不检测
    UPRIGHT = 0
    # SURF算子的Hessian Threshold
    HESSIAN_THRESHOLD = 400
    # SURF识别特征点匹配方法设置:
    FLANN_INDEX_KDTREE = 0

    def init_detector(self):
        """Init keypoint detector object."""
        # BRIEF is a feature descriptor, recommand CenSurE as a fast detector:
        if check_cv_version_is_new():
            # OpenCV3/4, surf is in contrib module, you need to compile it seperately.
            try:
                self.detector = cv2.xfeatures2d.SURF_create(self.HESSIAN_THRESHOLD, upright=self.UPRIGHT)
            except:
                import traceback
                traceback.print_exc()
                raise NoModuleError(
                    "There is no %s module in your OpenCV environment, need contribmodule!" % self.METHOD_NAME)
        else:
            # OpenCV2.x
            self.detector = cv2.SURF(self.HESSIAN_THRESHOLD, upright=self.UPRIGHT)

        # # create FlnnMatcher object:
        self.matcher = cv2.FlannBasedMatcher({'algorithm': self.FLANN_INDEX_KDTREE, 'trees': 5}, dict(checks=50))

    def get_keypoints_and_descriptors(self, image):
        """获取图像特征点和描述符."""
        keypoints, descriptors = self.detector.detectAndCompute(image, None)
        return keypoints, descriptors

    def match_keypoints(self, des_sch, des_src):
        """Match descriptors (特征值匹配)."""
        # 匹配两个图片中的特征点集，k=2表示每个特征点取出2个最匹配的对应点:
        return self.matcher.knnMatch(des_sch, des_src, k=2)
