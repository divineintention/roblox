import requests
import time
import json

WEBHOOK_URL = "Put Your Discord Webhook Here"
LIMITED_ITEMS = {1111: "Limited 1", 2222: "Limited 2"} # put your actual limited IDs & names (whatever you want for the names)
PRICE_THRESHOLD = 5000
REFRESH_RATE = 60
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_limited_data(item_id):
    url = f"https://economy.roblox.com/v1/assets/{item_id}/resale-data"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def send_webhook(item_id, name, price, rap):
    payload = {
        "content": f"**{name}** is now **{price} Robux**! (RAP: {rap})\n[View Limited](https://www.roblox.com/catalog/{item_id})"
    }
    headers = {"Content-Type": "application/json"}
    requests.post(WEBHOOK_URL, json=payload, headers=headers)

def monitor_limiteds():
    while True:
        for item_id, name in LIMITED_ITEMS.items():
            data = get_limited_data(item_id)
            if data and (price := data.get("lowestPrice")) and price <= PRICE_THRESHOLD:
                send_webhook(item_id, name, price, data.get("recentAveragePrice", 0))
        time.sleep(REFRESH_RATE)

if __name__ == "__main__":
    monitor_limiteds()
