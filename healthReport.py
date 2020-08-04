'''
1、使用Chrome浏览器，需要添加chromedriver.exe
2、python要安装selenium
'''

from selenium import webdriver
import time


def LoginZJU(url, username, password):
    driver = webdriver.Chrome()
    driver.get(url)
    name = driver.find_element_by_id("username")
    name.send_keys(username)
    name = driver.find_element_by_id("password")
    name.send_keys(password)
    login_button = driver.find_element_by_id("dl")
    login_button.click()
    return driver


def SetInfo(driver):
    time.sleep(5)
    driver.find_element_by_name("area").click()
    time.sleep(3)
    sfzx_btn = driver.find_element_by_xpath("//div[@name='sfzx']/div/div[2]")
    sfzx_btn.click()
    time.sleep(0.5)
    jrdqtlqk_btn = driver.find_element_by_xpath("//div[@name='jrdqtlqk']/div/div[3]")
    act = driver.find_element_by_xpath("//div[@name='jrdqtlqk']/div/div[3]/span").get_attribute('class')
    if not (act == "active"):
        jrdqtlqk_btn.click()
    elif (act == "active"):
        time.sleep(0.5)

    sfsqhzjkk_btn = driver.find_element_by_xpath("//div[@name='sfsqhzjkk']/div/div[1]")
    sfsqhzjkk_btn.click()
    time.sleep(0.5)

    healthcodecolor_btn = driver.find_element_by_xpath("//div[@name='sqhzjkkys']/div/div[1]")
    healthcodecolor_btn.click()
    time.sleep(0.5)

    sfymqjczrj_btn = driver.find_element_by_xpath("//div[@name='sfymqjczrj']/div/div[2]")
    sfymqjczrj_btn.click()
    time.sleep(0.5)

    sfqrxxss_btn = driver.find_element_by_xpath("//div[@name='sfqrxxss']/div/div")
    sfqrxxss_btn.click()
    time.sleep(0.5)
    submit_btn = driver.find_element_by_class_name("footers")
    submit_btn.click()
    time.sleep(0.5)

    conform_btn = driver.find_element_by_xpath("//div[@class='wapcf-btn-box']/div[2]")
    #conform_btn.click()
    time.sleep(0.5)

    # 4)-确认提交成功
    #success_btn = driver.find_element_by_xpath("//div[@class='alert']/div")
    #success_btn.click()

    #print('Success Submit info.')


if __name__ == '__main__':
    url = 'https://healthreport.zju.edu.cn/ncov/wap/default/index'

    username = ''
    password = ''

    driver = LoginZJU(url, username, password)

    SetInfo(driver)