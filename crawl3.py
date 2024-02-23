from tabnanny import check
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
import time
import sys
import os
import csv
import ast


def recup_info_video(browser, url, plage, depth):
    if not isinstance(browser, selenium.webdriver.firefox.webdriver.WebDriver):
        raise TypeError("browser doit être de type webdriver")

    while True:
        try :
            browser.get(str(url) + "&has_verified=1")
            break
        except :
            pass
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
            nom_chaine = browser.find_element(By.XPATH, './/div[@class="style-scope ytd-video-secondary-info-renderer"]//div[@class="style-scope ytd-channel-name" and @id="text-container"]//a')
            abonnes = browser.find_element(By.XPATH, './/div[@class="style-scope ytd-video-secondary-info-renderer"]//yt-formatted-string[@id="owner-sub-count"]')
            nom_chaine.location_once_scrolled_into_view
            compteurMeta = 0
            while compteurMeta<30:
                try :
                    date_vid = browser.find_element(By.XPATH, './/meta[@itemprop="datePublished"]')
                    ff = browser.find_element(By.XPATH, './/meta[@itemprop="isFamilyFriendly"]')
                    genre = browser.find_element(By.XPATH, './/meta[@itemprop="genre"]')
                    keyword = browser.find_element(By.XPATH, './/meta[@name="keywords"]')
                    #
                    infos['Date'] = date_vid.get_attribute('content')
                    infos['FamilyFriendly'] = ff.get_attribute('content')
                    infos['Genre'] = genre.get_attribute('content')
                    #
                    break
                except :
                    compteurMeta+=1
            if compteurMeta==30:
                print("erreur meta")
                infos["Date"]="2000-12-12"
                infos["Genre"]="erreur"
                infos["FamilyFriendly"]="none"
                    
                    
            pas_de_com = 0
            while True :
                #print()
                if pas_de_com > 20:
                    infos['Commentaires'] = "-1"

                    break
                try:
                    print("On boucle dans les commentaires")
                    commentaires = browser.find_element(By.XPATH, './/ytd-comments-header-renderer//yt-formatted-string[@class="count-text style-scope ytd-comments-header-renderer"]//span[@class="style-scope yt-formatted-string"][1]')
                    infos['Commentaires'] = commentaires.get_attribute('innerHTML').replace("\u202f", "")

                    # print("DEBUG : On boucle dans les commentaires")

                    break
                except Exception as e:
                    print(e)
                    # print("Avant 2eme try")

                    try :
                        print("2eme try")
                        commentaires = browser.find_element(By.XPATH, './/ytd-comments[@id="comments"]//yt-formatted-string[@id="message"]//span')
                        infos['Commentaires'] = commentaires.get_attribute('innerHTML').replace("\u202f", "")
                        print("2eme try")
                        break
                        
                    except:

                        pas_de_com += 1
                        print(url, "Except du 2eme try")

                        pass

                    pass
            print("après le while")
            videos_suivantes_elements = []
            
            compteur = 0
            while compteur < plage + 2 and len(videos_suivantes_elements) < plage : #permet d'attendre que le bon nombre de vidéos soient chargées dans la page
                print("on est la -------------------------")
                compteur += 1
                videos_suivantes_elements = browser.find_elements(By.XPATH, ".//div[@class='style-scope ytd-watch-next-secondary-results-renderer'][2]/ytd-compact-video-renderer//a[not(@id='thumbnail')]")
                # print("Je recup les elements")
            

            infos['Titre'] = titre.get_attribute('innerHTML')
            infos['URL'] = url
            infos['Vues'] = int( vues.get_attribute('innerHTML')[:vues.get_attribute('innerHTML').find(" ")].replace(",", "") )
            infos['Suivant'] = []
            infos['Profondeur'] = depth
            infos['Chaine'] = nom_chaine.get_attribute('innerHTML')
            infos['Abonnes'] = abonnes.get_attribute('innerHTML')
            #
            # infos['Date'] = date_vid.get_attribute('content')
            # infos['FamilyFriendly'] = ff.get_attribute('content')
            # infos['Genre'] = genre.get_attribute('content')
            # infos['Keywords'] = keyword.get_attribute('content')

            # print(infos['Commentaires'])
            # if infos['Abonnes'].find("M") == -1 :
            #     if infos['Abonnes'].find("k") == -1 :# Il y a ni k ni M
            #         # infos['Abonnes'] = infos['Abonnes'][:infos['Abonnes'].find("abo")].replace("&nbsp;", "").replace(",", "") 
            #         print("Pas k : ", infos['Abonnes'])
                    
            #     else : #Il y a k
            #         # infos['Abonnes'] = infos['Abonnes'][:infos['Abonnes'].find("k")+1].replace("&nbsp;", "").replace(",", ".")
            #         # infos['Abonnes'] = int (ast.literal_eval(infos['Abonnes']) * 1000)

            #         print("K : ", infos['Abonnes'])
            # else:
            #     # infos['Abonnes'] = infos['Abonnes'][:infos['Abonnes'].find("M")].replace("&nbsp;", "").replace(",", "")
            #     # infos['Abonnes'] = int (ast.literal_eval(infos['Abonnes']) * 1000000)
            #     print("M : ", infos['Abonnes'])
                



            print("DEBUG <-------------------")
            for e in videos_suivantes_elements[:plage] :
                    # print("Fonction info : ", e.get_attribute('href'))
                    infos['Suivant'].append(e.get_attribute('href'))


            return infos
        except Exception as e :
            print(e)
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
            try :
                vid['Titre'] = "Erreur d'encodage"
                writer.writerow(vid.values())
            except UnicodeEncodeError :
                vid['Chaine'] = "Erreur d'encodage"
                writer.writerow(vid.values())





    f.close()
    print("C'est bon on peut fermer")


