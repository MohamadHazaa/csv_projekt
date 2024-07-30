import pandas as pd
import os

# Pfad zum Ressourcenordner
resources_path = os.path.join(os.getcwd(), 'resources')

# CSV-Dateien einlesen
car_df = pd.read_csv(os.path.join(resources_path, 'car.csv'), delimiter=';')
motorcycle_df = pd.read_csv(os.path.join(resources_path, 'motorcycle.csv'), delimiter=';')

# Fehlende Spalten mit "unknown" auffüllen
car_df['used'] = 'unknown'
motorcycle_df['transmission'] = 'unknown'

# Datenrahmen kombinieren
combined_df = pd.concat([car_df, motorcycle_df], ignore_index=True)

# Kombinierte Daten in eine neue CSV-Datei schreiben
combined_df.to_csv(os.path.join(resources_path, 'combined.csv'), index=False, sep=';')

print("CSV-Dateien wurden erfolgreich kombiniert und gespeichert.")

