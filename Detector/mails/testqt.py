import quopri;
import io;

# helpers (the quopri module only supports file-to-file conversion)

def encodestring(instring, tabs=0):
    outfile = io.StringIO();
    quopri.encode(io.StringIO(instring), outfile, tabs);
    return outfile.getvalue();

def decodestring(instring):
    outfile = io.StringIO();
    quopri.decode(io.StringIO(instring), outfile);
    return outfile.getvalue();

#
# try it out

MESSAGE = "å i åa ä e ö!";

encoded_message = encodestring(MESSAGE);
decoded_message = decodestring(encoded_message);

print ("original:", MESSAGE);
print ("encoded message:", repr(encoded_message));
print ("decoded message:", decoded_message);
