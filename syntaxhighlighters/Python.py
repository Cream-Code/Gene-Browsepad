from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat, QColor
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMenu, QMessageBox, QTextEdit

from .Highlighter import Highlighter

class PythonHighlighter(Highlighter):
    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)

        self.highlightingRules = []

        keyword0Format = QTextCharFormat()
        keyword0Format.setForeground(QColor(51, 255, 255))
        keyword0Format.setFontWeight(QFont.Bold)

        keyword0Patterns = ['\\band\\b', 'or\\b', '\\bis\\b', '\\bin\\b', '\\bnot\\b']

        for pattern in keyword0Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword0Format))

        keyword1Format = QTextCharFormat()
        keyword1Format.setForeground(QColor('#FF5370'))
        keyword1Format.setFontWeight(QFont.Bold)

        keyword1Patterns = ['\\bclass\\b', '\\bdel\\b','\\bdef\\b','\\bglobal\\b']

        for pattern in keyword1Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword1Format))

        keyword2Format = QTextCharFormat()
        keyword2Format.setForeground(QColor(255,218,185))
        keyword2Format.setFontWeight(QFont.Bold)

        keyword2Patterns = ['\\breturn\\b', '\\bassert\\b', '\\bpass\\b', '\\blambda\\b']

        for pattern in keyword2Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword2Format))

        keyword3Format = QTextCharFormat()
        keyword3Format.setForeground(QColor(124,252,0))
        keyword3Format.setFontWeight(QFont.Bold)

        keyword3Patterns = ['\\bif\\b','\\belif\\b', '\\belse\\b','\\bfinally\\b', '\\btry\\b', '\\braise\\b', '\\byield\\b']

        for pattern in keyword3Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword3Format))
        
        keyword4Format = QTextCharFormat()
        keyword4Format.setForeground(QColor(205,133,63))
        keyword4Format.setFontWeight(QFont.Bold)

        keyword4Patterns = ['\\bTrue\\b', '\\bFalse\\b']

        for pattern in keyword4Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword4Format))
        
        keyword5Format = QTextCharFormat()
        keyword5Format.setForeground(QColor(70, 130, 180))
        keyword5Format.setFontWeight(QFont.Bold)

        keyword5Patterns = ['\\bbreak\\b', '\\bcontinue\\b', '\\bexcept\\b', '\\bexec\\b']

        for pattern in keyword5Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword5Format))
        
        keyword6Format = QTextCharFormat()
        keyword6Format.setForeground(QColor(212, 175, 55))
        keyword6Format.setFontWeight(QFont.Bold)

        keyword6Patterns = ['\\bfrom\\b', '\\bimport\\b', '\\bprint\\b']

        for pattern in keyword6Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword6Format))
        
        keyword7Format = QTextCharFormat()
        keyword7Format.setForeground(QColor(123,104,238))
        keyword7Format.setFontWeight(QFont.Bold)

        keyword7Patterns = ['\\bfor\\b', '\\bwhile\\b','\\bNone\\b']

        for pattern in keyword7Patterns:
                self.highlightingRules.append((QRegExp(pattern), keyword7Format))

        bracesFormat = QTextCharFormat()
        bracesFormat.setForeground(QColor(QColor(169,169,169)))
        bracesFormat.setFontWeight(QFont.Bold)

        bracesPatterns = ['\\b\{\\b', '\\b}\\b', '\\b(\\b', '\\b)\\b', '\\b[\\b', '\\b]\\b']
        
        for pattern in bracesPatterns:
                self.highlightingRules.append((QRegExp(pattern), bracesFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("#[^\n]*"),
                singleLineCommentFormat))


        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QColor(135,206,235))
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

        importFormat = QTextCharFormat()
        importFormat.setForeground(QColor(147, 112, 219))
        self.highlightingRules.append((QRegExp("^\\from\\b[A-Za-z0-9_]+\\import\\b[A-Za-z0-9_*,]+s*"), importFormat))
 
