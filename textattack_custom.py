from textattack.transformations import WordSwapRandomCharacterDeletion
from textattack.transformations import CompositeTransformation
from textattack.augmentation import Augmenter

transformation = CompositeTransformation([WordSwapRandomCharacterDeletion()])
augmenter = Augmenter(transformation=transformation, transformations_per_example=5)
s = 'What I cannot create, I do not understand.'

print(augmenter.augment(s))
['What I cannot creae, I do not understand.', 'What I cannot creat, I do not understand.', 
'What I cannot create, I do not nderstand.', 'What I cannot create, I do nt understand.', 'Wht I cannot create, I do not understand.']
