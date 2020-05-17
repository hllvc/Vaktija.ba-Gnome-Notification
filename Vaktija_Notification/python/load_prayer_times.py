import json,requests

with open("username") as the_file:
    username=the_file.read().replace('\n','')

content = requests.get("https://api.vaktija.ba/vaktija/v1/14")
prayer_times = json.loads(content.content)

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_location", "w+") as the_file:
    the_file.write(prayer_times["lokacija"])
    
with open("/home/" + username + "/.config/PrayerTimes/data/prayer_date", "w+") as the_file:
    the_file.write(prayer_times["datum"][0])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_gdate", "w+") as the_file:
    the_file.write(prayer_times["datum"][1])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_dawn", "w+") as the_file:
    the_file.write(prayer_times["vakat"][0])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_fajr", "w+") as the_file:
    the_file.write(prayer_times["vakat"][1])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_zuhr", "w+") as the_file:
    the_file.write(prayer_times["vakat"][2])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_asr", "w+") as the_file:
    the_file.write(prayer_times["vakat"][3])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_maghrib", "w+") as the_file:
    the_file.write(prayer_times["vakat"][4])

with open("/home/" + username + "/.config/PrayerTimes/data/prayer_isha", "w+") as the_file:
    the_file.write(prayer_times["vakat"][5])