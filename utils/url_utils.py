# url_utils.py
import os


def generate_base_url(service_type='api'):
    APP_TYPE = os.environ.get('APP_TYPE', 'member')
    TEST_ENV = os.environ.get('TEST_ENV', 'default_value_if_not_set')
    SUBDOMAIN = os.environ.get('SUBDOMAIN', 'default_subdomain')
    CLUSTER = os.environ.get('CLUSTER', 'default_cluster')
    DOMAIN = os.environ.get('DOMAIN', 'teladoc.io')

    if service_type == 'api':
        return f"https://tas.{SUBDOMAIN}.{CLUSTER}.{DOMAIN}/"
    elif service_type == 'application':
        return f"https://{APP_TYPE}.{SUBDOMAIN}.{CLUSTER}.{DOMAIN}/"
    else:
        raise ValueError("Invalid service_type. Choose either 'api' or 'application'.")
