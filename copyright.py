#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 11 Oct 2016, 16:10:42
#========================================
import time, wingapi
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
WEEK  = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
MONTH = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec')


def create_copyright_data():
    '''
    '''
    tm = time.localtime()
    data = ('#========================================',
            '# author: changlong.zang',
            '#   mail: zclongpop@163.com',
            '#   date: {0}, {1:0>2} {2} {3}, {4:0>2}:{5:0>2}:{6:0>2}'.format(WEEK[tm.tm_wday], tm.tm_mday, MONTH[tm.tm_mon], tm.tm_year, tm.tm_hour, tm.tm_min, tm.tm_sec),
            '#========================================',
            '#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+')

    return '\n'.join(data)



def init_python_document():
    '''
    '''
    editor = wingapi.gApplication.GetActiveEditor()
    if editor is None:
        return

    doc = editor.GetDocument()
    doc.SetText(create_copyright_data())
