def enter(context, locator, value):
    context.driver.find_element(*locator).send_keys(value)


def click(context, locator):
    context.driver.find_element(*locator).click()


def get_text(context, locator):
    return context.driver.find_element(*locator).text
