import os
from pydub import AudioSegment

def convert_audio_files(folder_path, bitrate="128k", sample_rate=48000):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.mp3', '.wav')):
                file_path = os.path.join(root, file)
                base_name = os.path.splitext(file_path)[0]
                
                m4a_path = base_name + '.m4a'
                ogg_path = base_name + '.ogg'
                
                try:
                    audio = AudioSegment.from_file(file_path)
                    audio = audio.set_frame_rate(sample_rate)
                    
                    # Export to M4A
                    audio.export(m4a_path, format='ipod', bitrate=bitrate)
                    
                    # Export to OGG
                    audio.export(ogg_path, format='ogg', bitrate=bitrate)
                    
                    os.remove(file_path)
                    print(f"Converted and removed {file_path}")
                except Exception as e:
                    print(f"Error converting {file_path}: {e}")

# Replace 'your_folder_path' with the path to your folder
convert_audio_files('C:\XAMPP\htdocs\Phaser\Catharsis')
