import urllib.request
import urllib.error
import json
import codecs

#current conditions
f = urllib.request.urlopen('http://api.wunderground.com/api/82697598ac328253/geolookup/conditions/q/NC/Durham.json')
reader = codecs.getreader("utf-8")
json_string = reader(f)
parsed_json = json.load(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
weather = parsed_json['current_observation']['weather']
pressure_trend = parsed_json['current_observation']['pressure_trend']
print ("""The current temperature in %s is %s. It is %s.\n
\n
The pressure is %s.""" % (location, temp_f, weather, pressure_trend))
f.close()