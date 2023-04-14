from datetime import datetime

date_string = "2018-11-15T02:18:49Z"

format = "%Y-%m-%dT%H:%M:%SZ"

date = datetime.strptime(date_string, format)

now = datetime.now()
first_login = datetime.strptime('2023-04-12T23:54:37Z', format)
print(now)
print(first_login.date())
print((now.date() - first_login.date()).days)