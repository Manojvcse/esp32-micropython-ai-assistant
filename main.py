import network
import time
import urequests
import json

SSID = "Samsung Galaxy F12"
PASSWORD = "manoj519"

PUTER_TOKEN = "IsImlhdCI6MTc3MTYwMDA0MX0.ETWoZchDSPbm4sr_evV_X2PkViHxMETREeip9g3h9QQ"

URL = "https://api.puter.com/puterai/openai/v1/chat/completions" 

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...!")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("WiFi Connected")
    print("IP:", wlan.ifconfig())
def ask_ai(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + PUTER_TOKEN
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        res = urequests.post(
            URL,
            headers=headers,
            data=json.dumps(data)
        )
        response = res.json()
        ai_message = response["choices"][0]["message"]["content"]
        print("\nAI:", ai_message)
        res.close()
    except Exception as e:
        print("Error:", e)
connect_wifi()
while True:
    user = input("\nYou: ")
    if user.lower() == "exit":
        print("Bye!")
        break
    ask_ai(user)
