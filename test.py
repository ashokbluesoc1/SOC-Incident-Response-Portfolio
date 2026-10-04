import os
import requests

API_KEY = os.getenv("VT_API_KEY")

if not API_KEY:
    print("Error: VT_API_KEY environment variable is not set.")
    exit()

headers = {
    "x-apikey": API_KEY
}

ips = [
    "8.8.8.8",
    "1.1.1.1",
    "8.8.4.4"
]

for ip in ips:

    print("\n" + "=" * 40)
    print("Investigating:", ip)
    print("=" * 40)

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        print("HTTP status:", response.status_code)

        if response.status_code != 200:
            print("Unable to retrieve VirusTotal data.")
            continue

        data = response.json()

        attributes = data.get("data", {}).get("attributes", {})

        country = attributes.get("country", "Unknown")
        owner = attributes.get("as_owner", "Unknown")

        stats = attributes.get("last_analysis_stats", {})

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)

        print("Country:", country)
        print("Owner:", owner)
        print("Malicious:", malicious)
        print("Suspicious:", suspicious)

        if malicious >= 1 or suspicious >= 1:
            print("🚨 Investigation needed!")
        else:
            print("No malicious/suspicious detections found.")

    except requests.RequestException as error:
        print("Request failed:", error)

    except ValueError:
        print("Invalid JSON response from VirusTotal.")