import nltk
import re

mail = """<div class="WordSection1">
<p class="MsoNormal">Bonjour,<o:p></o:p></p>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
<p class="MsoNormal">Essai pour découvrir comment fonctionne un e-mail,<o:p></o:p></p>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
<p class="MsoNormal">Cordialement<o:p></o:p></p>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
</div>"""
txt = re.findall("<p class=\"MsoNormal\">(.+?)<o\:p>", mail)
tt = ""
for i in txt :
    tt += i

tokens = nltk.word_tokenize(tt, language = 'french')
tagged = nltk.pos_tag(tokens)
print(tagged)