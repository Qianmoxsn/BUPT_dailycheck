from time import sleep
from selenium import webdriver

driver = webdriver.Edge()
driver.get(r'https://app.bupt.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fsite%2Fncov%2Fxisudailyup')


def login(username, password):
    login_url = driver.current_url
    username_tag = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/input")
    password_tag = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/input")
    username_tag.send_keys(username)
    password_tag.send_keys(password)
    btn = driver.find_element_by_xpath("//*[@id='app']/div[3]")
    btn.click()
    report_url = driver.current_url
    while report_url == login_url:
        report_url = driver.current_url
        sleep(3)
    print("登陆成功: ", report_url)
    return True


def report():
    # 位置选择
    btn_location = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[4]/div/input")
    btn_location.click()
    sleep(5)
    # 点击提交
    btn_submit = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[5]/div/a")
    btn_submit.click()
    sleep(1)
    # 确认提交
    btn_has_submit = driver.find_element_by_xpath("//*[@id='wapcf']/div/div[2]/div[2]")
    btn_has_submit.click()
    print("打卡成功")


if __name__ == '__main__':
    account = "****"
    password = "****"
    if login(account, password) is True:
        report()

    sleep(5)
    driver.close()
