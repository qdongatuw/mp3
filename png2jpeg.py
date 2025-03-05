import music_tag
from PIL import Image
import io

# Load the MP3 file
mp3_file_path = "your_music_file.mp3"
audio = music_tag.load_file(mp3_file_path)

# Check if there's an embedded cover image
if 'art' in audio and audio['art']:
    # Extract the image data
    image_data = audio['art'][0].data

    # Convert PNG to JPEG if necessary
    image = Image.open(io.BytesIO(image_data))
    if image.format == "PNG":
        jpeg_buffer = io.BytesIO()
        image = image.convert("RGB")  # Convert to RGB to ensure compatibility
        image.save(jpeg_buffer, format="JPEG", quality=85)
        jpeg_data = jpeg_buffer.getvalue()

        # Replace the existing cover with the new JPEG format
        audio['art'] = jpeg_data
        audio.save(mp3_file_path)

print("Cover image converted to JPEG and saved successfully.")
