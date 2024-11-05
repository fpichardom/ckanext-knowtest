import re
import uuid
import ckan.plugins.toolkit as tk


def knowtest_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value

# Definition based on ckanext-canada extension
# https://github.com/open-data/ckanext-canada/blob/master/ckanext/canada/validators.py
# 143:153
def knowtest_validate_generate_uuid(value):
    """
    Accept UUID-shaped values or generate a uuid for this
    dataset early so that it may be copied into the name field.
    """
    if not value or value is tk.missing:
        return str(uuid.uuid4())
    try:
        return str(uuid.UUID(value))
    except ValueError:
        raise tk.Invalid(tk._("Badly formed hexadecimal UUID string"))

def get_validators():
    return {
        "knowtest_required": knowtest_required,
        "knowtest_validate_generate_uuid": knowtest_validate_generate_uuid,

    }