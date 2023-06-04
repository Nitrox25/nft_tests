import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os
from webdriver_manager.chrome import ChromeDriverManager

# Получение полного пути к текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def browser():
    print("\nStart browser...")
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-profiles-outside-user-dir')
    # options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    path_to_extension = os.path.join(current_directory, 'nkbihfbeogaeaoehlefnkodbefgpgknn')
    options.add_argument('load-extension=' + path_to_extension)

    path_to_profile = os.path.join(current_directory, 'profile')
    options.add_argument('user-data-dir=' + path_to_profile)
    options.add_argument('--profile-directory=Profile_6')

    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=options)
    yield driver
    print("\nClose browser...")
    driver.quit()
