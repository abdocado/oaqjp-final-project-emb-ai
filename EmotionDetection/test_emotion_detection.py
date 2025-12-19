import unittest
import emotion_detector
class TestEmotionDetection(unittest.Testcase):
    def test_EmotionDetection(self): 
        result = emotion_detector('I am glad this happened')
        end = result["dominant_emotion"]
        self.assetEqual(end, 'joy')
