# Video Editing Script Readme

Ce script Python utilise la bibliothèque MoviePy pour automatiser la création de vidéo tiktok d'une minute avec une vidéo stimulante en bas de la vidéo.

## Installation des Dépendances

1. Assurez-vous d'avoir Python installé sur votre système. Si ce n'est pas le cas, téléchargez et installez Python à partir du [site officiel](https://www.python.org/).

2. Installez les dépendances requises en exécutant les commandes suivantes dans votre terminal ou invite de commande :

   ```bash
   pip install moviepy
   pip install Pillow==9.5.0
   ```

3. Installez également ImageMagick en suivant les instructions spécifiques à votre système d'exploitation. Vous pouvez télécharger ImageMagick depuis [leur site officiel](https://imagemagick.org/script/download.php).

## Utilisation du Script

1. **Préparation des Fichiers :** Placez les fichiers vidéo que vous souhaitez traiter dans le dossier spécifié par la variable `in`.

2. **Ajout de Clips Additionnels :** Ajoutez des clips vidéo supplémentaires dans le dossier spécifié par la variable `assets/clip`. Ces clips seront les vidéo "stimulante" en bas de l'écran.
3. **Exécution du Script :** Exécutez le script Python en utilisant la commande suivante dans votre terminal ou invite de commande :

   ```bash
   python tiktok.py
   ```
4. **Temps d'execution** : Dépend de la longueur de la video en entrée et de votre configuration de pc.
4. **Résultats :** Les vidéos générées seront sauvegardées dans le dossier spécifié par la variable `out`.
