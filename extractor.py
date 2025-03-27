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

teamPath = "//html/body/div[1]/div[2]/div/button[1]"
battlePath = "//html/body/div[1]/div[2]/div/button[2]"
vsPath = "//html/body/div[1]/div[2]/div/button[3]"
zombiePath = "//html/body/div[1]/div[2]/div/button[4]"

allPath = [teamPath, battlePath, vsPath, zombiePath]

def pageRead(desiredPath):
    multiplayer_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", desiredPath)))
    multiplayer_button.click()
    driver.implicitly_wait(20)
    spans = driver.find_elements("xpath", "//html/body/div[1]/div[5]/div/div")
    for elem in spans:
        allPlayers = elem.text

    result = [ ]
    cur = [ ]

    for i in range(len(allPlayers)):
        if ((allPlayers[i] == '🟢' or allPlayers[i] == '⚪') and len(cur) > 0):
            cs = ''.join(cur)
            result.append(cs)
            cur = []
        elif (allPlayers[i] == '🟢' or allPlayers[i] == '⚪'):
            continue
        else:
            cur.append(allPlayers[i])

    for elem in result:
        print(elem)

for i in range(4):
    pageRead(allPath[i])
