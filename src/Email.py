import email
import re


class Email:
    def __init__(self, raw = ""):
        self.raw = raw

        parser = email.parser.HeaderParser()
        headers = parser.parsestr(self.raw.as_string())
        content = re.split(";", headers['Content-Type'])[0]

        if content == "text/html" or content == "multipart/alternative":
            self.type = 'html'
        elif content == "text/plain":
            self.type = 'text'

        self.header = self.extract_header()
        self.body = self.extract_body()
        self.text = self.extract_text_full()
        self.lang = self.find_language()

    '''
    extract_header()
        extract the header part of the email
        return : 
            - return the header (str)
    '''
    def extract_header(self):
        parser = email.parser.HeaderParser()
        headers = parser.parsestr(self.raw.as_string())

        head = ""

        for h in headers.items():
            head += h[0]+' : '+h[1]+'\n'

        return head

    '''
    extract_body()
        extract the body part of the email
        return :
            - return the body (str)
    '''
    def extract_body(self):
        b = self.raw

        return b.get_payload()


    '''
    extract_txt()
        extract all the txt in the email
        return : 
            - return tab of all txt
    
    def extract_txt(self, txt):
        pass
    '''
    # same as before but only return str
    def extract_text_full(self):
        b = self.raw
        body = ""

        if b.is_multipart():
            for part in b.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # skip any text/plain (txt) attachments
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)  # decode
                    break
            # not multipart - i.e. plain text, no attachments, keeping fingers crossed
            else:
                body = b.get_payload(decode=True)

        return body.decode("utf-8")


    """
    find_language()
        find the language
        return :
            - return the language
    """
    def find_language(self):
        b = self.raw
        if b.is_multipart():
            return b['Content-Language']
        else:
            return False
    # get header
    def get_header(self):
        return (self.header+'.')[:-1]

    # get body
    def get_body(self):
        return (self.body+'.')[:-1]

    # get text
    def get_text(self):
        return (self.text+'.')[:-1]

    # get language
    def get_language(self):
        return (self.lang+'.')[:-1]

    # get all the links
    def get_links(self):
        url = self.text
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
        return urls

    # get the sender
    def get_sender(self):
        send = self.raw._headers[17][1]+'.'[:-1]
        send = re.split('<', send[:-1])
        return send

