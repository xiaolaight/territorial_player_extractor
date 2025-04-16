from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github import Github
from github import Auth
import time

# a basic web scraper to get player information and log their username and time logged in
# add the desired tracked names into the names.txt within the repo
# information will be recorded down in the detect.txt within the repo

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

tok = "YOUR AUTH TOKEN" #generate this by cloning the repository and using your auth token

auth = Auth.Token(tok)
g = Github(auth=auth)
repo = g.get_repo("xiaolaight/territorial_player_extractor")
userList = repo.get_contents("names.txt")
names = str(userList.decoded_content)
targetUsers = names.split('`')
del targetUsers[0]
targetUsers.pop()

def pageRead(desiredPath):
    multiplayer_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", desiredPath)))
    multiplayer_button.click()

    spans = driver.find_element("xpath", "//html/body/div[1]/div[5]/div/div")

    allPlayers = ""

    try:
        allPlayers = spans.text
        print(allPlayers)
    except:
        pass

    cur = [ ]

    for i in range(len(allPlayers)):
        if ((allPlayers[i] == '🟢' or allPlayers[i] == '⚪') and len(cur) > 0):
            cs = ''.join(cur)
            for j in targetUsers:
                if j in cs:
                    outputFile = repo.get_contents("detect.txt")
                    originalText = str(outputFile.decoded_content.decode("utf-8"))
                    newText = "User " + cs + " detected at " + str(time.ctime()) + " with keyword " + j + "  \n"
                    repo.update_file(outputFile.path, "NEW COMMIT", f"{originalText} {newText}", outputFile.sha)
            cur = []
        elif (allPlayers[i] == '🟢' or allPlayers[i] == '⚪'):
            continue
        else:
            cur.append(allPlayers[i])

def runAll():
    while True:
        for i in range(0, 4):
            pageRead(allPath[i])
        time.sleep(5)

runAll()
