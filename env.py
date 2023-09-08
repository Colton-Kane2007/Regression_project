user = 'robinson_2285'
host = 'data.codeup.com'
password = '7UNuickyqxVrGk0vKJPTEF2fy6Qpg1Dg'

def create_url(user, host, password, db):
    return f'sql+pymysql://{user}:{password}@{host}/{db}'

url = 'sql+pymysql://robinson_2285:7UNuickyqxVrGk0vKJPTEF2fy6Qpg1Dg@data.codeup.com/employees'
