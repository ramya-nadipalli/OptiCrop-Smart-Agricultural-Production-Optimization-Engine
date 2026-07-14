import requests
from pathlib import Path
import json

crops_wiki = {
    "coconut": "Coconut",
    "onion": "Onion",
    "broccoli": "Broccoli",
    "carrot": "Carrot",
    "groundnut": "Peanut",
    "watermelon": "Watermelon",
    "papaya": "Papaya",
    "pomegranate": "Pomegranate",
    "lemon": "Lemon",
    "pineapple": "Pineapple",
    "garlic": "Garlic",
    "ginger": "Ginger",
    "turmeric": "Turmeric",
    "chilli": "Chili pepper",
    "mustard": "Mustard plant",
    "sunflower": "Sunflower",
    "lentil": "Lentil",
    "cucumber": "Cucumber",
    "pumpkin": "Pumpkin"
}

img_dir = Path(__file__).parent / "static" / "img"
img_dir.mkdir(parents=True, exist_ok=True)

for crop_name, wiki_name in crops_wiki.items():
    img_path = img_dir / f"{crop_name}.jpg"
    
    if img_path.exists():
        print(f"[OK] {crop_name}.jpg already exists")
        continue
    
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={wiki_name}&prop=pageimages&format=json&pithumbsize=400"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            
            for page_id, page_data in pages.items():
                if 'thumbnail' in page_data:
                    image_url = page_data['thumbnail']['source']
                    img_response = requests.get(image_url, timeout=10)
                    
                    if img_response.status_code == 200:
                        with open(img_path, 'wb') as f:
                            f.write(img_response.content)
                        print(f"[DONE] Downloaded {crop_name}.jpg")
                        break
                else:
                    print(f"[FAIL] No image found for {crop_name}")
        else:
            print(f"[FAIL] API error for {crop_name}: {response.status_code}")
    
    except Exception as e:
        print(f"[ERROR] Error downloading {crop_name}: {str(e)}")

print("\nImage download complete!")
