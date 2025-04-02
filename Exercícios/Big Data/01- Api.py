import customtkinter
import requests
import re

class CatFactApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fato sobre Gatos")
        self.geometry("400x200")

        self.label_fact = customtkinter.CTkLabel(self, text="Clique no botão para ver um fato!", wraplength=380)
        self.label_fact.pack(pady=20)
        
        self.button = customtkinter.CTkButton(self, text="Mostrar Fato Sobre Gatos", command=self.fetch_cat_fact)
        self.button.pack(pady=10)
    
    def fetch_cat_fact(self):
        url = "https://catfact.ninja/fact"
        payload = {}
        headers = {
        'accept': 'application/json',
        'X-CSRF-TOKEN': 'T2LLl57yrMTiuxrgT8AOraPWQ04vspL37TQuxsLJ',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6InNnUHc3WndNK3Z1V09FcTBuWHZ2dGc9PSIsInZhbHVlIjoidVRGV3huZWtNMUFMamJiV3ZrVjYwSkd4QXJxVk94OFZmNW1kcnVmWU9VTzE4RzVZdllUM2p1dlJYd1ZZYkpodldRbHE0aC9nRDR5d2xRTnNMUWhzWlRYL2ZRLy9kdEdSWkZoQnUzVE4rKzI3OHgvVDJPdS9GSmNWTjN3ekNqMDIiLCJtYWMiOiI1M2EwMWVjODMwNWMyYWIzNzRiNTQ5ZTBhNGFiMDc3ZGU1NDJkYWMyMDdkMTBlMDc2MThiYzBiZTk1MDRhNTZhIiwidGFnIjoiIn0%3D; catfacts_session=eyJpdiI6IjFHc1JIMjJSM3NiMFZZRnF0eWtxVlE9PSIsInZhbHVlIjoiaWMwemg4MlZLcmg3aSttYlBoRUltSUJtUnhBTTNmUjV5N1g4VzloaFpOT2xDR3FEN2FldTRGKzRkOThPaytPTDRHZzl3Q3pTWnc2ZDVBRHVVa0NwZ0pSR1RKemJ4UWFTV1RqVm1hVG5KY3pESTk1RGtYVllEZmdoUUZRb3pBKzkiLCJtYWMiOiIwZDU1YjI0OTQ0NWJjNzM1NDFjYmM0MTExODNlZDQ2YjJmOTZjMzZmZmY2YzU4NmEyYTljNThiMWQ0YjI2OGE2IiwidGFnIjoiIn0%3D; cw7uQ5jXpHmePfotcjZIXSWwxFbTEyxKnqJFMteI=eyJpdiI6Ijc2aE5Ec0JsYWM0QWhra1hvZnhabHc9PSIsInZhbHVlIjoiYnMzVTZ3SlJJTDVLdUR2M3cxMENxaUJ4UE5EYzlRY1MrR0xId0dVeFBYcGxoNkxnMFI5SnNES25Da0cvNnhtSlV3OE9QS25iQWxSMVpOaUx6SU9ZcW9UbUR5d3lBSnJ0Tngvblp6VXAwbml5N0xsV0xTa2JERG9SZGVKZDdUeWlvZ0JEb0grdkFTSU5qV2NKUldNbmZYWk9TVTZOZzZuRUhVWUFiTnRUMWZYMFpoUlQ1bjNRYjNOblhhWU05NHU5dmU1RzMvckxja1EwbUR5WEJTVjlEcFBrdkF5OFJSU2FHZlgvSzlDNVdZanExUlB1V3BrdUFSSzhOVTJ5YlkxSkhrYkhURnQ2bFlOejJDRmxlZ0haSVZrZTdEQWMrVVBMUXdxeDNLckVCV2NYd2RSSHowZVJpYzZ3K2daUnVtT1FuVHNHZ3hVVWtDNkdpNloxdlNuZFpoNjRaTllGZ0ZkVkpoMjJUUXB6QVJ2NlZVbkljOGFxMkNWSitGU3hROW1zIiwibWFjIjoiYjc5OTJiODk5MGYxYzEzOWE1N2NjYzNhZDE3NmFjODc4MGQ0YWVkZDIwMWI1N2MxMzgxZmRkOWYzMDUxYjY0ZiIsInRhZyI6IiJ9'
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            match = re.search(r'"fact":"(.*?)"', response.text)
            if match:
                fact = match.group(1)
                self.label_fact.configure(text=fact)
        except requests.exceptions.RequestException:
            self.label_fact.configure(text="Erro ao buscar fato sobre gatos")

if __name__ == "__main__":
    app = CatFactApp()
    app.mainloop()