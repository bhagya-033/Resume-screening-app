import requests

def test_app():
    url = "http://127.0.0.1:5000"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("App main page is reachable.")
        else:
            print(f"App main page returned status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the app. Is it running?")

if __name__ == "__main__":
    test_app()
