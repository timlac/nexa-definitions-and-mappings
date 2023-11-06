import numpy as np
from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper

# Translate a single value
translation1 = Mapper.get_eng_translation_from_swe("ilska")
print(translation1)  # Output: "anger"

# Translate a list of values
emotions = np.array(["ilska", "glädje", "sorg"])
translations = Mapper.get_eng_translation_from_swe(emotions)
print(translations)  # Output: ["anger", "joy", "sadness"]

#
# print(Mapper.get_emotion_abr_from_emotion_id(1))
#
# print(Mapper.emotion_id_to_emotion_abr)
#
# print(Mapper.emotion_abr_to_emotion_id)