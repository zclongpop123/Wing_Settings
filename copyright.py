#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Mar 17 14:38:35 2017
#========================================
import time, string, wingapi
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def create_copyright_data():
    '''
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
                     2               18
    '''
    commentBase = string.punctuation[2]
    data = (commentBase + string.punctuation[18] * 40,
            '{0}{1}: {2}'.format(commentBase, 'author'.rjust(10), 'Changlong.Zang'),
            '{0}{1}: {2}'.format(commentBase,   'mail'.rjust(10), 'zclongpop123@163.com'),
            '{0}{1}: {2}'.format(commentBase,   'time'.rjust(10),  time.ctime(time.time())),
            commentBase + string.punctuation[18] * 40,
            commentBase + '--+' * 40,
			'def main():',
			"    '''",
			"    '''",
			'    pass')

    return '\n'.join(data)





def init_python_document():
    '''
    '''
    editor = wingapi.gApplication.GetActiveEditor()
    if editor is None:
        return

    #- add copyright
    doc = editor.GetDocument()
    doc.InsertChars(0, create_copyright_data())

    #- add main test code
    doc.InsertChars(doc.GetLength(), "\n\n\nif __name__ == \'__main__\':\n    main()\n")
