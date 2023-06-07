import sys
import platform
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from app_modules import *

# SETTINGS FILE MANAGER
import json
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "BtnBarHome")
        UIFunctions.labelPage(self, "Inicio")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "AK", "url(:/24x24/icons/24x24/logoak24.png)", True)
        UIFunctions.labelCredits(self, "Desarrollado por: Lucas Depetris, Santiago Figueroa, Emanuel Haro y Maribel Masucci")
        UIFunctions.labelVersion(self, "v0.5")
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
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

        # # ASK MODULATION CONNECTORS
        # self.ui.messageInputASK.textChanged.connect(lambda: self.modulateASK())
        # self.ui.carrierFreqInputASK.valueChanged.connect(lambda: self.modulateASK())
        # self.ui.clearBtnASK.clicked.connect(lambda: self.clearASK())
        # # ASK ANIMATION CONNECTORS
        # self.ui.modulateBtnASK.clicked.connect(lambda: self.animateModulation("ask"))
        # self.ui.Btn_pauseASK.clicked.connect(lambda: self.animASK.switchPause())
        # # ASK PLOT CONNECTORS
        # self.ui.Btn_antialiasASK.clicked.connect(lambda: self.animASK.setAntialising(self.ui.Btn_antialiasASK.isChecked()))
        # self.ui.Btn_autoajustadoASK.clicked.connect(lambda: self.animASK.adjustPlot())
        # self.ui.velocidadInputASK.valueChanged.connect(lambda: self.animASK.speedChanged())
        # self.ui.samplesInputASK.valueChanged.connect(lambda: self.animASK.samplesChanged())

        # # FSK MODULATION CONNECTORS
        # self.ui.messageInputFSK.textChanged.connect(lambda: self.modulateFSK())
        # self.ui.carrierFreq1InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        # self.ui.carrierFreq2InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        # self.ui.clearBtnFSK.clicked.connect(lambda: self.clearFSK())
        # # FSK ANIMATION CONNECTORS
        # self.ui.modulateBtnFSK.clicked.connect(lambda: self.animateModulation("fsk"))
        # self.ui.Btn_pauseFSK.clicked.connect(lambda: self.animFSK.switchPause())
        # # FSK PLOT CONNECTORS
        # self.ui.Btn_antialiasFSK.clicked.connect(lambda: self.animFSK.setAntialising(self.ui.Btn_antialiasFSK.isChecked()))
        # self.ui.Btn_autoajustadoFSK.clicked.connect(lambda: self.animFSK.adjustPlot())
        # self.ui.velocidadInputFSK.valueChanged.connect(lambda: self.animFSK.speedChanged())
        # self.ui.samplesInputFSK.valueChanged.connect(lambda: self.animFSK.samplesChanged())

        # # PSK MODULATION CONNECTORS
        # self.ui.messageInputPSK.textChanged.connect(lambda: self.modulatePSK())
        # self.ui.carrierFreqInputPSK.valueChanged.connect(lambda: self.modulatePSK())
        # self.ui.clearBtnPSK.clicked.connect(lambda: self.clearPSK())
        # # PSK ANIMATION CONNECTORS
        # self.ui.modulateBtnPSK.clicked.connect(lambda: self.animateModulation("psk"))
        # self.ui.Btn_pausePSK.clicked.connect(lambda: self.animPSK.switchPause())
        # # PSK PLOT CONNECTORS
        # self.ui.Btn_antialiasPSK.clicked.connect(lambda: self.animPSK.setAntialising(self.ui.Btn_antialiasPSK.isChecked()))
        # self.ui.Btn_autoajustadoPSK.clicked.connect(lambda: self.animPSK.adjustPlot())
        # self.ui.velocidadInputPSK.valueChanged.connect(lambda: self.animPSK.speedChanged())
        # self.ui.samplesInputPSK.valueChanged.connect(lambda: self.animPSK.samplesChanged())

        # self.ui.Btn_helpASK.clicked.connect(lambda: self.helpPage("ask"))
        # self.ui.Btn_helpFSK.clicked.connect(lambda: self.helpPage("fsk"))
        # self.ui.Btn_helpPSK.clicked.connect(lambda: self.helpPage("psk"))
        # self.ui.Btn_helpSettings.clicked.connect(lambda: self.helpPage("settings"))
        # self.ui.Btn_helpMain.clicked.connect(lambda: self.helpPage("main"))

        self.ui.BtnMenuSimu.clicked.connect(self.Button)
        # self.ui.Btn_FSK.clicked.connect(self.Button)
        # self.ui.Btn_PSK.clicked.connect(self.Button)
        
        # # SETTINGS
        # self.ui.btn_AplicarASK.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierASK, self.ui.minCarrierASK, self.ui.sliderASK, self.ui.carrierFreqInputASK, self.ui.label_maxASK, self.ui.label_minASK))
        # self.ui.btn_AplicarFSK1.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierFSK1, self.ui.minCarrierFSK1, self.ui.sliderFSK1, self.ui.carrierFreq1InputFSK, self.ui.label_maxFSK_1, self.ui.label_minFSK_1))
        # self.ui.btn_AplicarFSK2.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierFSK2, self.ui.minCarrierFSK2, self.ui.sliderFSK2, self.ui.carrierFreq2InputFSK, self.ui.label_maxFSK_2, self.ui.label_minFSK_2))
        # self.ui.btn_AplicarPSK.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierPSK, self.ui.minCarrierPSK, self.ui.sliderPSK, self.ui.carrierFreqInputPSK, self.ui.label_maxPSK, self.ui.label_minPSK))

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

            UIFunctions.themeSwitcher(self, "animalkingdom")

        # PAGE SIMULAR
        if btnWidget.objectName() == "BtnBarSimu" or btnWidget.objectName() == "BtnMenuSimu":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_simular)
            UIFunctions.labelPage(self, "SIMULACIÓN")
            UIFunctions.labelDescription(self, 'Seleccione una fecha y presione Simular para continuar')
            
            UIFunctions.resetStyle(self, "BtnBarSimu")
            UIFunctions.selectStandardMenu(self, "BtnBarSimu")
            
            UIFunctions.themeSwitcher(self)

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

    ## EVENT ==> CHANGE SETTINGS
    ########################################################################
    #TODO: SAVE ONLY CHANGED
    # def settingsChanged(self, inputMax: QSpinBox, inputMin: QSpinBox, slider: QSlider, input: QSpinBox, labelMax: QLabel, labelMin: QLabel):
    #     newMax = inputMax.value()
    #     newMin = inputMin.value()
    #     if (newMax - newMin) > 0:
    #         slider.setMaximum(newMax)
    #         input.setMaximum(newMax)
    #         slider.setMinimum(newMin)
    #         input.setMinimum(newMin)
    #         labelMax.setText("{0} Hz".format(newMax))
    #         labelMin.setText("{0} Hz".format(newMin))
    #         inputMax.setStyleSheet(Style.style_spinbox_ok)
    #         inputMin.setStyleSheet(Style.style_spinbox_ok)
    #         self.saveSettings()
    #     else:
    #         inputMax.setStyleSheet(Style.style_spinbox_error)
    #         inputMin.setStyleSheet(Style.style_spinbox_error)
    #         # print("No se puede cambiar: MaxAct={0} MaxIng={1}".format())

    # def saveSettings(self):
    #     print("Saving")
    #     settings_json = {'maxASK' : self.ui.maxCarrierASK.value(),
    #                 'minASK' : self.ui.minCarrierASK.value(),
    #                 'maxFSK1' : self.ui.maxCarrierFSK1.value(),
    #                 'minFSK1' : self.ui.minCarrierFSK1.value(),
    #                 'maxFSK2' : self.ui.maxCarrierFSK2.value(),
    #                 'minFSK2' : self.ui.minCarrierFSK2.value(),
    #                 'maxPSK' : self.ui.maxCarrierPSK.value(),
    #                 'minPSK' : self.ui.minCarrierPSK.value()
    #                 }
    #     with open('settingSIGMA.json','w+') as fp:
    #         fp.seek(0)
    #         json.dump(settings_json, fp)#, indent=4)
    #         # fp.write(json.dumps(settings_json))

    # def loadSettings(self):
    #     settingsFile = "./settingSIGMA.json"
    #     path = Path(settingsFile)
    #     if path.is_file():
    #         print("File Exists")
    #         if path.stat().st_size != 0:
    #             print("Loading File...")
    #             with open(settingsFile,'r') as json_file:
    #                 settings_json = json.load(json_file)

    #             self.ui.maxCarrierASK.setValue(settings_json["maxASK"])
    #             self.ui.minCarrierASK.setValue(settings_json["minASK"])
    #             self.ui.maxCarrierFSK1.setValue(settings_json["maxFSK1"])
    #             self.ui.minCarrierFSK1.setValue(settings_json["minFSK1"])
    #             self.ui.maxCarrierFSK2.setValue(settings_json["maxFSK2"])
    #             self.ui.minCarrierFSK2.setValue(settings_json["minFSK2"])
    #             self.ui.maxCarrierPSK.setValue(settings_json["maxPSK"])
    #             self.ui.minCarrierPSK.setValue(settings_json["minPSK"])

    #             self.ui.btn_AplicarASK.click()
    #             self.ui.btn_AplicarFSK1.click()
    #             self.ui.btn_AplicarFSK2.click()
    #             self.ui.btn_AplicarPSK.click()
    #         else:
    #             print("Empty File")
    #     else:
    #         print("File Not Found")
        
    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
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