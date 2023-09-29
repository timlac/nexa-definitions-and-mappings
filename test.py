from py_sentimotion_mapper.sentimotion_mapper import Mapper

Mapper.get_emotion_from_abr("ang")
Mapper.get_emotion_abr_from_emotion("anger")

print(Mapper.get_emotion_id_from_emotion("anger"))


print(Mapper.emotion_to_emotion_abr)