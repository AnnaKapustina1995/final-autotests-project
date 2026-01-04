import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="UI language: en, es, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    yield browser
    browser.quit()
