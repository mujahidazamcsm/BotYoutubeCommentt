from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class YoutubeBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\user\Desktop\ig\geckodriver" #Local do arquivo que está o seu 'geckodriver'
        )
        
        
    
        
    def login(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dpt%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fchannel%252FUCUN9lhwfMJRxMVuet7Shg0w&hl=pt-BR&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
       
       #Email
        user_element = driver.find_element_by_xpath(
            "//input[@id='identifierId']")
        user_element.clear()
        user_element.send_keys(self.username)

        #confirmação no botão
        login_button = driver.find_element_by_xpath(
            "//span[@class='RveJvd snByac']"
        )
        login_button.click()
        time.sleep(3)

        #senha
        user_element = driver.find_element_by_xpath(
            "//input[@class='whsOnd zHQkBf']")
        user_element.clear()
        user_element.send_keys(self.password)
        time.sleep(2)

        #confirmação no botão
        login_button = driver.find_element_by_xpath(
            "//span[@class='RveJvd snByac']"
        )
        login_button.click()    
        time.sleep(2)
        self.comente_nos_videos_com_o_tema("Tema") # Altere aqui para o tema que você deseja pesquisar
            

    def comente_nos_videos_com_o_tema(self, tema):
        #links_de_posts = []
        driver = self.driver
        driver.get("https://www.youtube.com/results?search_query=" + tema )

        time.sleep(2)
       
        #confirmação do video
        login_button = driver.find_element_by_xpath("//a[@id ='video-title']")                    
        login_button.click()
        time.sleep(3)

        for i in range(1,40): 
           driver.execute_script("window.scrollTo(0,500);")
           time.sleep(2)
           driver.execute_script("window.scrollTo(0,400);")
           time.sleep(2)


           messages = ['comente o que você quiser!']
    
           comment = messages
  
  #comentando
           try:

            #time.sleep(random.randint(80,100))
            #driver.execute_script("window.scrollTo(0, 800)")
            #time.sleep(random.randint(10, 15))

                driver.find_element_by_xpath('//*[@id="simplebox-placeholder"]').click()
                time.sleep(random.randint(3,5))
                driver.find_element_by_xpath('//*[@id="contenteditable-root"]').send_keys(comment)
                time.sleep(random.randint(3,5))
                driver.find_element_by_xpath('//*[@id="contenteditable-root"]').send_keys(Keys.CONTROL + Keys.ENTER)
                time.sleep(random.randint(15,20))
            
           
           except Exception as e:
                print(e)
           driver.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]').click()
       
# Entre com o usuário e senha aqui

jhonatanBot = YoutubeBot("seu email","sua senha")
jhonatanBot.login()
