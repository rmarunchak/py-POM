import factory
from factory import SubFactory, List, Dict


class PhoneNumberFactory(factory.Factory):
    class Meta:
        model = dict

    type = "home"
    number = factory.Faker('phone_number')
    extension = ""
    carrier = None
    iso3_country_code = "USA"


class AddressFactory(factory.Factory):
    class Meta:
        model = dict

    party_address_id = None
    state = factory.Faker('state_abbr')
    postal = factory.Faker('zipcode')
    country_cd = "USA"
    type = "home"
    address_line_1 = factory.Faker('street_address')
    address_line_2 = factory.Faker('secondary_address')
    city = factory.Faker('city')


class SecurityQuestionFactory(factory.Factory):
    class Meta:
        model = dict

    question_id = factory.Faker('random_digit_not_null')
    response = factory.Faker('word')


class RegistrationFactory(factory.Factory):
    class Meta:
        model = dict

    member_id = ""
    source_member_id = ""
    first_name = factory.Faker('first_name')
    middle_name = factory.Faker('last_name')
    last_name = factory.Faker('last_name')
    suffix = "Esq."
    status = "active"
    dob = factory.Faker('date_of_birth')
    gender = "male"
    language = "English"
    phone_numbers = List([SubFactory(PhoneNumberFactory)])
    addresses = List([SubFactory(AddressFactory)])
    email_address = factory.Faker('email')
    email_address_confirmation = factory.SelfAttribute('email_address')
    username = factory.Faker('user_name')
    password = "Test123456"
    password_confirmation = factory.SelfAttribute('password')
    group_id = 501
    security_questions = List([SubFactory(SecurityQuestionFactory) for _ in range(3)])
    primary = True


# Example usage:
registration = RegistrationFactory()
print(registration)
