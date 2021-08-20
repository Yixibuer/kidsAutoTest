import os
from ocv.settings import Settings as ST
from page.ios_common_page import IosCommonPage
from utils import config


class PlayerPage(IosCommonPage):
    """player页面"""

    def check_brush_block(self):
        """验证画笔积木"""
        ST.IMG_DIR_PATH = os.path.join(ST.IMG_DIR_PATH, 'brush_block')
        brush_result = self.is_img_exists('brush.png', threshold=0.99)
        clear_brush_result = self.is_img_exists('clear_brush.png', threshold=0.99)
        return brush_result and clear_brush_result

    def touch_and_verify(self, touch_file, verify_file, touch_threshold=0.8, verify_threshold=0.85):
        # 点击图片
        self.touch(touch_file, threshold=touch_threshold)
        # 判断预期图片是否存在
        result = self.is_img_exists(verify_file, threshold=verify_threshold)
        return result

    def touch_and_close(self, touch_file, verify_file, touch_threshold=0.8, verify_threshold=0.85):
        # 点击积木,验证预期页面，并关闭预期页面
        result = self.touch_and_verify(touch_file, verify_file, touch_threshold, verify_threshold)
        self.touch_close_btn()
        return result

    def touch_close_btn(self, threshold=0.8):
        # 点击运算积木作品-关闭
        self.touch('close_btn.png', threshold=threshold)

    def check_calculation_block(self):
        """验证运算积木"""
        ST.IMG_DIR_PATH = os.path.join(ST.IMG_DIR_PATH, 'calculation_block')
        operator_result = self.touch_and_close('operator_btn.png', 'operator_page.png', touch_threshold=0.9,
                                               verify_threshold=0.976)
        l_page_result = self.touch_and_close('L_btn.png', 'L_page.png', touch_threshold=0.9, verify_threshold=0.99)
        power_result = self.touch_and_close('power_btn.png', 'power_page.png', verify_threshold=0.99)
        random_result = self.touch_and_close('random_btn.png', 'random_page.png', verify_threshold=0.99)
        x_result = self.touch_and_close('x_btn.png', 'x_page.png', verify_threshold=0.99)
        divide_result = self.touch_and_close('divide_btn.png', 'divide_page.png', verify_threshold=0.99)
        and_or_result = self.touch_and_close('andor_btn.png', 'andor_page.png', verify_threshold=0.99)
        other_operate_result = self.touch_and_close('other_operate_btn.png', 'other_operate_page.png',
                                                    verify_threshold=0.99)
        str_operate_result = self.touch_and_close('str_operate_btn.png', 'str_operate_page.png', verify_threshold=0.99)
        l2_page_result = self.touch_and_verify('l2_btn.png', 'L2page.png', touch_threshold=0.9, verify_threshold=0.99)
        self.swipe_to_left()
        operator_result2 = self.is_img_exists('operator_page.png', threshold=0.976)
        self.swipe_to_right()
        l2_page_result2 = self.is_img_exists('L2page.png', threshold=0.99)
        self.touch_close_btn()
        result_list = [operator_result, l_page_result, power_result, random_result, x_result, divide_result,
                       and_or_result, other_operate_result, str_operate_result, l2_page_result, operator_result2,
                       l2_page_result2]
        if False in result_list:
            return False
        return True

    def check_event_blocks(self):
        """验证事件积木"""
        ST.IMG_DIR_PATH = os.path.join(ST.IMG_DIR_PATH, 'event_blocks')
        self.touch('codemao1_btn.png', threshold=0.9)
        codemao1_page1_result = self.is_img_exists('codemao1_page1.png', threshold=0.96)
        codemao1_page2_result = self.is_img_exists('codemao1_page2.png', threshold=0.97)
        self.touch('codemao2_btn.png', threshold=0.9)
        codemao2_page1_result = self.is_img_exists('codemao2_page1.png', threshold=0.98)
        self.touch('codemao2_btn.png', threshold=0.9)
        codemao2_page2_result = self.is_img_exists('codemao2_page2.png', threshold=0.94)
        self.click_player_reset_btn()
        self.click_player_play_btn()
        self.touch('codemao3_btn.png', threshold=0.9)
        codemao3_page1_result = self.is_img_exists('codemao3_page1.png', threshold=0.94)
        self.touch('codemao3_btn.png', threshold=0.9)
        codemao3_page2_result = self.is_img_exists('codemao3_page2.png', threshold=0.95)
        result_list = [codemao1_page1_result, codemao1_page2_result, codemao2_page1_result, codemao2_page2_result,
                       codemao3_page1_result, codemao3_page2_result]
        if False in result_list:
            return False
        return True

    def check_appearance_blocks(self):
        """验证外观类积木"""
        # 设置文件路径
        ST.IMG_DIR_PATH = os.path.join(ST.IMG_DIR_PATH, 'appearance_blocks')
        codemao1_size = self.is_img_exists('codemao1_size.png', threshold=0.992)
        codemao1_colo1 = self.is_img_exists('codemao1_color1.png', threshold=0.995)
        codemao1_colo2 = self.is_img_exists('codemao1_color2.png', threshold=0.99)
        cm_transparent = self.is_img_exists('cm_transparent.png', threshold=0.99)
        cm_transparent2 = self.is_img_exists('cm_transparent2.png', threshold=0.99)
        cm_brightness = self.is_img_exists('cm_brightness.png', threshold=0.99)
        cm_brightness2 = self.is_img_exists('cm_brightness2.png', threshold=0.99)
        pixel = self.is_img_exists('pixel.png', threshold=0.99)
        pixel2 = self.is_img_exists('pixel2.png', threshold=0.99)
        ripple = self.is_img_exists('ripple.png', threshold=0.99)
        distortion = self.is_img_exists('distortion.png', threshold=0.982)
        distortion2 = self.is_img_exists('distortion2.png', threshold=0.99)
        cm_black = self.is_img_exists('cm_black.png', threshold=0.99)
        dialog1 = self.is_img_exists('dialog1.png', threshold=0.99)
        self.touch('next_btn.png', threshold=0.7)
        dialog2 = self.is_img_exists('dialog2.png', threshold=0.99)
        self.touch('next_btn.png', threshold=0.7)
        cm2_kuai = self.is_img_exists('cm2_kuai.png', threshold=0.99)
        #
        self.touch('input_btn.png', threshold=0.7)
        self.touch('123_btn.png', threshold=0.7)
        self.touch('567.png', threshold=0.9, times=3)
        self.touch('confirm_btn.png', threshold=0.9)
        cm2_666 = self.is_img_exists('cm2_666.png', threshold=0.992)
        result_list = [codemao1_size, codemao1_colo1, codemao1_colo2, cm_transparent, cm_transparent2, cm_brightness,
                       cm_brightness2, pixel, pixel2, ripple, distortion, distortion2, cm_black, dialog1, dialog2, cm2_666, cm2_kuai]
        if False in result_list:
            return False
        return True