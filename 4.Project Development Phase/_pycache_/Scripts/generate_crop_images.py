import os

images = {
    'rice': 'Rice',
    'maize': 'Maize',
    'chickpea': 'Chickpea',
    'kidneybeans': 'Kidney Beans',
    'pigeonpeas': 'Pigeon Peas',
    'mothbeans': 'Moth Beans',
    'mungbean': 'Mung Bean',
    'blackgram': 'Black Gram',
    'lentil': 'Lentil',
    'pomegranate': 'Pomegranate',
    'banana': 'Banana',
    'mango': 'Mango',
    'grapes': 'Grapes',
    'watermelon': 'Watermelon',
    'muskmelon': 'Muskmelon',
    'apple': 'Apple',
    'orange': 'Orange',
    'papaya': 'Papaya',
    'coconut': 'Coconut',
    'cotton': 'Cotton',
    'jute': 'Jute',
    'coffee': 'Coffee',
}

base_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'images')
os.makedirs(base_dir, exist_ok=True)

svg_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs>
    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#dff4db"/>
      <stop offset="100%" stop-color="#b8e4a5"/>
    </linearGradient>
  </defs>
  <rect width="640" height="360" rx="30" fill="url(#g)"/>
  <circle cx="160" cy="180" r="90" fill="#ffffff" opacity="0.65"/>
  <circle cx="470" cy="140" r="80" fill="#ffffff" opacity="0.55"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="50" fill="#22572f">{label}</text>
  <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="24" fill="#3c5c48">Crop Recommendation</text>
</svg>'''

for key, label in images.items():
    path = os.path.join(base_dir, f"{key}.svg")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg_template.format(label=label))

default_path = os.path.join(base_dir, 'default.svg')
with open(default_path, 'w', encoding='utf-8') as f:
    f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs>
    <linearGradient id="gd" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#edf8f0"/>
      <stop offset="100%" stop-color="#cde8d1"/>
    </linearGradient>
  </defs>
  <rect width="640" height="360" rx="30" fill="url(#gd)"/>
  <text x="50%" y="28%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="40" fill="#316e39">Smart Agriculture</text>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="28" fill="#355a3a">Crop preview image</text>
  <text x="50%" y="72%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="20" fill="#547658">Submit values to see results</text>
</svg>''')

print(f"Created {len(images) + 1} SVG files in {base_dir}")
