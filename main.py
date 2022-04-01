from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

Edoptions = webdriver.EdgeOptions
Edoptions.add_argument('--no-sandbox')
Edoptions.add_argument('window-size=1920x1080')
Edoptions.add_argument('--disable-gpu')
Edoptions.add_argument('--headless')

location = "msedgedriver.exe"
account = os.environ["BUPT_USERNAME"]
password = os.environ["BUPT_PASSWORD"]
print("**驱动位置：", location)
print("**账号：", account)
print("**密码：", password)

driver = webdriver.Edge(executable_path=location, options=Edoptions)

driver.get(r'https://auth.bupt.edu.cn/authserver/login?service=https%3A%2F%2Fapp.bupt.edu.cn%2Fa_bupt%2Fapi%2Fsso'
           r'%2Fcas%3Fredirect%3Dhttps%253A%252F%252Fapp.bupt.edu.cn%252Fsite%252Fncov%252Fxisudailyup%26from%3Dwap')


def login(username, password):

    driver.switch_to.frame("loginIframe")
    login_url = driver.current_url
    username_tag = driver.find_element(by=By.ID, value="username")
    password_tag = driver.find_element(by=By.ID, value="password")
    username_tag.send_keys(username)
    password_tag.send_keys(password)
    btn = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[3]/div[1]/div[7]/input")
    btn.click()
    report_url = driver.current_url
    while report_url == login_url:
        report_url = driver.current_url
        sleep(1)
    print("\n\n登陆成功: ", report_url)
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
    sleep(0.5)
    # 确认提交
    btn_has_submit = driver.find_element(by=By.XPATH, value="//*[@id='wapcf']/div/div[2]/div[2]")
    btn_has_submit.click()
    print("\n\n!!打卡成功!!")


if __name__ == '__main__':

    if login(account, password) is True:
        report()

    sleep(1)
    driver.close()

