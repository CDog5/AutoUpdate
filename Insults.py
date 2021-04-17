import requests,json,time,pyttsx3
engine = pyttsx3.init()
#uses an api and says insult with text-to-speech
while True:
    r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    data = json.loads(r.text)
    print(data["insult"])
    engine.say(data["insult"])
    engine.runAndWait()
    time.sleep(5)

