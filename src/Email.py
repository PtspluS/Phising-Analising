import email
import re
import mailparser


class Email:
    def __init__(self, raw = ""):
        self.raw = raw

        """
        try:
            parser = email.parser.HeaderParser()
            headers = parser.parsestr(self.raw.as_string())
            content = re.split(";", headers['Content-Type'])[0]

            if content == "text/html" or content == "multipart/alternative":
                self.type = 'html'
            else:
                self.type = 'text'

        except:
            self.type = 'text'

        self.header = self.extract_header()
        self.body = self.extract_body()
        self.text = self.extract_text_full()
        """
        try:
            mail = mailparser.parse_from_file(raw)
            self.header = mail.headers
            self.body = mail.body
            self.text = mail.body
            self.lang = self.find_language()
            self.mail = mail.mail_partial
        except Exception as e:
            print(e)
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

        try:
            body = body.decode('utf-8')
        except:
            try:
                body = body.decode('windows-1252')
            except:
                body = str(body)
        return body


    """
    find_language()
        find the language
        return :
            - return the language
    """
    def find_language(self):
        return 'EN-en'
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
        if self.lang is None:
            return 'EN-en'
        return (self.lang+'.')[:-1]

    # get all the links
    def get_links(self):
        url = self.text
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
        return urls

    # get the sender
    def get_sender(self):
        try:
            return self.mail['from']
        except Exception as e:
            print(e)
            for i in range(len(self.mail)):
                if self.mail[i] == 'from':
                    return self.mail[i]
            return [['a', 'a']]
