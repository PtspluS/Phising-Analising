# imports
from src.AnalyseImage import analyseLienImage
from src.AnalyseSource import analyse
from src.Grammar_annalisis import error_grammar_frequency_en
from src.Link_analyser import analyse_link_from


def mark_email(email):
    sender_name = email.get_sender()[0][0]
    sender_mail = email.get_sender()[0][1]
    links = email.get_links()
    language = email.get_language()
    txt = email.get_text()

    marks = []

    marks.append(analyseLienImage(links, sender_name))
#    marks.append(analyse(sender_name, sender_mail))
    try :
        marks.append(analyse_link_from(links))
    except Exception as e:
        marks.append(0)

    if language != 'FR-fr':
        marks.append(error_grammar_frequency_en(txt))

    return marks
