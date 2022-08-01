from translate import Translator
from flask import request

to_fr = Translator(to_lang="fr")
to_en = Translator(from_lang="fr", to_lang="en")


def englishToFrench(text):
    try:
        text = request.args.get('textToTranslate')
    except Exception as ex:
        print(ex)
    translation = to_fr.translate(text)
    return translation


def frenchToEnglish(text):
    try:
        text = request.args.get('textToTranslate')
    except Exception as ex:
        print(ex)
    translation = to_en.translate(text)
    return translation
