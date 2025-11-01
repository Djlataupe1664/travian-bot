# 🤖 Travian Bot (Discord)

Un bot Discord conçu pour le serveur **Knights Legion**, qui détecte automatiquement les coordonnées Travian au format **x/y** et fournit un lien direct vers la carte du serveur **TS4**.

---

## ⚙️ Commandes Slash

### `/coord coords: x/y`

Renvoie un lien direct vers la carte Travian.

**Exemple :**
/coord coords: -10/25

yaml
Copier le code

Le bot répondra :
> 🌍 Coordonnées : (-10, 25)  
> 🔗 [Voir sur la carte TS4](https://ts4.x1.international.travian.com/position_details.php?x=-10&y=25)

---

## 💬 Détection automatique

Le bot scanne tous les messages contenant des coordonnées (exemple : `100/-20`)  
et envoie automatiquement un lien vers la carte correspondante.

---

## 🧩 Configuration

### Variables d’environnement

| Nom | Description |
|-----|--------------|
| `DISCORD_TOKEN` | Le token de ton bot Discord (à ajouter sur Render, **jamais dans le code**) |

---

## 🚀 Déploiement sur Render

### 1️⃣ Préparer ton dépôt

Assure-toi d’avoir ces fichiers à la racine de ton projet :
bot.py
requirements.txt
README.md

less
Copier le code

### 2️⃣ Créer ton service Render

1. Connecte ton dépôt GitHub [`Djlataupe1664/travian-bot`](https://github.com/Djlataupe1664/travian-bot) sur [Render.com](https://render.com)
2. Clique sur **New + → Background Worker**
3. Configure :
   - **Build Command :**
     ```
     pip install -r requirements.txt
     ```
   - **Start Command :**
     ```
     python bot.py
     ```

### 3️⃣ Ajouter ta variable d’environnement

Dans l’onglet **Environment** de ton service Render :
- **Key :** `DISCORD_TOKEN`
- **Value :** ton token Discord (copié depuis le portail [Discord Developer](https://discord.com/developers/applications))

---

## 🟢 Lancement

Une fois déployé, ton bot sera automatiquement lancé et restera actif **24h/24**.  
Les logs de connexion s’afficheront dans l’onglet **Logs** sur Render.

---

## 💡 Auteur

Projet créé par **[@Djlataupe1664](https://github.com/Djlataupe1664)**  
✨ Bot Discord Travian pour le serveur **Knights Legion** – hébergé sur Render