import unittest
from emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_EmotionDetection(self): 
        result1 = emotion_detector('I am glad this happened')
        end = result1["dominant_emotion"]
        self.assertEqual(end, 'joy')

        result2 = emotion_detector('I am really mad about this')
        end = result2["dominant_emotion"]
        self.assertEqual(end, 'anger')

        result3 = emotion_detector('I feel disgusted just hearing about this')
        end = result3["dominant_emotion"]
        self.assertEqual(end, 'disgust')

        result4 = emotion_detector('I am so sad about this')
        end = result4["dominant_emotion"]
        self.assertEqual(end, 'sadness')

        result5 = emotion_detector('I am really afraid that this will happen')
        end = result5["dominant_emotion"]
        self.assertEqual(end, 'fear')

if __name__ == "__main__":
    unittest.main()