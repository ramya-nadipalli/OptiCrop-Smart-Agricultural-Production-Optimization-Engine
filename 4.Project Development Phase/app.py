import os
import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file
from sklearn.tree import DecisionTreeClassifier
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

# Crop colors and styles for image generation
CROP_STYLES = {
    'rice': {'color': '#C8A882', 'accent': '#8B7500', 'bg': '#F0E68C'},
    'maize': {'color': '#FFD700', 'accent': '#228B22', 'bg': '#FFF8DC'},
    'chickpea': {'color': '#D2691E', 'accent': '#8B4513', 'bg': '#FFE4E1'},
    'kidneybeans': {'color': '#8B0000', 'accent': '#FF6347', 'bg': '#FFF0F5'},
    'pigeonpeas': {'color': '#B8860B', 'accent': '#DAA520', 'bg': '#FFFACD'},
    'mothbeans': {'color': '#CD853F', 'accent': '#8B4513', 'bg': '#F5DEB3'},
    'mungbean': {'color': '#556B2F', 'accent': '#6B8E23', 'bg': '#F0FFF0'},
    'blackgram': {'color': '#1A1A1A', 'accent': '#333333', 'bg': '#F5F5F5'},
    'lentil': {'color': '#A0522D', 'accent': '#8B4513', 'bg': '#FFE4E1'},
    'pomegranate': {'color': '#DC143C', 'accent': '#8B0000', 'bg': '#FFF8DC'},
    'banana': {'color': '#FFD700', 'accent': '#FFA500', 'bg': '#FFFACD'},
    'mango': {'color': '#FF8C00', 'accent': '#FF6347', 'bg': '#FFE4B5'},
    'grapes': {'color': '#800080', 'accent': '#4B0082', 'bg': '#F0E6FF'},
    'watermelon': {'color': '#FF1493', 'accent': '#FF69B4', 'bg': '#F5FFFA'},
    'muskmelon': {'color': '#FF9933', 'accent': '#FF7F50', 'bg': '#F5F5DC'},
    'apple': {'color': '#DC143C', 'accent': '#FF6347', 'bg': '#F0F8FF'},
    'orange': {'color': '#FF8C00', 'accent': '#FFA500', 'bg': '#FFF8DC'},
    'papaya': {'color': '#FFA07A', 'accent': '#FF7F50', 'bg': '#FFF5EE'},
    'coconut': {'color': '#8B4513', 'accent': '#A0522D', 'bg': '#F0FFFF'},
    'cotton': {'color': '#FFFFFF', 'accent': '#D3D3D3', 'bg': '#F5F5F5'},
    'jute': {'color': '#DAA520', 'accent': '#8B7355', 'bg': '#F5F5DC'},
    'coffee': {'color': '#6F4E37', 'accent': '#8B5A3C', 'bg': '#FAF0E6'},
}
CROP_INFO = {
    'rice': {
        'label': 'Rice',
        'description': 'Ideal for wet soils and warm climates, rice is a staple high-yield cereal.',
        'image': '/api/crop-image/rice'
    },
    'maize': {
        'label': 'Maize',
        'description': 'A versatile crop that grows well in warm weather and provides strong yields.',
        'image': '/api/crop-image/maize'
    },
    'chickpea': {
        'label': 'Chickpea',
        'description': 'A protein-rich legume that improves soil fertility and thrives in moderate climates.',
        'image': '/api/crop-image/chickpea'
    },
    'kidneybeans': {
        'label': 'Kidney Beans',
        'description': 'A nutritious pulse crop that prefers well-drained soil and warm growth conditions.',
        'image': '/api/crop-image/kidneybeans'
    },
    'pigeonpeas': {
        'label': 'Pigeon Peas',
        'description': 'A drought-tolerant legume suited for subtropical regions and low-water soils.',
        'image': '/api/crop-image/pigeonpeas'
    },
    'mothbeans': {
        'label': 'Moth Beans',
        'description': 'A hardy pulse crop that can flourish in arid soils and high temperatures.',
        'image': '/api/crop-image/mothbeans'
    },
    'mungbean': {
        'label': 'Mung Bean',
        'description': 'A fast-growing legume popular for its nutritional seeds and soil benefits.',
        'image': '/api/crop-image/mungbean'
    },
    'blackgram': {
        'label': 'Black Gram',
        'description': 'Also called urad bean, it grows well in warm, well-drained fields.',
        'image': '/api/crop-image/blackgram'
    },
    'lentil': {
        'label': 'Lentil',
        'description': 'A cool-season pulse crop known for its nutrient-dense seeds and easy growth.',
        'image': '/api/crop-image/lentil'
    },
    'pomegranate': {
        'label': 'Pomegranate',
        'description': 'A fruit crop that thrives in sunny conditions with moderate irrigation.',
        'image': '/api/crop-image/pomegranate'
    },
    'banana': {
        'label': 'Banana',
        'description': 'A tropical plantation crop requiring warmth, humidity, and rich soil.',
        'image': '/api/crop-image/banana'
    },
    'mango': {
        'label': 'Mango',
        'description': 'A high-value fruit crop that prefers warm weather and well-drained soil.',
        'image': '/api/crop-image/mango'
    },
    'grapes': {
        'label': 'Grapes',
        'description': 'A fruit crop suited for vineyards with temperate climates and good drainage.',
        'image': '/api/crop-image/grapes'
    },
    'watermelon': {
        'label': 'Watermelon',
        'description': 'A refreshing summer crop that needs warm temperatures and ample water.',
        'image': '/api/crop-image/watermelon'
    },
    'muskmelon': {
        'label': 'Muskmelon',
        'description': 'A fragrant melon crop that performs well in warm, sunny conditions.',
        'image': '/api/crop-image/muskmelon'
    },
    'apple': {
        'label': 'Apple',
        'description': 'A temperate fruit crop that requires cooler nights and steady moisture.',
        'image': '/api/crop-image/apple'
    },
    'orange': {
        'label': 'Orange',
        'description': 'A citrus crop that thrives in sunny, well-drained orchards with moderate humidity.',
        'image': '/api/crop-image/orange'
    },
    'papaya': {
        'label': 'Papaya',
        'description': 'A tropical fruit crop that grows quickly in warm, humid conditions.',
        'image': '/api/crop-image/papaya'
    },
    'coconut': {
        'label': 'Coconut',
        'description': 'A coastal crop favored by warm climates and sandy, well-drained soil.',
        'image': '/api/crop-image/coconut'
    },
    'cotton': {
        'label': 'Cotton',
        'description': 'A fiber crop that prefers warm temperatures and sunlight for strong yields.',
        'image': '/api/crop-image/cotton'
    },
    'jute': {
        'label': 'Jute',
        'description': 'A fiber crop that grows best in humid, subtropical climates with rich soil.',
        'image': '/api/crop-image/jute'
    },
    'coffee': {
        'label': 'Coffee',
        'description': 'A high-value bean crop suited for shaded tropical highlands with steady rain.',
        'image': '/api/crop-image/coffee'
    }
}
CROPS = list(CROP_INFO.keys())


