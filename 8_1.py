import re


def email_parse(email):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email):
        raise ValueError(f'wrong email: {email}')
    print(re_email.match(email).groupdict())


for i in ['someone@geekbrains.ru', 'someone@gbru', 's0m$one.ru']:
    try:
        email_parse(i)
    except ValueError as r:
        print(r)
