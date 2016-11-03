#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 11 Oct 2016, 16:10:42
#========================================
import time, wingapi
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
WEEK  = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
MONTH = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


def create_copyright_data():
    '''
    '''
    tm = time.localtime()
    data = ('#========================================',
            '# author: changlong.zang',
            '#   mail: zclongpop@163.com',
            '#   date: {1}, {0.tm_mday:0>2} {2} {0.tm_year}, {0.tm_hour:0>2}:{0.tm_min:0>2}:{0.tm_sec:0>2}'.format(tm, WEEK[tm.tm_wday], MONTH[tm.tm_mon]),
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