def train_fallback_model():
    X = np.array([
        [90, 42, 43, 20.9, 82.0, 6.5, 202.9],
        [60, 55, 35, 27.0, 70.0, 5.5, 150.0],
        [20, 80, 30, 24.0, 65.0, 6.0, 100.0],
        [10, 20, 10, 30.0, 45.0, 7.0, 80.0],
        [80, 60, 50, 25.0, 90.0, 6.8, 180.0],
        [50, 40, 20, 22.0, 74.0, 6.2, 110.0],
    ], dtype=float)
    y = np.array(['rice', 'maize', 'cotton', 'mango', 'banana', 'jute'])
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    return model


def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    return train_fallback_model()


MODEL = load_model()


def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    prediction = MODEL.predict(features)
    return prediction[0]


def get_crop_info(crop):
    return CROP_INFO.get(crop, {
        'label': crop.title(),
        'description': 'A recommended crop based on your soil and weather conditions.',
        'image': '/api/crop-image/default'
    })


def generate_crop_image(crop_name):
    """Generate realistic crop images with natural styling"""
    width, height = 600, 400
    styles = CROP_STYLES.get(crop_name, CROP_STYLES.get('rice'))
    
    # Create base image with sky-like background
    img = Image.new('RGB', (width, height), (135, 206, 235))  # Sky blue
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Draw gradient-like background (sky to field)
    for y in range(height):
        ratio = y / height
        r = int(135 * (1 - ratio) + 101 * ratio)
        g = int(206 * (1 - ratio) + 155 * ratio)
        b = int(235 * (1 - ratio) + 50 * ratio)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b, 255))
    
    # Draw soil/ground area
    soil_height = height // 2.5
    for y in range(height - int(soil_height), height):
        ratio = (y - (height - int(soil_height))) / int(soil_height)
        r = int(139 * (1 - ratio) + 101 * ratio)
        g = int(90 * (1 - ratio) + 67 * ratio)
        b = int(43 * (1 - ratio) + 33 * ratio)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b, 255))
    
    # Draw realistic crop elements based on crop type
    if crop_name == 'rice':
        draw_rice_plants(draw, width, height, styles)
    elif crop_name == 'maize':
        draw_maize_plants(draw, width, height, styles)
    elif crop_name in ['chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil']:
        draw_legume_plants(draw, width, height, styles)
    elif crop_name in ['banana', 'mango', 'papaya', 'coconut']:
        draw_fruit_trees(draw, width, height, styles, crop_name)
    elif crop_name in ['grapes', 'watermelon', 'muskmelon']:
        draw_trailing_plants(draw, width, height, styles, crop_name)
    elif crop_name in ['pomegranate', 'apple', 'orange']:
        draw_citrus_trees(draw, width, height, styles, crop_name)
    elif crop_name == 'cotton':
        draw_cotton_plants(draw, width, height, styles)
    elif crop_name == 'jute':
        draw_jute_plants(draw, width, height, styles)
    elif crop_name == 'coffee':
        draw_coffee_plants(draw, width, height, styles)
    else:
        draw_generic_crop(draw, width, height, styles)
    
    # Draw title banner
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        label_font = ImageFont.truetype("arial.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        label_font = title_font
    
    crop_label = CROP_INFO.get(crop_name, {}).get('label', crop_name.title())
    
    # Semi-transparent background for text
    banner_height = 60
    draw.rectangle([0, 0, width, banner_height], fill=(0, 0, 0, 180))
    
    # Draw crop name
    text_bbox = draw.textbbox((0, 0), crop_label, font=title_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (width - text_width) // 2
    draw.text((text_x, 15), crop_label, fill='white', font=title_font)
    
    return img.convert('RGB')

def draw_rice_plants(draw, width, height, styles):
    """Draw realistic rice plants"""
    soil_top = int(height * 0.6)
    for x in range(50, width, 100):
        for y_offset in range(-5, 10, 5):
            # Rice stalks
            stalk_x = x + y_offset
            draw.line([(stalk_x, soil_top), (stalk_x - 15, soil_top - 80)], fill=(139, 120, 93), width=2)
            draw.line([(stalk_x, soil_top), (stalk_x + 15, soil_top - 75)], fill=(139, 120, 93), width=2)
            # Rice heads
            draw.ellipse([stalk_x - 8, soil_top - 85, stalk_x + 8, soil_top - 70], 
                        fill=(184, 134, 11), outline=(139, 105, 10), width=1)

def draw_maize_plants(draw, width, height, styles):
    """Draw realistic corn/maize plants"""
    soil_top = int(height * 0.6)
    for x in range(80, width, 150):
        # Main stalk
        draw.line([(x, soil_top), (x, soil_top - 150)], fill=(34, 139, 34), width=4)
        # Leaves
        for i in range(5):
            leaf_y = soil_top - (30 + i * 25)
            draw.polygon([(x, leaf_y), (x - 25, leaf_y - 15), (x - 15, leaf_y - 20)], 
                         fill=(76, 175, 80))
            draw.polygon([(x, leaf_y), (x + 25, leaf_y - 15), (x + 15, leaf_y - 20)], 
                         fill=(56, 142, 60))
        # Corn cob
        draw.ellipse([x - 12, soil_top - 160, x + 12, soil_top - 120], 
                    fill=(184, 134, 11), outline=(139, 105, 10), width=1)

def draw_legume_plants(draw, width, height, styles):
    """Draw legume plants (beans, peas, lentils)"""
    soil_top = int(height * 0.6)
    for x in range(60, width, 120):
        # Plant stems
        draw.line([(x, soil_top), (x - 10, soil_top - 60)], fill=(34, 139, 34), width=2)
        draw.line([(x, soil_top), (x + 10, soil_top - 65)], fill=(34, 139, 34), width=2)
        # Leaves (round for legumes)
        draw.ellipse([x - 15, soil_top - 75, x, soil_top - 55], fill=(85, 180, 85))
        draw.ellipse([x, soil_top - 70, x + 15, soil_top - 50], fill=(76, 175, 80))
        # Pods
        draw.ellipse([x - 8, soil_top - 90, x + 8, soil_top - 75], fill=(107, 142, 35))

def draw_fruit_trees(draw, width, height, styles, crop_name):
    """Draw fruit trees (banana, mango, papaya, coconut)"""
    soil_top = int(height * 0.65)
    tree_x = width // 2
    
    # Trunk
    draw.rectangle([tree_x - 15, soil_top - 180, tree_x + 15, soil_top], 
                  fill=(139, 69, 19), outline=(101, 50, 15))
    
    # Canopy - large circle of foliage
    canopy_radius = 80
    canopy_color = (34, 139, 34) if crop_name != 'coconut' else (107, 142, 35)
    draw.ellipse([tree_x - canopy_radius, soil_top - 200 - canopy_radius, 
                  tree_x + canopy_radius, soil_top - 200 + canopy_radius], 
                fill=canopy_color, outline=(25, 100, 25), width=2)
    
    # Add fruits as circles
    fruit_color = styles.get('color', '#FFD700')
    fruit_hex = fruit_color.lstrip('#')
    fruit_rgb = tuple(int(fruit_hex[i:i+2], 16) for i in (0, 2, 4))
    
    for i in range(5):
        fruit_x = tree_x - 60 + i * 30
        fruit_y = soil_top - 200 + (i % 2) * 30
        draw.ellipse([fruit_x - 12, fruit_y - 12, fruit_x + 12, fruit_y + 12], 
                    fill=fruit_rgb, outline=(200, 140, 50), width=1)

def draw_trailing_plants(draw, width, height, styles, crop_name):
    """Draw trailing plants (grapes, melons)"""
    soil_top = int(height * 0.65)
    
    # Vines
    for i in range(3):
        start_x = 100 + i * 200
        for j in range(4):
            vine_y = soil_top - 50 - j * 40
            draw.line([(start_x, soil_top), (start_x + 30, vine_y)], 
                     fill=(34, 139, 34), width=3)
            # Grapes/fruits in clusters
            fruit_color = styles.get('color', '#FF69B4')
            fruit_hex = fruit_color.lstrip('#')
            fruit_rgb = tuple(int(fruit_hex[i:i+2], 16) for i in (0, 2, 4))
            
            for k in range(3):
                draw.ellipse([start_x + 20 + k*8, vine_y - 20 + k*6, 
                             start_x + 28 + k*8, vine_y - 12 + k*6], 
                            fill=fruit_rgb)

def draw_citrus_trees(draw, width, height, styles, crop_name):
    """Draw citrus trees (apple, orange, pomegranate)"""
    soil_top = int(height * 0.65)
    for tree_x in [150, 400]:
        # Trunk
        draw.rectangle([tree_x - 10, soil_top - 120, tree_x + 10, soil_top], 
                      fill=(139, 69, 19))
        # Canopy
        draw.ellipse([tree_x - 60, soil_top - 180, tree_x + 60, soil_top - 60], 
                    fill=(34, 139, 34), outline=(25, 100, 25), width=2)
        # Fruits
        fruit_color = styles.get('color', '#FF8C00')
        fruit_hex = fruit_color.lstrip('#')
        fruit_rgb = tuple(int(fruit_hex[i:i+2], 16) for i in (0, 2, 4))
        
        for i in range(6):
            fruit_x = tree_x - 40 + (i % 3) * 40
            fruit_y = soil_top - 100 - (i // 3) * 40
            draw.ellipse([fruit_x - 10, fruit_y - 10, fruit_x + 10, fruit_y + 10], 
                        fill=fruit_rgb, outline=(200, 120, 40))

def draw_cotton_plants(draw, width, height, styles):
    """Draw cotton plants with fluffy bolls"""
    soil_top = int(height * 0.6)
    for x in range(100, width, 150):
        # Main stem
        draw.line([(x, soil_top), (x, soil_top - 100)], fill=(34, 139, 34), width=3)
        # Leaves
        for i in range(4):
            leaf_y = soil_top - 25 - i * 20
            draw.polygon([(x, leaf_y), (x - 20, leaf_y - 10), (x - 15, leaf_y + 10)], 
                         fill=(85, 180, 85))
        # Cotton bolls (fluffy white circles)
        for i in range(3):
            boll_x = x - 30 + i * 30
            boll_y = soil_top - 80 + (i % 2) * 20
            draw.ellipse([boll_x - 15, boll_y - 15, boll_x + 15, boll_y + 15], 
                        fill=(240, 240, 240), outline=(200, 200, 200), width=1)

def draw_jute_plants(draw, width, height, styles):
    """Draw jute plants with tall stalks"""
    soil_top = int(height * 0.6)
    for x in range(80, width, 140):
        # Tall jute stalks
        draw.line([(x, soil_top), (x - 5, soil_top - 130)], fill=(139, 105, 20), width=3)
        draw.line([(x, soil_top), (x + 5, soil_top - 125)], fill=(139, 105, 20), width=3)
        # Upper leaves
        for i in range(5):
            leaf_y = soil_top - 40 - i * 15
            draw.polygon([(x, leaf_y), (x - 15, leaf_y - 8), (x + 12, leaf_y - 5)], 
                         fill=(107, 142, 35))
        # Flower head (small)
        draw.ellipse([x - 8, soil_top - 135, x + 8, soil_top - 120], 
                    fill=(210, 180, 140))

def draw_coffee_plants(draw, width, height, styles):
    """Draw coffee plants with berries"""
    soil_top = int(height * 0.6)
    for x in range(100, width, 160):
        # Coffee plant bush
        draw.ellipse([x - 35, soil_top - 100, x + 35, soil_top - 30], 
                    fill=(34, 139, 34), outline=(25, 100, 25), width=2)
        # Coffee berries (red cherries)
        for i in range(5):
            berry_x = x - 25 + i * 15
            berry_y = soil_top - 90 + (i % 2) * 15
            draw.ellipse([berry_x - 6, berry_y - 6, berry_x + 6, berry_y + 6], 
                        fill=(139, 35, 35))

def draw_generic_crop(draw, width, height, styles):
    """Draw generic crop as fallback"""
    soil_top = int(height * 0.6)
    for x in range(60, width, 120):
        # Generic plants
        draw.line([(x, soil_top), (x - 10, soil_top - 80)], fill=(34, 139, 34), width=2)
        draw.line([(x, soil_top), (x + 10, soil_top - 75)], fill=(34, 139, 34), width=2)
        draw.ellipse([x - 15, soil_top - 85, x + 15, soil_top - 60], 
                    fill=(107, 142, 35))


@app.route('/api/crop-image/<crop_name>')
def crop_image(crop_name):
    """Generate and serve crop image"""
    try:
        img = generate_crop_image(crop_name)
        img_io = BytesIO()
        img.save(img_io, 'JPEG', quality=85)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg', as_attachment=False)
    except Exception as e:
        # Return a default error image
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True) or request.form
    try:
        prediction = predict_crop(
            float(data['nitrogen']),
            float(data['phosphorus']),
            float(data['potassium']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall']),
        )
        crop_info = get_crop_info(prediction)
        return jsonify({
            'crop': prediction,
            'label': crop_info['label'],
            'description': crop_info['description'],
            'image': crop_info['image']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
