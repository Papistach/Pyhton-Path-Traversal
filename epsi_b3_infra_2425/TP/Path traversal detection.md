# Détection automatisée de failles de type "Path Traversal"

Le path traversal (ou directory traversal) est une vulnérabilité qui permet à un attaquant d'accéder à des fichiers ou dossiers en dehors du répertoire racine prévu de l'application. Ce type de vulnérabilité peut être utilisé pour lire des fichiers sensibles tels que /etc/passwd sur des systèmes Linux ou C:\Windows\System32\ sur Windows.  

Développez un script Python capable de détecter automatiquement ce type de faille sur un serveur web.

## Consignes

### Analyser un serveur web cible

- Vous disposez d’un serveur de test à l’adresse http://localhost:8080
- Ce serveur contient un répertoire "public" qui est censé être le seul accessible depuis l'extérieur
- Cependant, le serveur est vulnérable à des attaques de path traversal

### Développer le script de détection
        
- Le script doit envoyer des requêtes HTTP au serveur en utilisant différentes URL qui pourraient être vulnérables au path traversal
- Par exemple, des chemins comme /../../etc/passwd ou /../windows/system.ini peuvent être testés

### Analyse des réponses
        
Le script doit analyser les réponses HTTP renvoyées par le serveur :

- Si le code de retour est 200 OK et que le contenu suggère que des fichiers sensibles sont affichés (comme le contenu de /etc/passwd ou system.ini), cela indique une vulnérabilité
- Si le code de retour est 403 Forbidden ou 404 Not Found, le serveur semble protégé
- D'autres codes de retour peuvent être exploités (500, etc.)

### Rapport de vulnérabilité

- Le script doit générer un rapport (txt ou markdown) résumant les URL testées et indiquant si elles sont vulnérables ou sécurisées
- Pour chaque URL vulnérable détectée, le script doit lister l’URL et afficher un message d’alerte