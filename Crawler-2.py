import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import csv

def recup_info_video(browser, url, plage):
    if not isinstance(browser, selenium.webdriver.firefox.webdriver.WebDriver):
        raise TypeError("browser doit être de type webdriver")

    browser.get(url)
    # time.sleep(2)

    # try:
    #     myElem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, ".//h1[@class='title style-scope ytd-video-primary-info-renderer']/yt-formatted-string")))
    # except Exception as e :
    #     print(e)

    while True : 
        try :

            infos = {}
            titre = browser.find_element(By.XPATH, ".//h1[@class='title style-scope ytd-video-primary-info-renderer']/yt-formatted-string")
            vues = browser.find_element(By.XPATH, ".//div[@id='info']//span[@class='view-count style-scope ytd-video-view-count-renderer']")
            videos_suivantes_elements = []
            while len(videos_suivantes_elements) < plage :
                videos_suivantes_elements = browser.find_elements(By.XPATH, ".//div[@class='style-scope ytd-watch-next-secondary-results-renderer'][2]/ytd-compact-video-renderer//a[not(@id='thumbnail')]")
                # print("Je recup les elements")
            

            infos['Titre'] = titre.get_attribute('innerHTML')
            infos['URL'] = url
            infos['Vues'] = int( vues.get_attribute('innerHTML')[:vues.get_attribute('innerHTML').find("view")-1].replace(",", "") )
            infos['Suivant'] = []
            for e in videos_suivantes_elements[:plage] :
                    # print("Fonction info : ", e.get_attribute('href'))
                    infos['Suivant'].append(e.get_attribute('href'))


            return infos
        except Exception as e :
            # print(e)
            pass


def ecrire_resultats(chemin, vids, premiere_iteration = False):
    print("Debut d'ecriture, ne surtout pas fermer le programme")

    f = open(chemin, 'a')

    writer = csv.writer(f)

    if premiere_iteration == True :
        writer.writerow(vids[0].keys())

    for vid in vids :
        try :
            writer.writerow(vid.values())
        except UnicodeEncodeError:
            vid['Titre'] = "Erreur d'encodage"
            writer.writerow(vid.values())





    f.close()
    print("C'est bon on peut fermer")


def crawl(video_initiale, crawl_depth, plage, browser, chemin, checkpoint = 100):
    videos_rencontrees = [] #Liste contenant les infos de toutes les vidéos rencontrées

    nouvelles_videos = [video_initiale]
    compteur = 0
    total = 0

    for i in range(crawl_depth+1):

        video_a_regarder = nouvelles_videos.copy()
        nouvelles_videos = []

        # print("video à regarder : ", video_a_regarder)



        for url in video_a_regarder :
            infos_video = recup_info_video(browser, url, plage)
            videos_rencontrees.append(infos_video)
            compteur += 1
            # print("Suivant : ", infos_video['Suivant'])
            nouvelles_videos += infos_video['Suivant']
            if compteur >= checkpoint :
                if total == 0:
                    ecrire_resultats(chemin, videos_rencontrees, True)
                else :
                    ecrire_resultats(chemin, videos_rencontrees)
                total += compteur
                compteur = 0
                print("Nb total de vidéos rencontrées : ", total)
                videos_rencontrees = []

    
    ecrire_resultats(chemin, videos_rencontrees)
    

def main():

    video_initiale = "https://www.youtube.com/watch?v=uY0pn-YTgSw"
    crawl_depth = 6
    plage = 5
    chemin_fichier_resultat = "resultats.csv"

    #NB de video pour 4/5 -> 781 (total avec les videos sans lien -> 3906)


    # for e in os.scandir():
    #     print(e)
    browser = webdriver.Firefox('C:\Program Files\Python39\Scripts\geckodriver-0.31.0')
    browser.get("https://www.youtube.com")

    file = open(chemin_fichier_resultat, "w" )
    file.close

    time.sleep(2)
    
    # cookie_accept_button = browser.find_elements(By.XPATH, ".//*[@id='dialog']//*[@id='text']")[3]

    # print("resultat", cookie_accept_button)

    # print("Click")
    # cookie_accept_button.click()

    time.sleep(1)

    crawl(video_initiale, crawl_depth, plage, browser, chemin_fichier_resultat, 5)
    
    # nouvelles_videos = [video_initiale]

    # for i in range(crawl_depth+1):

    #     video_a_regarder = nouvelles_videos.copy()
    #     nouvelles_videos = []

    #     for url in video_a_regarder :
    #         infos_video = recup_info_video(browser, url, plage)
    #         videos_rencontrees.append(infos_video)
    #         nouvelles_videos += infos_video['Suivant']

    
    







def test():
    browser = webdriver.Firefox('Firefox')
    if isinstance(browser, selenium.webdriver.firefox.webdriver.WebDriver):
        print("ok")
    else :
        print("Pas ok")



if __name__ == '__main__':
    main()

    