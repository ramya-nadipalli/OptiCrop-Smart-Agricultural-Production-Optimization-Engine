import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app


class CropPredictionTests(unittest.TestCase):
    def test_predict_crop_returns_known_crop(self):
        prediction = app.predict_crop(90, 42, 43, 20.9, 82.0, 6.5, 202.9)
        self.assertIn(prediction, {"rice", "maize", "chickpea", "kidneybeans", "pigeonpeas", "mothbeans", "mungbean", "blackgram", "lentil", "pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "apple", "orange", "papaya", "coconut", "cotton", "jute", "coffee"})


if __name__ == "__main__":
    unittest.main()
