from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://territorial.io"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get(url)
multiplayer_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", "//html/body/button[1]")))
multiplayer_button.click()

driver.implicitly_wait(20)
spans = driver.find_elements("xpath", "//html/body/div[1]/div[5]/div/div")
for elem in spans:
    s = elem.text

res = [ ]
cur = [ ]

for i in range(len(s)):
    if ((s[i] == '🟢' or s[i] == '⚪') and len(cur) > 0):
        cs = ''.join(cur)
        res.append(cs)
        cur = []
    elif (s[i] == '🟢' or s[i] == '⚪'):
        continue
    else:
        cur.append(s[i])

for elem in res:
    print(elem)
