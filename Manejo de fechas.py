# datetime - fecha y hora exacta
import datetime

my_time =  datetime.datetime.now()

print(my_time)


# solo la fecha actual
import datetime
my_day = datetime.date.today()

print(my_day)

# aceeder alas diferentes partes de las fechas
import datetime
my_day = datetime.date.today()
print(f'year: {my_day.year}')
print(f'month: {my_day.month}')
print(f'day: {my_day.day}')

# formato de fechas
from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d,%m,%Y')
print(f'formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m,%d,%Y')
print(f'formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'formato Random: {my_str}')

