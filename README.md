# Win520 Buy Bot
Simple Python for Win520 buy


# What is it?

연금복권 사이트에서 무작위 연금복권을 구매하는 간단한 Python 모듈

## Main Features

1. 로그인 기능
```id = ㅁㅁㅁㅁ # 사이트 계정
pwd = ㅁㅁㅁㅁ # 사이트 계정 password
buy_cnt = 5 # 구매할 수량
time.sleep(3)
input_id = browser.find_element_by_id("userId")
input_id.send_keys(id)
input_pass = browser.find_element_by_css_selector("#article > div:nth-child(2) > div > form > div > div.inner > fieldset > div.form > input[type=password]:nth-child(2)")
input_pass.send_keys(pwd)
browser.execute_script("check_if_Valid3();")
```

2. Alert창 없애기위한 함수
```
def alert_accept(self, browser):
	try:
		alert = browser.switch_to_alert()
		alert.accept()
	except:
		pass
```

3. 연근복권 무작위 번호 선택 
```
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
   ```

4. 연금복권 구매버튼 자동 클릭 
```
browser.find_element_by_css_selector("#frm > div > ul.lotto720_bottom_wrapper > li.lotto720_btn_pay_wrapper.pay > a").click()
    time.sleep(1)
    KUtil.alert_accept(browser)
    time.sleep(1)
    browser.find_element_by_css_selector("#lotto720_popup_confirm > div > div.lotto720_popup_bottom_wrapper.btn_area > a.btn_blue").click()
    time.sleep(3)
    browser.find_element_by_css_selector("#lotto720_popup_pay > div > div.lotto720_popup_bottom_wrapper > a").click()
```

## Installation
- selenium 에서 사용할 크롬드라이브 다운로드
  - https://chromedriver.chromium.org/downloads
- Python 모듈인 selenium 설치 
  - pip install selenium
