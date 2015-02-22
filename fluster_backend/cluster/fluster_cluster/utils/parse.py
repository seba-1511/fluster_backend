import os
import docx
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


#: textract library has implemented most of the following functionality.
#: however, the way they set it up means we can't use it with dropbox
#: rest response objects.
#:
#: copy it wherever possible.

#: before writing a parser, make a test set of the given file types.

supported_file_types = ['.txt', '.docx', '.pdf']


def parse(file, metadata):
    """Try to read a file and return name if exception."""
    parser = {
        '.txt': parse_txt,
        '.docx': parse_docx,
        '.pdf': parse_pdf
    }

    contents = []
    file_type = os.path.splitext(metadata['path'])[1]
    if file_type in supported_file_types:
        parser[file_type](file)
    else:
        contents.append(os.path.basename(file))
    return contents


def parse_txt(file):
    """ Parse text files"""
    with open(file) as file:
        contents = file.read()
        file.close()
        return contents


def parse_pdf(file_name):
    """Parse pdf files."""
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(file_name, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 15
    caching = True
    pagenos = set()
    try:
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                      caching=caching):
            interpreter.process_page(page)
            break
    except PDFTextExtractionNotAllowed:
        print 'PDF Text Exctraction Not Allowed: ', file_name
        return 'PDFTextExtractionNotAllowed'
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    file_name.close()
    return str


def parse_rtf(file):
    """Parse rtf files."""
    #: this can be done in native python


def parse_docx(file):
    """Parse word files."""
    document = docx.Document(file)
    contents = '\n\n'.join(
        [paragraph.text for paragraph in document.paragraphs])
    file.close()
    return contents


def parse_doc(file):
    """Parse word (pre 2007) files."""
    #: Has to be done differently than .docx


def parse_xls(file):
    """Parse excel files."""
    #: same as word? I think ',' will get dropped by feature extraction.
    #:
    #: there are different file endings (.xlsx). Do we handle them separately?


def parse_ppt(file):
    """Parse powerpoint files."""
    #: same as word?
    #:
    #: eventually we want to capture structure of these file types.


def parse_latex(file):
    """Parse latex files."""
    #: low priority but kind of annoying because it means fluster doesn't work
    #: on my dropbox
    #:
    #: is there a library to do this?


def parse_csv(file):
    """Parse comma separated files."""
    #: python has a csv library


def parse_jpg(file):
    """Parse png image files."""
    #: very low priority (textract library does this however)
    #:
    #: eventually it would be cool to group these but for now just move them
    #: into an image folder or preserve existing structure if it exists
    #:
    #: this could get tricky if there are images grouped with certain files
    #:
    #: do we handle different image formats differently?


def parse_mp3(file):
    """Parse mp3 audio files."""
    #: very low priority (textract library does this however)
    #:
    #: similar comments as parse_jpg


def parse_pages(file):
    """Parse pages files."""
    #: how do handle pages files?
