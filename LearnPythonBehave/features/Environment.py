from selenium import webdriver


def before_all(context):
    print("<<<<< Before All >>>>>")


def after_all(context):
    print("<<<<< After All >>>>>")


def before_feature(context, feature):
    print("<<<<< Before Feature >>>>>")


def after_feature(context, feature):
    print("<<<<< After Feature >>>>>")


def before_scenario(context, scenario):
    print("<<<<< Before Scenario >>>>>")
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    print("<<<<< After Scenario >>>>>")
    context.driver.close()


def before_step(context, step):
    print("<<<<< Before Step >>>>>")


def after_step(context, step):
    print("<<<<< After Step >>>>>")


def before_tag(context, tag):
    print("<<<<< Before Tag >>>>>")


def after_tag(context, tag):
    print("<<<<< After Tag >>>>>")
