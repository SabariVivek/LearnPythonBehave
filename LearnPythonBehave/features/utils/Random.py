from faker import Faker

faker = Faker()


def random_first_name():
    return faker.first_name()


def random_last_name():
    return faker.last_name()


def random_email():
    return faker.email()


def random_password():
    return faker.password()
