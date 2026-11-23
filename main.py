'''
1 час = 60*60 = 3600сек
2 часа = 7200 сек
'''
import math #подключаем библиотеку
seconds_in_a_day2 = 24*60*60
seconds2 = 4210 # это 1 час 1 минута 1 секунда_ до конца дня 22 часа 59 мин 59 сек
hours = (seconds_in_a_day2-seconds2)//60//60 #часов до конца дня
print(f"Часы {hours}")
minutes = math.ceil((((seconds_in_a_day2-seconds2)/60/60)-hours)*60)
#hours2 = (seconds_in_a_day2-seconds2)//3600
print(f"Минуты {minutes}")
seconds_left = (seconds_in_a_day2-seconds2)%60%60
print(f"секунды {seconds_left}")
seconds_in_a_day = 24*60*60
print(f"Секунд в дне: {seconds_in_a_day}")
seconds = int(input("Введите время в секундах прошедшее сначала дня: "))
seconds_end_day = seconds_in_a_day - seconds #сколько секунд до конца дня
minutes_end_day = seconds_end_day/60 #сколько минут до конца дня
hours_end_day = minutes_end_day/60 #сколько часов до конца дня
print(f"До конца дня осталось: {hours_end_day} часов\n"
      f"или {minutes_end_day} минут\n"
      f"или {seconds_end_day} секунд")
