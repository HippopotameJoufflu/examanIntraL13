"""
Exercice n#1:
À l’aide de sélénium webdriver, effectuer les tâches suivantes :
1- Se connecter au site : https://videotron.com/
2- Trouver le nombre d’images sur le site et l’afficher dans la console de votre éditeur de code.
3- Afficher la valeur de l’attribut « alt » des images du site dans la console.
4- Trouver le nombre de liens sur le site et l’afficher dans la console.
5- Trouver le nombre de liens dans la section « footer » du site et l’afficher dans la console.
6- Récupérer la valeur de l’attribut « href » de chaque lien dans la section « footer » du site et l’afficher dans la console.
7-Pousser le code de votre projet vers un dépôt « GitHub ».
8-Envoyer l’adresse de votre dépôt par mio pour la correction.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

#Precondition : Ouvrir une page Chrome
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)     #initialiser variable 'implicit wait'

#1 - Recupérer la page de videotron
driver.get("https://videotron.com/")
time.sleep(2)

#2 - Trouver le nombre d'images
nombreImages = driver.find_elements(By.XPATH, "//img")
print(f"Il y a {len(nombreImages)} images sur la page d'accueil.")
print()

#3 - Valeur attribut 'alt'
valeurAlt = driver.find_elements(By.XPATH, "//img[@alt]")
for image in nombreImages:
    valeurAlt = image.get_attribute("alt")
    #condition pour imprimer uniquement lorsqu'il y a une valeur pour l'attribut 'alt'
    if not(valeurAlt==""):
        print(f"Valeur de 'alt' : {valeurAlt}")
print()

#4 - Trouver le nombre de liens
nombreLiens = driver.find_elements(By.XPATH, "//a")
print(f"Il y a {len(nombreLiens)} liens sur cette page.")
print()

#5 - Trouver le nombre de liens dans <footer>
nombreLiensFooter = driver.find_elements(By.XPATH, "//footer//a")
print(f"Il y a {len(nombreLiensFooter)} de liens dans la section Footer.")
print()

#6 - Trouver la valeur de chaque lien dans <footer>
liensFooter = driver.find_elements(By.XPATH, "//footer//a")
for lienF in liensFooter:
    href = lienF.get_attribute("href")
    print(f"Lien : {href}")
print()