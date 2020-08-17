from gtts import gTTS

eng = "Hello, I welcome you in this lesson I believe we can learn a lot together.Thank You"
obj = gTTS(text = eng, slow = False, lang = 'en')
obj.save('eng.mp3')


hindi = "हमको मालूम है जन्नत की हक़ीक़त लेकिन,दिल के खुश रखने को 'ग़ालिब' ये ख़याल अच्छा है"
obj = gTTS(text = hindi, slow = False, lang = 'hi')
obj.save('hindi.mp3')




