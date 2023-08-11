# mapper.py
import json
import os


class SentimotionMapper:
    def __init__(self):
        self.module_path = os.path.dirname(__file__)
        self.data_path = os.path.join(self.module_path, '../definitions')
        self.load_mappings()

    def load_json(self, filename):
        with open(os.path.join(self.data_path, filename), 'r') as file:
            return json.load(file)

    def load_mappings(self):
        data = self.load_json('sentimotion_definitions.json')
        self.emotion_to_emotion_abr = data["emotion_to_emotion_abr"]
        self.emotion_abr_to_emotion = dict(zip(self.emotion_to_emotion_abr.values(),
                                               self.emotion_to_emotion_abr.keys()))

        self.emotion_to_emotion_id = data["emotion_to_emotion_id"]
        self.emotion_id_to_emotion = dict(zip(self.emotion_to_emotion_id.values(),
                                              self.emotion_to_emotion_id.keys()))

        self.emotion_abr_to_emotion_id = {}
        for emotion, abr in self.emotion_to_emotion_abr.items():
            self.emotion_abr_to_emotion_id[abr] = self.emotion_to_emotion_id.get(emotion)
        self.emotion_id_to_emotion_abr = dict(zip(self.emotion_abr_to_emotion_id,
                                                  self.emotion_abr_to_emotion_id))

        self.emotion_to_valence = data["emotion_to_valence"]

        self.emotion_eng_to_swe = data["emotion_eng_to_swe"]
        self.emotion_swe_to_eng = dict(zip(self.emotion_eng_to_swe.values(),
                                           self.emotion_eng_to_swe.keys()))

    def get_emotion_abr_from_emotion(self, emotion):
        return self.emotion_to_emotion_abr[emotion]

    def get_emotion_from_abr(self, abr):
        return self.emotion_abr_to_emotion[abr]

    def get_emotion_id_from_emotion(self, emotion):
        return self.emotion_to_emotion_id[emotion]

    def get_emotion_from_id(self, emotion_id):
        return self.emotion_id_to_emotion[emotion_id]

    def get_emotion_abr_from_id(self, emotion_id):
        return self.emotion_id_to_emotion_abr[emotion_id]

    def get_id_from_emotion_abr(self, emotion_abr):
        return self.emotion_abr_to_emotion_id[emotion_abr]

    def get_valence_from_emotion(self, emotion):
        return self.emotion_to_valence[emotion]

    def get_swe_translation_from_eng(self, emotion_eng):
        return self.emotion_eng_to_swe[emotion_eng]

    def get_eng_translation_from_swe(self, emotion_swe):
        return self.emotion_swe_to_eng[emotion_swe]


mapper = SentimotionMapper()

