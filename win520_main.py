from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime, random,time, logging, selenium
import sys



def process520(browser, jo):
    temp_jo = jo + 2

    time.sleep(1)

    browser.find_element_by_css_selector("#frm > div > ul.lotto720_select_wrapper > li.lotto720_group_wrapper > span:nth-child("+str(temp_jo)+") > label > span").click()
    #browser.execute_script("selJo("+ str(random.randrange(1, 8)) +")")
    time.sleep(2)
    # td_style_2_3 > input:nth-child(1)
    # lotto720_lottery_wrapper_bg > div > div.lotto720_auto_number_wrapper > a

    browser.find_element_by_css_selector("#lotto720_lottery_wrapper_bg > div > div.lotto720_auto_number_wrapper > a").click()
    time.sleep(2)
    #lotto720_lottery_wrapper_bg > div > div.lotto720_confirm_number_wrapper > a
    browser.find_element_by_css_selector("#lotto720_lottery_wrapper_bg > div > div.lotto720_confirm_number_wrapper > a").click()




def alert_accept(self, browser):
    try:
        alert = browser.switch_to_alert()
        alert.accept()
    except:
        pass



chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome("C:/app/chromedriver.exe", chrome_options=chrome_options)
browser.get("https://dhlottery.co.kr/user.do?method=login&returnUrl=")

try:
    id = ㅁㅁㅁㅁ # 사이트 계정 id
    pwd = ㅁㅁㅁㅁ # 사이트 계정 password
    buy_cnt = 5 # 구매할 수량

    time.sleep(3)

    input_id = browser.find_element_by_id("userId")
    input_id.send_keys(id)

    # 비밀번호 입력
    input_pass = browser.find_element_by_css_selector("#article > div:nth-child(2) > div > form > div > div.inner > fieldset > div.form > input[type=password]:nth-child(2)")
    input_pass.send_keys(pwd)

    browser.execute_script("check_if_Valid3();")

    time.sleep(3)

    print("status::login-on!!!!!!")

    money = browser.find_element_by_css_selector(
        "body > div:nth-child(1) > header > div > div.top_menu > form > div > ul.information > li > a:nth-child(2) > strong")
    sendTelegram(conn, "lotto money::"+str(money.text))
    momey_int = money.text.replace("원","")
    momey_int = int(momey_int.replace(",", ""))
    if momey_int < 5000:
        print("not-money!!!!")
        testeee.exee1ew() #일부러에러발생해서 종료시키기

    browser.get("https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LP32")

    browser.switch_to_default_content()
    browser.switch_to_frame(browser.find_element_by_css_selector("#container > iframe"))
    time.sleep(1)


    # 연금복권 구매
    for idx in range(int(buy_cnt)):
        jo = idx % 5;
        jo = jo +1
        process520(browser, jo)


    time.sleep(1)
    browser.find_element_by_css_selector("#frm > div > ul.lotto720_bottom_wrapper > li.lotto720_btn_pay_wrapper.pay > a").click()
    time.sleep(1)
    KUtil.alert_accept(browser)
    time.sleep(1)
    browser.find_element_by_css_selector("#lotto720_popup_confirm > div > div.lotto720_popup_bottom_wrapper.btn_area > a.btn_blue").click()
    time.sleep(3)
    browser.find_element_by_css_selector("#lotto720_popup_pay > div > div.lotto720_popup_bottom_wrapper > a").click()
    time.sleep(1)

    browser.execute_script("self.close();")
    time.sleep(2)


except Exception as e:
    logging.exception("error!!!")
finally:
    browser.close()
    browser.quit()
    sys.exit()



