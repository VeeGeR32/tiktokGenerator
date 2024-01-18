from moviepy.editor import *
import time
import os
import random
input_folder = "in"
output_folder = "out"
output_prefix = "partie"
output_extension = ".mp4"
clip_folder = "assets/clip"

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)
start_time_total = time.time()
# Parcourir tous les fichiers dans le dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_filepath = os.path.join(input_folder, filename)
        print(f"Processing {input_filepath}...")
        output_video_folder = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}")
        clipMain = VideoFileClip(input_filepath).fx(afx.audio_normalize)

        # Calculate the dimensions for cropping
        original_width, original_height = clipMain.size
        target_width = original_height * 9 // 8
        crop_width = (original_width - target_width) // 2

        # Crop the video
        clipMain = clipMain.crop(x1=crop_width, x2=original_width - crop_width).resize((720, 640))

        # Découper la vidéo principale en segments d'une minute
        segment_duration = 60  # en secondes
        num_segments = int(clipMain.duration // segment_duration)

        # Créer le dossier de sortie pour la vidéo d'entrée
        os.makedirs(output_video_folder, exist_ok=True)

        # Boucle pour traiter chaque segment
        for i in range(num_segments):
            start_time_segment = time.time()

            start_time = i * segment_duration
            end_time = (i + 1) * segment_duration

            # Prendre un moment aléatoire d'une minute pour clipBot
            clipBot_filename = random.choice(os.listdir(clip_folder))
            clipBot_filepath = os.path.join(clip_folder, clipBot_filename)
            clipBot = VideoFileClip(clipBot_filepath, audio=False).fx(afx.audio_normalize)
            original_width_bot, original_height_bot = clipBot.size
            target_width_bot = original_height_bot * 9 // 8
            crop_width_bot = (original_width_bot - target_width_bot) // 2
            clipBot = clipBot.crop(x1=crop_width_bot, x2=original_width_bot - crop_width_bot).resize((720, 640))
            clipBot_start_time = random.uniform(0, clipBot.duration - 60)
            clipBot_end_time = clipBot_start_time + 60
            bot_clip = clipBot.subclip(clipBot_start_time, clipBot_end_time)

            # Découper la vidéo principale pour obtenir le segment
            segment_clip = clipMain.subclip(start_time, end_time)

            # Ajouter le texte pour ce segment
            text = TextClip(f"Partie {i+1}", size=(500, 100), color="white").set_position(("center", "top")).set_duration(10)

            # Combiner les éléments pour ce segment
            segment_clip_W_TXT = CompositeVideoClip([segment_clip, text])

            # Créer le tableau de clips pour ce segment
            combine = clips_array([[segment_clip_W_TXT], [bot_clip]])

            # Écrire le fichier de sortie pour ce segment
            output_segment_filename = f"{output_prefix}_{i+1}{output_extension}"
            output_segment_filepath = os.path.join(output_video_folder, output_segment_filename)
            combine.write_videofile(output_segment_filepath)

            # Fermer les clips
            combine.close()
            end_time_segment = time.time()
            elapsed_time_segment = (end_time_segment - start_time_segment)/60
            print(f"Partie {i+1} fini en {elapsed_time_segment:.2f} minutes.")

end_time_total = time.time()
elapsed_time_total = (end_time_total - start_time_total)/60
print(f"Toutes les parties finis en {elapsed_time_total:.2f} minutes.")