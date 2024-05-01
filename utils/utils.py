from godaddypy import Account, Client
import requests


class Utils:
    def __init__(self, api_key, api_secret):
        self.account = Account(api_key, api_secret)

    # Make sure to define or import the classes `Account` and `Client` to fully implement this code.
    # Class that contains all the utility functions
    def getCurrentIp(self):
        response = requests.get('https://api.ipify.org')
        response.raise_for_status()  # Raise an exception if the request fails
        return response.text

    def configureGodaddy(self, ip, domain_name):
        client = Client(self.account)
        return client.update_ip(ip, "A", [domain_name])

    def storeCurrentIp(self, ip):
        with open('current_ip.txt', 'w') as f:
            f.write(ip)
        return True

    def getStoredIp(self):
        try:
            with open('current_ip.txt', 'r') as f:
                return f.read()
        except Exception as e:
            return f"{e}"

    def notify(self, subject, message):
        # Implementation for a notification service can go here, e.g., email or SMS.
        # For now, let's simulate a notification being sent successfully:
        print(f"Notification sent: {subject} - {message}")
        return True
