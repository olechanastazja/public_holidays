# public_holidays

Public Holidays ia an application that will present you holiday days in both Poland and Czech Republic.


## Installation

Although I recommend to use docker for local deployment it is also possible to run each command
manually. SQLite3 is being used as a database.

```bash
$ git clone https://github.com/olechanastazja/public_holidays.git
$ cd public_holidays
```

### Docker way

```bash
# docker-compose up -d
```

### Manual way 

```
$ virtualenv -p python3 venv/
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py loaddata countries.json
$ python3 manage.py collectstatic
$ python3 manage.py runserver
```
 