from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

output = Path("assets/banner.png")
output.parent.mkdir(parents=True, exist_ok=True)
width, height = 1200, 320
image = Image.new("RGB", (width, height), color=(18, 36, 65))
draw = ImageDraw.Draw(image)
try:
    title_font = ImageFont.truetype("arial.ttf", 80)
    subtitle_font = ImageFont.truetype("arial.ttf", 36)
except Exception:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

line1 = "Movie Recommendation System"
line2 = "Content-Based Filtering with TF-IDF and Cosine Similarity"

bbox1 = draw.textbbox((0, 0), line1, font=title_font)
text_width = bbox1[2] - bbox1[0]
draw.text(((width - text_width) / 2, 70), line1, font=title_font, fill=(255, 255, 255))

bbox2 = draw.textbbox((0, 0), line2, font=subtitle_font)
text_width2 = bbox2[2] - bbox2[0]
draw.text(((width - text_width2) / 2, 180), line2, font=subtitle_font, fill=(200, 220, 255))

image.save(output)
print(f"Banner saved to {output.resolve()}")
