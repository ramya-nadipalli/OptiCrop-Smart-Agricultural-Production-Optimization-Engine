from PIL import Image, ImageDraw, ImageFont
import os

# Missing crops
missing_crops = [
    "coconut", "onion", "broccoli", "carrot", "groundnut", 
    "watermelon", "papaya", "pomegranate", "lemon", "pineapple",
    "garlic", "ginger", "turmeric", "chilli", "mustard",
    "sunflower", "lentil", "cucumber", "pumpkin"
]

# Colors for each crop
colors = {
    "coconut": "#8B4513",
    "onion": "#FFD700",
    "broccoli": "#228B22",
    "carrot": "#FF8C00",
    "groundnut": "#A0522D",
    "watermelon": "#FF1493",
    "papaya": "#FF6347",
    "pomegranate": "#DC143C",
    "lemon": "#FFFF00",
    "pineapple": "#FFD700",
    "garlic": "#F5F5F5",
    "ginger": "#DAA520",
    "turmeric": "#FFB347",
    "chilli": "#FF4500",
    "mustard": "#FFD700",
    "sunflower": "#FFD700",
    "lentil": "#8B4513",
    "cucumber": "#32CD32",
    "pumpkin": "#FF8C00"
}

img_dir = os.path.join(os.path.dirname(__file__), "static", "img")

for crop in missing_crops:
    img_path = os.path.join(img_dir, f"{crop}.jpg")
    
    if os.path.exists(img_path):
        print(f"✓ {crop}.jpg already exists")
        continue
    
    # Create image
    img = Image.new("RGB", (400, 300), color=colors.get(crop, "#90EE90"))
    draw = ImageDraw.Draw(img)
    
    # Add text
    text = crop.upper()
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (400 - text_width) // 2
    y = (300 - text_height) // 2
    
    draw.text((x, y), text, fill="white", font=font)
    
    # Save
    img.save(img_path)
    print(f"✓ Created {crop}.jpg")

print("\nAll placeholder images created!")
