#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Empty experiment GUI

author: Robert Luke
"""

# Import useful modules

from PyQt4 import QtCore, QtGui
from functools import partial


#
# GUI for the experimenter
#

class Experimenter(QtGui.QWidget):

    def __init__(self):
        super(Experimenter, self).__init__()
        self.initUI()
        self.participant = Participant()

    def initUI(self):
        self.setWindowTitle('Experimenter')

        self.createSettingsBox()
        self.createActivityBox()
        self.createControlBox()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)         # Set spacing between widgets

        grid.addWidget(self.settingsBox, 1, 1)
        grid.addWidget(self.activityBox, 2, 1)
        grid.addWidget(self.controlBox,  3, 1)

        self.setLayout(grid)
        self.show()

    #
    # Settings box

    def createSettingsBox(self):

        self.settingsBox = QtGui.QGroupBox("Experimental Settings")
        grid = QtGui.QGridLayout()

        # Add a button
        self.button_name = QtGui.QPushButton("A button")
        self.button_name.clicked.connect(self.button_name_action)
        grid.addWidget(self.button_name, 0, 0, QtCore.Qt.AlignVCenter)

        # And a combo box
        self.combo_mode = QtGui.QComboBox(self)
        self.combo_mode.addItem("Mode")
        self.combo_mode.addItem('P1')
        self.combo_mode.addItem('P2')
        for i in range(2):
            self.combo_mode.addItem('CE' + str(i+1))
        self.combo_mode.activated[str].connect(self.combo_name_action)
        grid.addWidget(self.combo_mode, 0, 1)

        self.settingsBox.setLayout(grid)

    def button_name_action(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
                                              'You pushed a button.')
        if ok:
            name = str(text)
            self.button_name.setText('You: ' + str(name))

    def combo_name_action(self, text):
        text = str(text)

    #
    # Activity box

    def createActivityBox(self):

        self.activityBox = QtGui.QGroupBox("Experimental Activity")
        grid = QtGui.QGridLayout()
        self.activityBox.setLayout(grid)

    #
    # Control box

    def createControlBox(self):

        self.controlBox = QtGui.QGroupBox("Experimental Control")
        grid = QtGui.QGridLayout()
        self.controlBox.setLayout(grid)


#
# GUI for the participant
#

class Participant(QtGui.QWidget):

    def __init__(self):
        super(Participant, self).__init__()
        self.setWindowTitle('Participant')

        nButtons = 3

        grid = QtGui.QGridLayout()
        self.button = {}
        for i in range(nButtons):

            # Add a button
            self.button[(i)] = QtGui.QPushButton(str(i+1))
            self.button[(i)].setSizePolicy(QtGui.QSizePolicy.Preferred,
                                           QtGui.QSizePolicy.Expanding)
            self.button[i].clicked.connect(partial(self.participant_choice, i))
            grid.addWidget(self.button[(i)], 1, i)

        self.setLayout(grid)
        self.show()

    def participant_choice(self, option):
        print option


#
#  Main program
#

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    exper = Experimenter()
    sys.exit(app.exec_())
