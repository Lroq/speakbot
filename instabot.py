from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException

# Chemin relatif du chromedriver
chromedriver_path = 'chromedriver-win64/chromedriver.exe'

# Utilisation de Service pour spécifier le chemin du chromedriver
service = Service(chromedriver_path)

# Initialisation du WebDriver avec le service spécifié
try:
    driver = webdriver.Chrome(service=service)
except WebDriverException as e:
    print(f"Erreur lors du lancement du WebDriver : {e}")
    exit(1)

# Vos identifiants Instagram
username = "louis.rques"
password = "nkYb2@meScOuilleS.com"

def start():
    try:
        driver.get("https://www.instagram.com/")
        print("Instagram ouvert")

        # Attendez que le champ de connexion soit chargé
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Remplir les champs de connexion et se connecter
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)

        # Cliquez sur le bouton de connexion
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Log In']"))
        )
        login_button.click()

        # Ajoutez ici d'autres actions après la connexion
        # ...

    except TimeoutException as e:
        print(f"Le chargement de la page a pris trop de temps : {e}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

start()

# Gardez cette ligne pour fermer le navigateur à la fin de votre script
# driver.quit()
