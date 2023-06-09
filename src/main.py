import sys
import platform
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSizePolicy, QLabel, QGraphicsDropShadowEffect, QSizeGrip

# GUI FILE
from app_modules import *

# SETTINGS FILE MANAGER
# import json
# from pathlib import Path

# Simulacion
import simulacion.simulacion as simu

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fecha = ""

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True) # type: ignore
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Animal Kingdom Simulator')
        UIFunctions.labelTitle(self, 'Animal Kingdom Simulator')
        UIFunctions.labelDescription(self, 'Seleccione una opción')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 800)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 1000, 800)
        ## ==> END ##
        
        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Inicio", "BtnBarHome", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Simular", "BtnBarSimu", "url(:/16x16/icons/16x16/cil-3d.png)", True)
        # UIFunctions.addNewMenu(self, "Ajustes", "BtnBarAjustes", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        UIFunctions.addNewMenu(self, "Tema", "BtnBarTema", "url(:/16x16/icons/16x16/cil-lightbulb.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.themeSwitcher(self, self.ui.frame_left_menu.findChild(QPushButton, "BtnBarTema"), "ak")
        UIFunctions.selectStandardMenu(self, "BtnBarHome")
        UIFunctions.labelPage(self, "Inicio")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "AK", "url(:/24x24/icons/24x24/logoak24.png)", True)
        UIFunctions.labelCredits(self, "Desarrollado por: Lucas Depetris, Santiago Figueroa, Emanuel Haro y Maribel Masucci")
        UIFunctions.labelVersion(self, "v1.1")
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton: # type: ignore
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow # type: ignore
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        ## START - CONNECTORS // Conectan botones, deslizadores y entradas con funciones (lambda) y acciones
        ############################## ---/--/--- ##############################

        self.ui.BtnMenuSimu.clicked.connect(self.Button)
        self.ui.BtnSimular.clicked.connect(self.generarSimu)
        self.ui.calendarWidget.clicked.connect(lambda: self.ui.dia_label.setText("Día " + self.ui.calendarWidget.selectedDate().toString("dd/MM/yyyy")))
        self.ui.calendarWidget.clicked.connect(lambda: self.fechaCambiada(self.ui.calendarWidget.selectedDate().toString("dd/MM/yyyy")))

        ########################################################################
        ## END - CONNECTORS
        ############################## ---/--/--- ##############################

        ## INITIALIZE SETTINGS // Cargo la configuración
        # self.loadSettings()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        # FINALIZA SETEO DE LA VENTANA
        
    # Se declaran funciones que se usaran durante la ejecución
    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "BtnBarHome":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

            UIFunctions.labelPage(self, "INICIO")
            UIFunctions.labelDescription(self, 'Seleccione una opción')
            
            UIFunctions.resetStyle(self, "BtnBarHome")
            UIFunctions.selectStandardMenu(self, "BtnBarHome")
            
            self.ui.frame_content.setStyleSheet(self.ui.frame_content.styleSheet().replace('treeak.png', 'expeve.png'))

        # PAGE SIMULAR
        if btnWidget.objectName() == "BtnBarSimu" or btnWidget.objectName() == "BtnMenuSimu":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_simular)

            UIFunctions.labelPage(self, "SIMULACIÓN")
            UIFunctions.labelDescription(self, 'Seleccione una fecha y presione Simular para continuar')
            
            UIFunctions.resetStyle(self, "BtnBarSimu")
            UIFunctions.selectStandardMenu(self, "BtnBarSimu")

            self.ui.frame_content.setStyleSheet(self.ui.frame_content.styleSheet().replace('expeve.png', 'treeak.png'))
        
        # PAGE THEME
        if btnWidget.objectName() == "BtnBarTema":
            if UIFunctions.theme == "default":
                UIFunctions.themeSwitcher(self, btnWidget, "ak")
            else: 
                UIFunctions.themeSwitcher(self, btnWidget, "default")

        # PAGE AJUSTES
        if btnWidget.objectName() == "BtnBarAjustes":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            UIFunctions.resetStyle(self, "BtnBarAjustes")
            UIFunctions.labelPage(self, "AJUSTES")
            UIFunctions.labelDescription(self, 'Modifique los valores máximos y mínimos de frecuencia. Valores en rojo no seran considerados')
            
            UIFunctions.resetStyle(self, "BtnBarSimu")
            UIFunctions.selectStandardMenu(self, "BtnBarSimu")

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS // Son funciones para probar la aplicacion y mostrar en terminal las entradas
    ########################################################################
        
    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick: # type: ignore
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton: # type: ignore
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton: # type: ignore
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton: # type: ignore
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START ==> SIMULACION
    ############################## ---/--/--- ##############################

    def fechaCambiada(self, fecha: str):
        # print("self.fecha: " + self.fecha)
        # print("fecha: " + fecha)
        if self.fecha != fecha:
            self.ui.BtnSimular.setEnabled(True)
            self.fecha = fecha

    def generarSimu(self):
        self.ui.BtnSimular.setEnabled(False)
        datos = simu.Simulacion()
        nrovisit, problluvia, tipolluvia, probhuracan, perpot = datos
        # nrovisit, problluvia, probhuracan, perpot = [10500, 0.85, 0.1, 98213]
        self.ui.visitantes_label.setText(str(nrovisit) + " visitantes")
        self.ui.lluvia_label.setText("{:.2f}".format(problluvia * 100) + "%")
        self.ui.huracan_label.setText("{:.2f}".format(probhuracan * 100) + "%")
        self.ui.perdidas_label.setText("$" + str(perpot))

        if tipolluvia == "NO LLUEVE":
            self.ui.lluvia_label.setStyleSheet("color: #FFFFFF")
            self.ui.lluvia_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/sol24.png) 0 0 0 0 stretch stretch;")
            self.ui.label_tipo_lluvia.setText("No llueve")
        elif tipolluvia == "LLUVIA LIGERA":
            self.ui.lluvia_label.setStyleSheet("color: #FBC400")
            self.ui.lluvia_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/sol-lluvia24.png) 0 0 0 0 stretch stretch;")
            self.ui.label_tipo_lluvia.setText("Lluvia Ligera")
        elif tipolluvia == "LLUVIA INTENSA":
            self.ui.lluvia_label.setStyleSheet("color: #ffa149")
            self.ui.lluvia_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/lluvia24.png) 0 0 0 0 stretch stretch;")
            self.ui.label_tipo_lluvia.setText("Lluvia Intensa")
        elif tipolluvia == "LLUVIA MUY ABUNDANTE":
            self.ui.lluvia_label.setStyleSheet("color: #FF0000")
            self.ui.lluvia_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/lluvia24.png) 0 0 0 0 stretch stretch;")
            self.ui.label_tipo_lluvia.setText("Lluvia Abundante")

        if probhuracan <= 0.2:
            self.ui.huracan_label.setStyleSheet("color: #FFFFFF")
            self.ui.huracan_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/sol-viento24.png) 0 0 0 0 stretch stretch;")
        elif probhuracan <= 0.8:
            self.ui.huracan_label.setStyleSheet("color: #FBC400")
            self.ui.huracan_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/tornado24.png) 0 0 0 0 stretch stretch;")
        else:
            self.ui.huracan_label.setStyleSheet("color: #FF0000")
            self.ui.huracan_frame.setStyleSheet("border-image: url(:/24x24/icons/24x24/tornado24.png) 0 0 0 0 stretch stretch;")
        

    ########################################################################
    ## END ==> SIMULACION
    ############################## ---/--/--- ##############################
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# Hasta aqui llega
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Todo lo que se declaro antes se ejecuta aqui abajo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Black.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Light.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Regular.ttf')
    font = QFont("Satoshi Regular")
    app.setFont(font, "*") # type: ignore
    window = MainWindow()
    sys.exit(app.exec_())