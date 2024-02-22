from src.webpage import WebPageAssistant


def test_title(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.press_skip_button()

    assert main_page.get_page_title() == "Delassus Group"


def test_legals(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.press_skip_button()
    main_page.go_to_legals()

    assert delassus_browser.current_url == "https://delassus.com/en/legals"


def test_reject_cookies(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.reject_cookies()
    main_page.press_skip_button()

    assert main_page.get_page_title() == "Delassus Group"


def test_learn_more_link(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.learn_more()

    assert delassus_browser.current_url == "https://delassus.com/en/legals"


def test_ru_locale(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.press_skip_button()
    main_page.switch_ru()

    assert main_page.get_current_page() == "https://delassus.com/ru/"


def test_title_ru_locale(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.press_skip_button()
    main_page.switch_ru()

    assert main_page.get_page_title() == "Группа компаний Delassus"


def test_about(delassus_browser):
    main_page = WebPageAssistant(delassus_browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.press_skip_button()
    main_page.press_burger()
    main_page.press_about()

    assert main_page.get_current_page() == "https://delassus.com/en/about"
