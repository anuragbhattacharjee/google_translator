# from mtranslate import translate
from writefile import writefile
from readfile import readfile
from fileLocation import fileLocation
from languages import LANGUAGES
import urllib
from googleapiclient.discovery import build

# translator = Translator()
# print(LANGUAGES)
intents = readfile('en/intent.txt')
# print(intents)
service = build('translate', 'v2',
            developerKey='AIzaSyCN5X2fEWsdO4jRSgwB_PZ3v_0A4HbmXCY')

for key, value in LANGUAGES.items():
    print (key, value)
    list = []
    translated = service.translations().list(
      source='en',
      target=key,
      q=intents
    ).execute()
    for tranlation in translated['translations']:
        list.append(tranlation['translatedText'])

    # break
    writefile(key, list)
    # print(key + ' : ' , list)
    # break