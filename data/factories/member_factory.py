import factory
from factory import SubFactory, List, Dict
from faker import Faker
import datetime

fake = Faker()


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
    state = factory.Faker('state')
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


class CardFactory(factory.Factory):
    class Meta:
        model = dict

    @factory.lazy_attribute
    def card_type(self):
        return fake.random_element(elements=('Mastercard', 'Visa', 'Discover', 'American Express'))

    @factory.lazy_attribute
    def card_number(self):
        card_generators = {
            "Mastercard": fake.credit_card_number(card_type='mastercard'),
            "Visa": fake.credit_card_number(card_type='visa'),
            "Discover": fake.credit_card_number(card_type='discover'),
            "American Express": fake.credit_card_number(card_type='amex')
        }
        return card_generators[self.card_type]

    @factory.lazy_attribute
    def exp_month(self):
        return fake.random_element(elements=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'))

    @factory.lazy_attribute
    def exp_year(self):
        current_year = datetime.datetime.now().year
        future_year = current_year + fake.random_int(min=1, max=5)  # This will give a year 1 to 5 years in the future
        return str(future_year)


class MemberFactory(factory.Factory):
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
    group_id = 1
    security_questions = List([SubFactory(SecurityQuestionFactory) for _ in range(3)])
    primary = True
    card_details = SubFactory(CardFactory)
