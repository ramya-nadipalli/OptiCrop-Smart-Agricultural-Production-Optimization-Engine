"""
Generate SVG images for all crops in the recommendation system
"""
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'images')

CROP_SVGS = {
    'rice': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f0e68c"/>
  <ellipse cx="100" cy="80" rx="8" ry="35" fill="#8b7500" opacity="0.7"/>
  <ellipse cx="85" cy="75" rx="6" ry="40" fill="#8b7500" opacity="0.6"/>
  <ellipse cx="115" cy="78" rx="6" ry="38" fill="#8b7500" opacity="0.6"/>
  <circle cx="100" cy="100" r="25" fill="#90ee90"/>
  <circle cx="75" cy="110" r="20" fill="#90ee90"/>
  <circle cx="125" cy="110" r="20" fill="#90ee90"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#2d5016" font-weight="bold">Rice</text>
</svg>''',
    'maize': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#ffe4b5"/>
  <rect x="90" y="40" width="20" height="80" fill="#228b22"/>
  <circle cx="100" cy="60" r="15" fill="#ffd700"/>
  <circle cx="100" cy="80" r="15" fill="#ffd700"/>
  <circle cx="100" cy="100" r="15" fill="#ffd700"/>
  <circle cx="100" cy="120" r="15" fill="#ffd700"/>
  <path d="M 80 50 Q 60 70 70 100" stroke="#228b22" stroke-width="3" fill="none"/>
  <path d="M 120 50 Q 140 70 130 100" stroke="#228b22" stroke-width="3" fill="none"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#2d5016" font-weight="bold">Maize</text>
</svg>''',
    'chickpea': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#e6f3ff"/>
  <circle cx="70" cy="70" r="25" fill="#d2691e"/>
  <circle cx="130" cy="70" r="25" fill="#d2691e"/>
  <circle cx="100" cy="110" r="25" fill="#d2691e"/>
  <circle cx="85" cy="140" r="20" fill="#d2691e"/>
  <circle cx="115" cy="140" r="20" fill="#d2691e"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#8b4513" font-weight="bold">Chickpea</text>
</svg>''',
    'kidneybeans': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#fff0f5"/>
  <ellipse cx="60" cy="80" rx="20" ry="30" fill="#8b0000"/>
  <ellipse cx="100" cy="70" rx="20" ry="30" fill="#8b0000"/>
  <ellipse cx="140" cy="80" rx="20" ry="30" fill="#8b0000"/>
  <ellipse cx="80" cy="120" rx="20" ry="30" fill="#8b0000"/>
  <ellipse cx="120" cy="120" rx="20" ry="30" fill="#8b0000"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#5d0000" font-weight="bold">Kidney Beans</text>
</svg>''',
    'pigeonpeas': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#ffeaa7"/>
  <circle cx="70" cy="60" r="18" fill="#b8860b"/>
  <circle cx="110" cy="50" r="18" fill="#b8860b"/>
  <circle cx="150" cy="60" r="18" fill="#b8860b"/>
  <circle cx="85" cy="110" r="18" fill="#b8860b"/>
  <circle cx="125" cy="110" r="18" fill="#b8860b"/>
  <line x1="75" y1="65" x2="85" y2="105" stroke="#666" stroke-width="2"/>
  <line x1="115" y1="55" x2="120" y2="105" stroke="#666" stroke-width="2"/>
  <text x="100" y="170" text-anchor="middle" font-size="14" fill="#6b5b00" font-weight="bold">Pigeon Peas</text>
</svg>''',
    'mothbeans': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f5deb3"/>
  <circle cx="60" cy="80" r="16" fill="#cd853f"/>
  <circle cx="100" cy="70" r="16" fill="#cd853f"/>
  <circle cx="140" cy="80" r="16" fill="#cd853f"/>
  <circle cx="80" cy="120" r="16" fill="#cd853f"/>
  <circle cx="120" cy="120" r="16" fill="#cd853f"/>
  <circle cx="100" cy="145" r="16" fill="#cd853f"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#8b6914" font-weight="bold">Moth Beans</text>
</svg>''',
    'mungbean': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#e8f5e9"/>
  <circle cx="65" cy="75" r="17" fill="#556b2f"/>
  <circle cx="105" cy="65" r="17" fill="#556b2f"/>
  <circle cx="145" cy="75" r="17" fill="#556b2f"/>
  <circle cx="85" cy="115" r="17" fill="#556b2f"/>
  <circle cx="125" cy="115" r="17" fill="#556b2f"/>
  <circle cx="105" cy="145" r="17" fill="#556b2f"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#2d4d0f" font-weight="bold">Mung Bean</text>
</svg>''',
    'blackgram': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f0f0f0"/>
  <circle cx="65" cy="75" r="17" fill="#1a1a1a"/>
  <circle cx="105" cy="65" r="17" fill="#1a1a1a"/>
  <circle cx="145" cy="75" r="17" fill="#1a1a1a"/>
  <circle cx="85" cy="115" r="17" fill="#1a1a1a"/>
  <circle cx="125" cy="115" r="17" fill="#1a1a1a"/>
  <circle cx="105" cy="145" r="17" fill="#1a1a1a"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#333" font-weight="bold">Black Gram</text>
</svg>''',
    'lentil': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#ffe4e1"/>
  <circle cx="70" cy="75" r="16" fill="#a0522d"/>
  <circle cx="110" cy="65" r="16" fill="#a0522d"/>
  <circle cx="150" cy="75" r="16" fill="#a0522d"/>
  <circle cx="85" cy="120" r="16" fill="#a0522d"/>
  <circle cx="125" cy="120" r="16" fill="#a0522d"/>
  <circle cx="105" cy="150" r="16" fill="#a0522d"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#6b3410" font-weight="bold">Lentil</text>
</svg>''',
    'pomegranate': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#fff8dc"/>
  <circle cx="100" cy="90" r="40" fill="#dc143c"/>
  <circle cx="75" cy="120" r="12" fill="#8b0000"/>
  <circle cx="95" cy="130" r="12" fill="#8b0000"/>
  <circle cx="125" cy="130" r="12" fill="#8b0000"/>
  <circle cx="100" cy="60" r="8" fill="#228b22"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#8b3a00" font-weight="bold">Pomegranate</text>
</svg>''',
    'banana': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#fffacd"/>
  <ellipse cx="75" cy="85" rx="18" ry="35" fill="#ffd700" transform="rotate(-20 75 85)"/>
  <ellipse cx="100" cy="70" rx="18" ry="35" fill="#ffd700" transform="rotate(0 100 70)"/>
  <ellipse cx="125" cy="85" rx="18" ry="35" fill="#ffd700" transform="rotate(20 125 85)"/>
  <line x1="75" y1="120" x2="75" y2="140" stroke="#228b22" stroke-width="3"/>
  <line x1="100" y1="105" x2="100" y2="140" stroke="#228b22" stroke-width="3"/>
  <line x1="125" y1="120" x2="125" y2="140" stroke="#228b22" stroke-width="3"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#daa520" font-weight="bold">Banana</text>
</svg>''',
    'mango': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#ffe4b5"/>
  <ellipse cx="100" cy="85" rx="35" ry="40" fill="#ff8c00"/>
  <ellipse cx="85" cy="80" rx="15" ry="20" fill="#ffa500"/>
  <ellipse cx="115" cy="80" rx="15" ry="20" fill="#ffa500"/>
  <line x1="100" y1="125" x2="100" y2="145" stroke="#8b4513" stroke-width="3"/>
  <ellipse cx="90" cy="135" rx="8" ry="12" fill="#228b22"/>
  <ellipse cx="110" cy="135" rx="8" ry="12" fill="#228b22"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#cc6600" font-weight="bold">Mango</text>
</svg>''',
    'grapes': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f0e6ff"/>
  <line x1="100" y1="40" x2="100" y2="120" stroke="#8b4513" stroke-width="3"/>
  <circle cx="85" cy="60" r="12" fill="#800080"/>
  <circle cx="100" cy="50" r="12" fill="#800080"/>
  <circle cx="115" cy="60" r="12" fill="#800080"/>
  <circle cx="75" cy="80" r="12" fill="#800080"/>
  <circle cx="100" cy="75" r="12" fill="#800080"/>
  <circle cx="125" cy="80" r="12" fill="#800080"/>
  <circle cx="85" cy="100" r="12" fill="#800080"/>
  <circle cx="115" cy="100" r="12" fill="#800080"/>
  <circle cx="100" cy="110" r="12" fill="#800080"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#660066" font-weight="bold">Grapes</text>
</svg>''',
    'watermelon': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#e6ffe6"/>
  <circle cx="100" cy="90" r="38" fill="#ff1493"/>
  <circle cx="100" cy="90" r="33" fill="#ff69b4"/>
  <circle cx="85" cy="80" r="5" fill="#2f4f4f"/>
  <circle cx="100" cy="95" r="5" fill="#2f4f4f"/>
  <circle cx="115" cy="85" r="5" fill="#2f4f4f"/>
  <circle cx="90" cy="110" r="5" fill="#2f4f4f"/>
  <path d="M 95 50 L 105 50 L 108 60 L 92 60 Z" fill="#228b22"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#c71585" font-weight="bold">Watermelon</text>
</svg>''',
    'muskmelon': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f5f5dc"/>
  <circle cx="100" cy="90" r="38" fill="#ff9933"/>
  <circle cx="100" cy="90" r="35" fill="#ffb366"/>
  <path d="M 80 70 Q 100 60 120 70 Q 100 90 80 110 Q 100 100 120 110" stroke="#666" stroke-width="1.5" fill="none" opacity="0.5"/>
  <circle cx="100" cy="90" r="3" fill="#333"/>
  <path d="M 95 50 L 105 50 L 108 60 L 92 60 Z" fill="#228b22"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#cc7722" font-weight="bold">Muskmelon</text>
</svg>''',
    'apple': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f0f8ff"/>
  <circle cx="100" cy="90" r="35" fill="#dc143c"/>
  <circle cx="85" cy="75" r="20" fill="#ff6b6b"/>
  <circle cx="115" cy="75" r="20" fill="#ff6b6b"/>
  <rect x="97" y="35" width="6" height="25" fill="#8b4513"/>
  <ellipse cx="115" cy="50" rx="10" ry="8" fill="#228b22"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#8b0000" font-weight="bold">Apple</text>
</svg>''',
    'orange': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#fff8dc"/>
  <circle cx="100" cy="90" r="38" fill="#ff8c00"/>
  <circle cx="100" cy="90" r="35" fill="#ffa500"/>
  <circle cx="85" cy="75" r="6" fill="#ff9912"/>
  <circle cx="100" cy="70" r="6" fill="#ff9912"/>
  <circle cx="115" cy="75" r="6" fill="#ff9912"/>
  <circle cx="90" cy="95" r="6" fill="#ff9912"/>
  <circle cx="110" cy="95" r="6" fill="#ff9912"/>
  <line x1="100" y1="35" x2="100" y2="50" stroke="#228b22" stroke-width="2"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#cc6600" font-weight="bold">Orange</text>
</svg>''',
    'papaya': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#fff5ee"/>
  <ellipse cx="100" cy="90" rx="28" ry="38" fill="#ffa07a"/>
  <ellipse cx="100" cy="90" rx="24" ry="34" fill="#ff7f50"/>
  <circle cx="85" cy="85" r="5" fill="#333"/>
  <circle cx="100" cy="75" r="5" fill="#333"/>
  <circle cx="115" cy="85" r="5" fill="#333"/>
  <circle cx="90" cy="105" r="5" fill="#333"/>
  <circle cx="110" cy="105" r="5" fill="#333"/>
  <line x1="100" y1="35" x2="100" y2="50" stroke="#228b22" stroke-width="3"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#d2691e" font-weight="bold">Papaya</text>
</svg>''',
    'coconut': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#e0ffff"/>
  <circle cx="100" cy="80" r="32" fill="#8b4513"/>
  <circle cx="100" cy="80" r="28" fill="#a0522d"/>
  <path d="M 100 50 L 85 40 L 90 50 L 75 35 L 85 45 L 80 55" fill="#228b22"/>
  <path d="M 100 50 L 115 40 L 110 50 L 125 35 L 115 45 L 120 55" fill="#228b22"/>
  <circle cx="85" cy="80" r="4" fill="#333"/>
  <circle cx="115" cy="80" r="4" fill="#333"/>
  <line x1="100" y1="112" x2="100" y2="140" stroke="#8b4513" stroke-width="4"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#6b4423" font-weight="bold">Coconut</text>
</svg>''',
    'cotton': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#fff5ee"/>
  <circle cx="70" cy="75" r="18" fill="#f5f5f5"/>
  <circle cx="100" cy="60" r="18" fill="#f5f5f5"/>
  <circle cx="130" cy="75" r="18" fill="#f5f5f5"/>
  <circle cx="85" cy="110" r="18" fill="#f5f5f5"/>
  <circle cx="115" cy="110" r="18" fill="#f5f5f5"/>
  <circle cx="100" cy="130" r="18" fill="#f5f5f5"/>
  <path d="M 70 75 L 85 110" stroke="#8b7355" stroke-width="2"/>
  <path d="M 100 60 L 100 130" stroke="#8b7355" stroke-width="2"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#d2691e" font-weight="bold">Cotton</text>
</svg>''',
    'jute': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f5f5dc"/>
  <line x1="100" y1="40" x2="100" y2="130" stroke="#8b7355" stroke-width="4"/>
  <ellipse cx="85" cy="60" rx="12" ry="18" fill="#daa520"/>
  <ellipse cx="100" cy="50" rx="12" ry="18" fill="#daa520"/>
  <ellipse cx="115" cy="60" rx="12" ry="18" fill="#daa520"/>
  <ellipse cx="80" cy="90" rx="14" ry="20" fill="#daa520"/>
  <ellipse cx="120" cy="90" rx="14" ry="20" fill="#daa520"/>
  <ellipse cx="100" cy="110" rx="14" ry="20" fill="#daa520"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#8b6914" font-weight="bold">Jute</text>
</svg>''',
    'coffee': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#faf0e6"/>
  <circle cx="70" cy="75" r="16" fill="#6f4e37"/>
  <circle cx="100" cy="65" r="16" fill="#6f4e37"/>
  <circle cx="130" cy="75" r="16" fill="#6f4e37"/>
  <circle cx="85" cy="110" r="16" fill="#6f4e37"/>
  <circle cx="115" cy="110" r="16" fill="#6f4e37"/>
  <circle cx="100" cy="140" r="16" fill="#6f4e37"/>
  <path d="M 70 75 L 85 110 L 100 140" stroke="#228b22" stroke-width="2" fill="none"/>
  <path d="M 100 65 L 115 110" stroke="#228b22" stroke-width="2" fill="none"/>
  <text x="100" y="170" text-anchor="middle" font-size="18" fill="#4a3728" font-weight="bold">Coffee</text>
</svg>''',
    'default': '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#e8f5e9"/>
  <circle cx="100" cy="80" r="30" fill="#4caf50"/>
  <path d="M 100 50 L 85 70 L 95 65 L 75 80 L 95 75 L 85 95 L 100 85 L 115 95 L 105 75 L 125 80 L 105 65 L 115 70 Z" fill="#8bc34a"/>
  <rect x="95" y="110" width="10" height="25" fill="#8b4513"/>
  <text x="100" y="170" text-anchor="middle" font-size="16" fill="#2e7d32" font-weight="bold">Crop</text>
</svg>'''
}

def generate_svgs():
    """Generate SVG images for all crops"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for crop_name, svg_content in CROP_SVGS.items():
        file_path = os.path.join(OUTPUT_DIR, f'{crop_name}.svg')
        with open(file_path, 'w') as f:
            f.write(svg_content)
        print(f'✓ Generated {crop_name}.svg')

if __name__ == '__main__':
    generate_svgs()
    print(f'\n✓ All SVG images generated in {OUTPUT_DIR}')