def crawl(video_initiale, crawl_depth, plage, browser, chemin, checkpoint = 100):
    videos_rencontrees = [] #Liste contenant les infos de toutes les vidéos rencontrées

    nouvelles_videos = [video_initiale]
    compteur = 0
    total = 0
    depth = 0

    for i in range(crawl_depth+1):

        video_a_regarder = nouvelles_videos.copy()
        nouvelles_videos = []

        # print("video à regarder : ", video_a_regarder)



        for url in video_a_regarder :
            print("Recup une video")
            infos_video = recup_info_video(browser, url, plage, depth)
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
        
        depth += 1

    
    ecrire_resultats(chemin, videos_rencontrees)
    

def main():
    
    video_initiale = "https://www.youtube.com/watch?v=CIr8QIcpgi8"
    #video_initiale = "https://www.youtube.com/watch?v=QoBTr_CSMzs"
    # video_initiale = "https://www.youtube.com/watch?v=MgpOf1udE00"
    # video_initiale = "https://www.youtube.com/watch?v=pqZx5IY7cnY"
    # video_initiale = "https://www.youtube.com/watch?v=R55ACTWHvBY"


    crawl_depth = 6
    plage = 3
    chemin_fichier_resultat = "resultats.csv"
    checkpoint = 5

    #NB de video pour 4/5 -> 781 (total avec les videos sans lien -> 3906)


    # for e in os.scandir():
    #     print(e)
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument("start-maximized")
    # browser = webdriver.Firefox('Firefox')
    browser = webdriver.Firefox('C:\Program Files\Python39\Scripts\geckodriver-0.31.0', options=options)

    browser.get("https://www.youtube.com")

    file = open(chemin_fichier_resultat, "w" )
    file.close

    time.sleep(2)
    
    cookie_accept_button = browser.find_elements(By.XPATH, ".//*[@id='dialog']//*[@id='text']")[3]

    print("resultat", cookie_accept_button)

    print("Click")
    cookie_accept_button.click()

    time.sleep(1)

    crawl(video_initiale, crawl_depth, plage, browser, chemin_fichier_resultat, checkpoint)
    
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

