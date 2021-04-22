NLP Augmentation Hands-On
Augmentation in Computer Vision is one of the important techniques and has proved to be effective. In NLP, augmentation is also tried and shown imporovements in quite a few cases.

In this part, We will first undestand the following

-What Data Augmentation is and why it works?

-Why it works so well Computer Vision?

-Benefits on Augmentation.

-Types of NLP Augmentation.

Then we will jump into one of the types of NLP Augmentation and will do hands-on.

What augmentation is and why it works?
Data Augmentation is a technique to sythetically generate new data points such that generated data have same semantics as of original data. In other words Data Augmentation is semantically invariant transformation.

Data Augmentation has these primary reasons to work.

Data Scarcity
Improves generalization capabilities (reuce overfitting)
Test Time Augmentation (Confident Prediction)
Why it works so well Computer Vision?
In Computer vision, particulally Deep Learning algorithms are data hungary. It means more data is always welcome.

Though there are some researcher object the volume vs quality of data. If you want to undestand more aabout it please go through this https://www.slideshare.net/xamat/10-lessons-learned-from-building-machine-learning-systems

Transformations applied on image during augmenation still preserve the meaning, hence are semantically invariant transformation. (reference - https://medium.com/secure-and-private-ai-writing-challenge/data-augmentation-increases-accuracy-of-your-model-but-how-aa1913468722)

"Image Aumentation"

Rules of Data Augmentation
The augmented data must follow a statistical distribution similar to that of the original data.
A human being should not be able to distinguish between the amplified data and the original data.
Data augmentation involves semantically invariant transformations.
In supervised learning, the transformations allowed for data augmentation are those that do not modify the class label of the new data generated.
In order to respect the semantic invariance, the number of successive or combined transformations must be limited, empirically to two (2).
Reference for above Rules Text Data Augmentation Made Simple

Benefits of Data Augmentation
Benefits of augmentation is widely docoments in Computer vision research.

Implicit regularization
Semi-Supervised applications, insufficient data.
Cost effective way to data gathering and labeling. Automated synthetic data generation helps to alliviate tedious data collection process.
Now we have some understanding of Data Augmentation we will shift our attention to text augmentation. Text augmentation and NLP Augmentation could be treated as synonym.

NLP augmentation can be classified into these major categories. Which each category having bunch of techniques.

Categories of NLP Augmentation
Lexical Substitution
Back Translation
Text Surface Transformation
Random Noise Injection
Instance Crossover Augmentation
Syntax-tree Manipulation
In this part we do hands-on for Lexical Substitution
