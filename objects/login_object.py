#!/usr/bin/env python
# encoding: utf-8
'''
  @author: zxl
  @file: test_login_object.py
  @time: 2022/3/28 16:27
  @desc:
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class LoginPage:
    def __init__(self,driver):
        self.user_elem=By.CSS_SELECTOR, '#login_email'
        self.pass_elem=By.CSS_SELECTOR, '[type="password"]'
        self.logbutton_elem=By.CSS_SELECTOR, '#loginsubm'
        self.logout_elem=By.LINK_TEXT,'退出'
        self.driver=driver
        self.allgroup_elem=By.LINK_TEXT,'群组'
        self.newgroup_elem=By.LINK_TEXT,'创建群组'
        self.photo_elem = By.LINK_TEXT, '相册'
        self.newphoto_elem=By.LINK_TEXT,'上传相片'
        self.select_phot_elem=By.ID,'album_name'
        self.switch_upload_method_elem=By.LINK_TEXT,'切换上传方式'
        self.upload_photo_elem=By.XPATH,'//tr[1]/td[1]/input[1]'
        self.upload_button_elem=By.NAME,'submit'



    def input_username(self,username):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.pass_elem).clear()
        if password==None:
            password=' '
        self.driver.find_element(*self.pass_elem).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.logbutton_elem).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_elem).click()
    #点击群组
    def click_groups(self):
        self.driver.find_element(*self.allgroup_elem).click()
    #点击相册
    def click_photos(self):
        self.driver.find_element(*self.photo_elem).click()
    #创建群组
    def create_new_group(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.newgroup_elem).click()
    #创建相册
    def create_new_photo(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.newphoto_elem).click()

    def select_photo(self,index):
        Select(self.driver.find_element(*self.select_phot_elem)).select_by_index(index)

    def switch_photo_method(self):
        self.driver.find_element(*self.switch_upload_method_elem).click()

    def upload_photos(self,path_addr):
        self.driver.find_element(*self.upload_photo_elem).send_keys(path_addr)

    def click_upload(self):
        self.driver.find_element(*self.upload_button_elem).click()