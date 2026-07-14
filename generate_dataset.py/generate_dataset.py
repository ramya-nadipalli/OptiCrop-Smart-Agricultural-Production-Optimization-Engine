import numpy as np
import pandas as pd

np.random.seed(42)

CROPS = {
    "rice":       {"N":(60,100),  "P":(30,60),  "K":(30,60),  "temperature":(20,35), "humidity":(70,90), "ph":(5.5,7.0), "rainfall":(150,250)},
    "maize":      {"N":(60,100),  "P":(30,60),  "K":(10,30),  "temperature":(18,27), "humidity":(55,75), "ph":(5.8,7.0), "rainfall":(90,150)},
    "wheat":      {"N":(80,120),  "P":(30,60),  "K":(30,60),  "temperature":(10,25), "humidity":(55,75), "ph":(6.0,7.5), "rainfall":(50,90)},
    "sugarcane":  {"N":(100,140), "P":(30,60),  "K":(40,60),  "temperature":(20,30), "humidity":(70,90), "ph":(6.0,7.5), "rainfall":(150,200)},
    "cotton":     {"N":(100,140), "P":(30,60),  "K":(10,30),  "temperature":(25,35), "humidity":(55,75), "ph":(5.8,7.0), "rainfall":(50,100)},
    "banana":     {"N":(80,120),  "P":(60,90),  "K":(40,60),  "temperature":(26,30), "humidity":(70,90), "ph":(5.5,6.5), "rainfall":(160,220)},
    "mango":      {"N":(10,30),   "P":(20,35),  "K":(20,40),  "temperature":(24,30), "humidity":(40,60), "ph":(5.5,7.5), "rainfall":(75,250)},
    "apple":      {"N":(10,30),   "P":(5,15),   "K":(5,15),   "temperature":(18,24), "humidity":(85,95), "ph":(5.8,6.8), "rainfall":(75,120)},
    "orange":     {"N":(10,30),   "P":(5,15),   "K":(5,15),   "temperature":(18,29), "humidity":(85,95), "ph":(5.5,6.5), "rainfall":(100,150)},
    "grapes":     {"N":(10,30),   "P":(110,140),"K":(180,205),"temperature":(15,30), "humidity":(70,90), "ph":(6.0,7.0), "rainfall":(60,100)},
    "potato":     {"N":(100,140), "P":(30,60),  "K":(10,30),  "temperature":(15,20), "humidity":(70,90), "ph":(5.0,6.0), "rainfall":(75,110)},
    "tomato":     {"N":(60,100),  "P":(30,60),  "K":(30,60),  "temperature":(20,27), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(80,120)},
    "onion":      {"N":(40,60),   "P":(20,40),  "K":(20,40),  "temperature":(13,24), "humidity":(55,75), "ph":(6.0,7.0), "rainfall":(70,100)},
    "chickpea":   {"N":(30,50),   "P":(55,80),  "K":(65,90),  "temperature":(10,25), "humidity":(10,25), "ph":(6.0,7.0), "rainfall":(35,60)},
    "coffee":     {"N":(80,120),  "P":(20,40),  "K":(20,40),  "temperature":(18,24), "humidity":(50,70), "ph":(5.0,6.5), "rainfall":(120,180)},
    "tea":        {"N":(30,50),   "P":(20,30),  "K":(20,30),  "temperature":(15,25), "humidity":(70,90), "ph":(4.5,6.0), "rainfall":(150,250)},
    "rice":       {"N":(60,100),  "P":(30,60),  "K":(30,60),  "temperature":(20,35), "humidity":(70,90), "ph":(5.5,7.0), "rainfall":(150,250)},
    "paddy":      {"N":(60,100),  "P":(30,60),  "K":(30,60),  "temperature":(20,30), "humidity":(70,90), "ph":(5.5,6.5), "rainfall":(150,200)},
    "millet":     {"N":(10,30),   "P":(20,30),  "K":(20,30),  "temperature":(25,35), "humidity":(55,75), "ph":(5.5,7.0), "rainfall":(40,80)},
    "soybean":    {"N":(10,30),   "P":(35,55),  "K":(35,55),  "temperature":(20,30), "humidity":(55,75), "ph":(6.0,7.0), "rainfall":(60,100)},
    "barley":     {"N":(50,70),   "P":(45,65),  "K":(45,65),  "temperature":(10,20), "humidity":(55,75), "ph":(6.0,7.5), "rainfall":(40,80)},
    "cabbage":    {"N":(100,140), "P":(50,70),  "K":(40,60),  "temperature":(10,20), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(60,100)},
    "spinach":    {"N":(60,100),  "P":(30,50),  "K":(30,50),  "temperature":(10,20), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(50,80)},
    "lettuce":    {"N":(50,70),   "P":(25,35),  "K":(25,35),  "temperature":(10,20), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(70,100)},
    "pea":        {"N":(30,50),   "P":(35,45),  "K":(35,45),  "temperature":(10,20), "humidity":(60,80), "ph":(6.0,7.5), "rainfall":(50,80)},
    "broccoli":   {"N":(70,90),   "P":(35,45),  "K":(35,45),  "temperature":(15,20), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(80,120)},
    "carrot":     {"N":(50,70),   "P":(35,45),  "K":(35,45),  "temperature":(15,20), "humidity":(55,75), "ph":(6.0,6.8), "rainfall":(75,100)},
    "groundnut":  {"N":(15,30),   "P":(40,60),  "K":(40,60),  "temperature":(25,30), "humidity":(55,75), "ph":(5.5,7.0), "rainfall":(60,150)},
    "coconut":    {"N":(15,30),   "P":(10,22),  "K":(35,55),  "temperature":(20,32), "humidity":(85,95), "ph":(5.5,8.0), "rainfall":(150,250)},
    "watermelon": {"N":(80,120),  "P":(40,60),  "K":(50,70),  "temperature":(25,35), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(40,80)},
    "papaya":     {"N":(80,120),  "P":(40,60),  "K":(50,70),  "temperature":(25,35), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(100,150)},
    "pomegranate":{"N":(20,40),   "P":(20,40),  "K":(20,40),  "temperature":(25,35), "humidity":(50,70), "ph":(5.5,7.5), "rainfall":(50,100)},
    "lemon":      {"N":(20,40),   "P":(10,20),  "K":(10,20),  "temperature":(20,30), "humidity":(60,80), "ph":(5.5,6.5), "rainfall":(75,125)},
    "pineapple":  {"N":(80,120),  "P":(10,20),  "K":(100,140),"temperature":(20,30), "humidity":(70,90), "ph":(4.5,6.0), "rainfall":(100,150)},
    "garlic":     {"N":(80,120),  "P":(40,60),  "K":(40,60),  "temperature":(12,24), "humidity":(55,75), "ph":(6.0,7.0), "rainfall":(50,100)},
    "ginger":     {"N":(80,120),  "P":(40,60),  "K":(60,80),  "temperature":(20,30), "humidity":(70,90), "ph":(5.5,6.5), "rainfall":(150,200)},
    "turmeric":   {"N":(80,120),  "P":(40,60),  "K":(60,80),  "temperature":(20,30), "humidity":(70,90), "ph":(5.5,7.0), "rainfall":(150,200)},
    "chilli":     {"N":(80,120),  "P":(40,60),  "K":(60,80),  "temperature":(20,30), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(60,120)},
    "mustard":    {"N":(60,100),  "P":(30,50),  "K":(30,50),  "temperature":(10,25), "humidity":(55,75), "ph":(6.0,7.5), "rainfall":(40,80)},
    "sunflower":  {"N":(60,100),  "P":(40,60),  "K":(40,60),  "temperature":(20,30), "humidity":(55,75), "ph":(6.0,7.5), "rainfall":(50,100)},
    "lentil":     {"N":(20,40),   "P":(40,60),  "K":(20,40),  "temperature":(15,25), "humidity":(55,75), "ph":(6.0,8.0), "rainfall":(25,50)},
    "cucumber":   {"N":(80,120),  "P":(40,60),  "K":(50,70),  "temperature":(20,30), "humidity":(60,80), "ph":(6.0,7.0), "rainfall":(60,100)},
    "pumpkin":    {"N":(80,120),  "P":(40,60),  "K":(50,70),  "temperature":(18,28), "humidity":(60,80), "ph":(6.0,7.5), "rainfall":(60,100)},
}

ROWS_PER_CROP = 50

rows = []
for crop, ranges in CROPS.items():
    for _ in range(ROWS_PER_CROP):
        row = {k: round(np.random.uniform(v[0], v[1]), 2) for k, v in ranges.items()}
        row["crop"] = crop
        rows.append(row)

df = pd.DataFrame(rows)
df = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall", "crop"]]
df.to_csv("dataset.csv", index=False)
print(f"Dataset generated: {len(df)} rows, {df['crop'].nunique()} crops")
print("Crops:", sorted(df['crop'].unique()))
