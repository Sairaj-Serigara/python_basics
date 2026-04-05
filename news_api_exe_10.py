import requests

api_key = "4d4919b16b644e56878c1c3429629cf3"
url = f"https://newsapi.org/v2/everything?q=technology&language=en&apiKey={api_key}"

response = requests.get(url)
data = response.json()

print("Status Code:", response.status_code)

if data.get("status") == "ok":
    articles = data.get("articles", [])
    if articles:
        print("\n🗞️ Top Articles:\n")
        for article in articles[:5]:
            print("📰", article["title"])
            print("🔗", article["url"])
            print()
    else:
        print("No articles found.")
else:
    print("Error:", data)
