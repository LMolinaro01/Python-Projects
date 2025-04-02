import customtkinter
import requests
import re

class CatFactApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fato sobre Gatos")
        self.label = customtkinter.CTkLabel(self, text="Fatos Sobre Gatos", font=("Consolas bold", 17))
        self.label.pack(padx=10, pady=10)
        
        self.geometry("400x300")

        self.label_fact = customtkinter.CTkLabel(self, text="Clique no botão para ver um fato!", wraplength=380)
        self.label_fact.pack(pady=20)
        
        self.button = customtkinter.CTkButton(self, text="Mostrar Fato", command=self.fetch_cat_fact)
        self.button.pack(pady=10)
    
    def fetch_cat_fact(self):
        url = "https://catfact.ninja/fact"
        try:
            response = requests.get(url)
            response.raise_for_status()
            match = re.search(r'"fact":"(.*?)"', response.text)
            if match:
                fact = match.group(1)
                translated_fact = self.translate_text(fact)
                self.label_fact.configure(text=translated_fact)
            else:
                self.label_fact.configure(text="Nenhum fato encontrado.")
        except requests.exceptions.RequestException:
            self.label_fact.configure(text="Erro ao buscar fato sobre gatos")
    
    def translate_text(self, text, source="en", target="pt"):
        translate_url = "https://api.mymemory.translated.net/get"
        params = {"q": text, "langpair": f"{source}|{target}"}
        
        try:
            response = requests.get(translate_url, params=params)
            response.raise_for_status()
            return response.json().get("responseData", {}).get("translatedText", text)
        except requests.exceptions.RequestException:
            return "Erro na tradução"

if __name__ == "__main__":
    app = CatFactApp()
    app.mainloop()