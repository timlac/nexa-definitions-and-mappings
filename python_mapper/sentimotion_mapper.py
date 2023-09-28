# mapper.py
import json
import os


class Mapper:

    data = None

    @staticmethod
    def _load_data_if_needed():
        # Load data from file if it hasn't been loaded yet
        if Mapper.data is None:
            module_path = os.path.dirname(__file__)
            data_path = os.path.join(module_path, '../definitions/sentimotion_definitions.json')

            with open(data_path, 'r') as file:
                Mapper.data = json.load(file)
        Mapper.load_mappings(Mapper.data)

    @staticmethod
    def load_mappings(data):

        print(data)

        Mapper.emotion_to_emotion_abr = data["emotion_to_emotion_abr"]
        Mapper.emotion_abr_to_emotion = dict(zip(Mapper.emotion_to_emotion_abr.values(),
                                                 Mapper.emotion_to_emotion_abr.keys()))

        Mapper.emotion_to_emotion_id = data["emotion_to_emotion_id"]
        Mapper.emotion_id_to_emotion = dict(zip(Mapper.emotion_to_emotion_id.values(),
                                                Mapper.emotion_to_emotion_id.keys()))

        Mapper.emotion_abr_to_emotion_id = {}
        for emotion, abr in Mapper.emotion_to_emotion_abr.items():
            Mapper.emotion_abr_to_emotion_id[abr] = Mapper.emotion_to_emotion_id.get(emotion)
            
        Mapper.emotion_id_to_emotion_abr = dict(zip(Mapper.emotion_abr_to_emotion_id,
                                                    Mapper.emotion_abr_to_emotion_id))

        Mapper.emotion_to_valence = data["emotion_to_valence"]

        Mapper.emotion_eng_to_swe = data["emotion_eng_to_swe"]
        Mapper.emotion_swe_to_eng = dict(zip(Mapper.emotion_eng_to_swe.values(),
                                             Mapper.emotion_eng_to_swe.keys()))
    
    @staticmethod
    def get_emotion_abr_from_emotion(emotion):
        Mapper._load_data_if_needed()
        return Mapper.emotion_to_emotion_abr[emotion]
    
    @staticmethod
    def get_emotion_from_abr(abr):
        Mapper._load_data_if_needed()
        return Mapper.emotion_abr_to_emotion[abr]
    
    @staticmethod
    def get_emotion_id_from_emotion(emotion):
        Mapper._load_data_if_needed()
        return Mapper.emotion_to_emotion_id[emotion]
    
    @staticmethod
    def get_emotion_from_id(emotion_id):
        Mapper._load_data_if_needed()
        return Mapper.emotion_id_to_emotion[emotion_id]
    
    @staticmethod
    def get_emotion_abr_from_id(emotion_id):
        Mapper._load_data_if_needed()
        return Mapper.emotion_id_to_emotion_abr[emotion_id]
    
    @staticmethod
    def get_id_from_emotion_abr(emotion_abr):
        Mapper._load_data_if_needed()
        return Mapper.emotion_abr_to_emotion_id[emotion_abr]
    
    @staticmethod
    def get_valence_from_emotion(emotion):
        Mapper._load_data_if_needed()
        return Mapper.emotion_to_valence[emotion]
    
    @staticmethod
    def get_swe_translation_from_eng(emotion_eng):
        Mapper._load_data_if_needed()
        return Mapper.emotion_eng_to_swe[emotion_eng]
    
    @staticmethod
    def get_eng_translation_from_swe(emotion_swe):
        Mapper._load_data_if_needed()
        return Mapper.emotion_swe_to_eng[emotion_swe]


m = Mapper

print(m.get_valence_from_emotion("shame"))
