# url_utils.py
import os


def generate_base_url(service_type='api'):
    APP_TYPE = os.getenv('APP_TYPE', 'member')
    TEST_ENV = os.getenv('TEST_ENV')
    SUBDOMAIN = os.getenv('SUBDOMAIN', 'default_subdomain')
    CLUSTER = os.getenv('CLUSTER', 'default_cluster')
    DOMAIN = os.getenv('DOMAIN', 'teladoc.io')

    base_url = f"https://{APP_TYPE}.{SUBDOMAIN}.{CLUSTER}.{DOMAIN}/"
    if service_type == 'api':
        base_url = f"https://tas.{SUBDOMAIN}.{CLUSTER}.{DOMAIN}/"
    elif service_type != 'application':
        raise ValueError("Invalid service_type. Choose either 'api' or 'application'.")

    return base_url
