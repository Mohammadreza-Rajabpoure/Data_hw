import hazm

def Normalize(text):

    normalizer = hazm.Normalizer()

    normalied_text = normalizer.normalize(text)

    return normalied_text