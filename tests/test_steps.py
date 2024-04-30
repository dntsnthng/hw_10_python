import allure
from selene import by, browser, be
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()


    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 87"):
        s(by.partial_text("#87")).should(be.visible)

