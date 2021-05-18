link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_browser_add_button_check(browser):
    browser.get(link)
    button_text = browser.find_element_by_css_selector(".btn-add-to-basket").text
    assert button_text == "Añadir al carrito", f'expected "Añadir al carrito", got {button_text}'