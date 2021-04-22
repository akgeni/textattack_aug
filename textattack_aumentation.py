from textattack.augmentation import EmbeddingAugmenter

augmenter = EmbeddingAugmenter(pct_words_to_swap=0.2, transformations_per_example=5)
s = 'What I cannot create, I do not understand.'

print(augmenter.augment(s))
#output
['What I cannot create, I do not realise.', 'What I cannot create, I do not understanding.', 'What I cannot create, I do not understands.', 'What I cannot create, I do not understood.', 'What I cannot creating, I do not understand.']
