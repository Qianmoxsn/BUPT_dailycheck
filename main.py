from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import xlrd

data = xlrd.open_workbook_xls("data.xls")
st1 = data.sheet_by_index(0)
location = st1.cell_value(0, 1)
account = st1.cell_value(1, 1)
password = st1.cell_value(2, 1)
print("驱动位置：", location)
print("账号：", account)
print("密码：", password)
driver = webdriver.Edge(executable_path=location)
driver.get(r'https://app.bupt.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fsite%2Fncov%2Fxisudailyup')


def login(username, password):
    login_url = driver.current_url
    username_tag = driver.find_element(by=By.XPATH, value="//*[@id='app']/div[2]/div[1]/input")
    password_tag = driver.find_element(by=By.XPATH, value="//*[@id='app']/div[2]/div[2]/input")
    username_tag.send_keys(username)
    password_tag.send_keys(password)
    btn = driver.find_element(by=By.XPATH, value="//*[@id='app']/div[3]")
    btn.click()
    report_url = driver.current_url
    while report_url == login_url:
        report_url = driver.current_url
        sleep(2)
    print("登陆成功: ", report_url)
    return True


def report():
    # 位置选择
    btn_location = driver.find_element(by=By.XPATH,
                                       value="/html/body/div[1]/div[1]/div/section/div[4]/ul/li[4]/div/input")
    btn_location.click()
    sleep(3)
    # 点击提交
    btn_submit = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/section/div[5]/div/a")
    btn_submit.click()
    sleep(1)
    # 确认提交
    btn_has_submit = driver.find_element(by=By.XPATH, value="//*[@id='wapcf']/div/div[2]/div[2]")
    btn_has_submit.click()
    print("打卡成功")


if __name__ == '__main__':

    if login(account, password) is True:
        report()

    sleep(5)
    driver.close()
