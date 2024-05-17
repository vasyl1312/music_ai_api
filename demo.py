from gtts import gTTS

mytext = 'Kyiv is the capital and most populous city of Ukraine.'
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")

# реалізація українською
mytext_uk = 'Київ — столиця і найбільше місто України. Місто розташоване на півночі Центральної України, адміністративний центр Київської області, на березі річки Дніпро. Сьоме місто в Європі за чисельністю населення.'
language_uk = 'uk'

myobj_uk = gTTS(text=mytext_uk, lang=language_uk, slow=False)
myobj_uk.save("welcome_uk.mp3")
