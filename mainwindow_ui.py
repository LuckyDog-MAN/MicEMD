# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 652)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_signal_type = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_signal_type.setGeometry(QtCore.QRect(10, 5, 561, 616))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.tab_signal_type.setFont(font)
        self.tab_signal_type.setAutoFillBackground(True)
        self.tab_signal_type.setObjectName("tab_signal_type")
        self.tab_FDEM = QtWidgets.QWidget()
        self.tab_FDEM.setAutoFillBackground(True)
        self.tab_FDEM.setObjectName("tab_FDEM")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_FDEM)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 5, 536, 331))
        self.groupBox_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 25, 516, 86))
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_96 = QtWidgets.QLabel(self.groupBox_12)
        self.label_96.setGeometry(QtCore.QRect(490, 30, 16, 21))
        self.label_96.setObjectName("label_96")
        self.le_detector_current = QtWidgets.QLineEdit(self.groupBox_12)
        self.le_detector_current.setGeometry(QtCore.QRect(255, 30, 61, 21))
        self.le_detector_current.setAlignment(QtCore.Qt.AlignCenter)
        self.le_detector_current.setObjectName("le_detector_current")
        self.le_detector_roll = QtWidgets.QLineEdit(self.groupBox_12)
        self.le_detector_roll.setGeometry(QtCore.QRect(255, 55, 61, 21))
        self.le_detector_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.le_detector_roll.setObjectName("le_detector_roll")
        self.le_detector_radius = QtWidgets.QLineEdit(self.groupBox_12)
        self.le_detector_radius.setGeometry(QtCore.QRect(85, 30, 61, 21))
        self.le_detector_radius.setAlignment(QtCore.Qt.AlignCenter)
        self.le_detector_radius.setObjectName("le_detector_radius")
        self.label_97 = QtWidgets.QLabel(self.groupBox_12)
        self.label_97.setGeometry(QtCore.QRect(180, 30, 71, 21))
        self.label_97.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_97.setScaledContents(False)
        self.label_97.setAlignment(QtCore.Qt.AlignCenter)
        self.label_97.setObjectName("label_97")
        self.label_98 = QtWidgets.QLabel(self.groupBox_12)
        self.label_98.setGeometry(QtCore.QRect(350, 30, 71, 21))
        self.label_98.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_98.setScaledContents(False)
        self.label_98.setAlignment(QtCore.Qt.AlignCenter)
        self.label_98.setObjectName("label_98")
        self.label_99 = QtWidgets.QLabel(self.groupBox_12)
        self.label_99.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        self.label_99.setFont(font)
        self.label_99.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_99.setScaledContents(False)
        self.label_99.setAlignment(QtCore.Qt.AlignCenter)
        self.label_99.setObjectName("label_99")
        self.label_100 = QtWidgets.QLabel(self.groupBox_12)
        self.label_100.setGeometry(QtCore.QRect(320, 30, 16, 21))
        self.label_100.setObjectName("label_100")
        self.le_detector_pitch = QtWidgets.QLineEdit(self.groupBox_12)
        self.le_detector_pitch.setGeometry(QtCore.QRect(85, 55, 61, 21))
        self.le_detector_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.le_detector_pitch.setObjectName("le_detector_pitch")
        self.label_101 = QtWidgets.QLabel(self.groupBox_12)
        self.label_101.setGeometry(QtCore.QRect(150, 55, 16, 21))
        self.label_101.setObjectName("label_101")
        self.label_102 = QtWidgets.QLabel(self.groupBox_12)
        self.label_102.setGeometry(QtCore.QRect(320, 55, 16, 21))
        self.label_102.setObjectName("label_102")
        self.label_103 = QtWidgets.QLabel(self.groupBox_12)
        self.label_103.setGeometry(QtCore.QRect(10, 55, 71, 21))
        self.label_103.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_103.setScaledContents(False)
        self.label_103.setAlignment(QtCore.Qt.AlignCenter)
        self.label_103.setObjectName("label_103")
        self.label_104 = QtWidgets.QLabel(self.groupBox_12)
        self.label_104.setGeometry(QtCore.QRect(150, 30, 16, 21))
        self.label_104.setObjectName("label_104")
        self.le_detector_frequency = QtWidgets.QLineEdit(self.groupBox_12)
        self.le_detector_frequency.setGeometry(QtCore.QRect(425, 30, 61, 21))
        self.le_detector_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.le_detector_frequency.setObjectName("le_detector_frequency")
        self.label_105 = QtWidgets.QLabel(self.groupBox_12)
        self.label_105.setGeometry(QtCore.QRect(180, 55, 71, 21))
        self.label_105.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_105.setScaledContents(False)
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 115, 516, 111))
        self.groupBox_13.setObjectName("groupBox_13")
        self.le_target_length = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_length.setGeometry(QtCore.QRect(425, 55, 61, 21))
        self.le_target_length.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_length.setObjectName("le_target_length")
        self.label_115 = QtWidgets.QLabel(self.groupBox_13)
        self.label_115.setGeometry(QtCore.QRect(490, 55, 16, 21))
        self.label_115.setObjectName("label_115")
        self.label_116 = QtWidgets.QLabel(self.groupBox_13)
        self.label_116.setGeometry(QtCore.QRect(180, 55, 71, 21))
        self.label_116.setAlignment(QtCore.Qt.AlignCenter)
        self.label_116.setObjectName("label_116")
        self.le_target_roll = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_roll.setGeometry(QtCore.QRect(255, 55, 61, 21))
        self.le_target_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_roll.setObjectName("le_target_roll")
        self.label_117 = QtWidgets.QLabel(self.groupBox_13)
        self.label_117.setGeometry(QtCore.QRect(320, 55, 16, 21))
        self.label_117.setObjectName("label_117")
        self.label_112 = QtWidgets.QLabel(self.groupBox_13)
        self.label_112.setGeometry(QtCore.QRect(180, 31, 71, 21))
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.le_target_permeability = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_permeability.setGeometry(QtCore.QRect(255, 31, 61, 21))
        self.le_target_permeability.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_permeability.setObjectName("le_target_permeability")
        self.label_113 = QtWidgets.QLabel(self.groupBox_13)
        self.label_113.setGeometry(QtCore.QRect(320, 31, 26, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_113.setFont(font)
        self.label_113.setObjectName("label_113")
        self.label_114 = QtWidgets.QLabel(self.groupBox_13)
        self.label_114.setGeometry(QtCore.QRect(350, 55, 71, 21))
        self.label_114.setAlignment(QtCore.Qt.AlignCenter)
        self.label_114.setObjectName("label_114")
        self.label_120 = QtWidgets.QLabel(self.groupBox_13)
        self.label_120.setGeometry(QtCore.QRect(350, 30, 71, 21))
        self.label_120.setAlignment(QtCore.Qt.AlignCenter)
        self.label_120.setObjectName("label_120")
        self.le_target_radius = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_radius.setGeometry(QtCore.QRect(425, 30, 61, 21))
        self.le_target_radius.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_radius.setObjectName("le_target_radius")
        self.label_121 = QtWidgets.QLabel(self.groupBox_13)
        self.label_121.setGeometry(QtCore.QRect(490, 30, 16, 21))
        self.label_121.setObjectName("label_121")
        self.label_122 = QtWidgets.QLabel(self.groupBox_13)
        self.label_122.setGeometry(QtCore.QRect(10, 55, 71, 21))
        self.label_122.setAlignment(QtCore.Qt.AlignCenter)
        self.label_122.setObjectName("label_122")
        self.le_target_pitch = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_pitch.setGeometry(QtCore.QRect(85, 55, 61, 21))
        self.le_target_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_pitch.setObjectName("le_target_pitch")
        self.label_123 = QtWidgets.QLabel(self.groupBox_13)
        self.label_123.setGeometry(QtCore.QRect(150, 55, 16, 21))
        self.label_123.setObjectName("label_123")
        self.label_118 = QtWidgets.QLabel(self.groupBox_13)
        self.label_118.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.label_118.setAlignment(QtCore.Qt.AlignCenter)
        self.label_118.setObjectName("label_118")
        self.le_target_conductivity = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_conductivity.setGeometry(QtCore.QRect(85, 31, 61, 21))
        self.le_target_conductivity.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_conductivity.setObjectName("le_target_conductivity")
        self.label_119 = QtWidgets.QLabel(self.groupBox_13)
        self.label_119.setGeometry(QtCore.QRect(150, 31, 26, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_119.setFont(font)
        self.label_119.setObjectName("label_119")
        self.label_124 = QtWidgets.QLabel(self.groupBox_13)
        self.label_124.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_124.setAlignment(QtCore.Qt.AlignCenter)
        self.label_124.setObjectName("label_124")
        self.le_target_position_z = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_position_z.setGeometry(QtCore.QRect(125, 80, 21, 21))
        self.le_target_position_z.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_position_z.setObjectName("le_target_position_z")
        self.label_111 = QtWidgets.QLabel(self.groupBox_13)
        self.label_111.setGeometry(QtCore.QRect(150, 80, 16, 21))
        self.label_111.setObjectName("label_111")
        self.le_target_position_y = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_position_y.setGeometry(QtCore.QRect(105, 80, 21, 21))
        self.le_target_position_y.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_position_y.setObjectName("le_target_position_y")
        self.le_target_position_x = QtWidgets.QLineEdit(self.groupBox_13)
        self.le_target_position_x.setGeometry(QtCore.QRect(85, 80, 21, 21))
        self.le_target_position_x.setAlignment(QtCore.Qt.AlignCenter)
        self.le_target_position_x.setObjectName("le_target_position_x")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 230, 516, 91))
        self.groupBox_14.setObjectName("groupBox_14")
        self.le_collection_SNR = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_SNR.setGeometry(QtCore.QRect(425, 30, 61, 21))
        self.le_collection_SNR.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_SNR.setObjectName("le_collection_SNR")
        self.label_133 = QtWidgets.QLabel(self.groupBox_14)
        self.label_133.setGeometry(QtCore.QRect(180, 30, 71, 21))
        self.label_133.setAlignment(QtCore.Qt.AlignCenter)
        self.label_133.setObjectName("label_133")
        self.le_collection_height = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_height.setGeometry(QtCore.QRect(255, 30, 61, 21))
        self.le_collection_height.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_height.setObjectName("le_collection_height")
        self.label_132 = QtWidgets.QLabel(self.groupBox_14)
        self.label_132.setGeometry(QtCore.QRect(150, 30, 16, 21))
        self.label_132.setObjectName("label_132")
        self.le_collection_spacing = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_spacing.setGeometry(QtCore.QRect(85, 30, 61, 21))
        self.le_collection_spacing.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_spacing.setObjectName("le_collection_spacing")
        self.label_135 = QtWidgets.QLabel(self.groupBox_14)
        self.label_135.setGeometry(QtCore.QRect(350, 30, 71, 21))
        self.label_135.setAlignment(QtCore.Qt.AlignCenter)
        self.label_135.setObjectName("label_135")
        self.label_134 = QtWidgets.QLabel(self.groupBox_14)
        self.label_134.setGeometry(QtCore.QRect(320, 30, 16, 21))
        self.label_134.setObjectName("label_134")
        self.label_131 = QtWidgets.QLabel(self.groupBox_14)
        self.label_131.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.label_131.setAlignment(QtCore.Qt.AlignCenter)
        self.label_131.setObjectName("label_131")
        self.label_136 = QtWidgets.QLabel(self.groupBox_14)
        self.label_136.setGeometry(QtCore.QRect(490, 30, 16, 21))
        self.label_136.setObjectName("label_136")
        self.le_collection_x_max = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_x_max.setGeometry(QtCore.QRect(125, 60, 21, 21))
        self.le_collection_x_max.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_x_max.setObjectName("le_collection_x_max")
        self.cb_collection_direction = QtWidgets.QComboBox(self.groupBox_14)
        self.cb_collection_direction.setGeometry(QtCore.QRect(425, 60, 61, 20))
        self.cb_collection_direction.setAutoFillBackground(False)
        self.cb_collection_direction.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cb_collection_direction.setObjectName("cb_collection_direction")
        self.cb_collection_direction.addItem("")
        self.cb_collection_direction.addItem("")
        self.cb_collection_direction.addItem("")
        self.cb_collection_direction.addItem("")
        self.label_130 = QtWidgets.QLabel(self.groupBox_14)
        self.label_130.setGeometry(QtCore.QRect(320, 60, 16, 21))
        self.label_130.setObjectName("label_130")
        self.label_138 = QtWidgets.QLabel(self.groupBox_14)
        self.label_138.setGeometry(QtCore.QRect(350, 60, 71, 21))
        self.label_138.setAlignment(QtCore.Qt.AlignCenter)
        self.label_138.setObjectName("label_138")
        self.label_126 = QtWidgets.QLabel(self.groupBox_14)
        self.label_126.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.label_126.setAlignment(QtCore.Qt.AlignCenter)
        self.label_126.setObjectName("label_126")
        self.label_129 = QtWidgets.QLabel(self.groupBox_14)
        self.label_129.setGeometry(QtCore.QRect(282, 60, 16, 21))
        self.label_129.setObjectName("label_129")
        self.le_collection_y_min = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_y_min.setGeometry(QtCore.QRect(255, 60, 21, 21))
        self.le_collection_y_min.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_y_min.setObjectName("le_collection_y_min")
        self.label_137 = QtWidgets.QLabel(self.groupBox_14)
        self.label_137.setGeometry(QtCore.QRect(150, 60, 16, 21))
        self.label_137.setObjectName("label_137")
        self.le_collection_y_max = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_y_max.setGeometry(QtCore.QRect(295, 60, 21, 21))
        self.le_collection_y_max.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_y_max.setObjectName("le_collection_y_max")
        self.le_collection_x_min = QtWidgets.QLineEdit(self.groupBox_14)
        self.le_collection_x_min.setGeometry(QtCore.QRect(85, 60, 21, 21))
        self.le_collection_x_min.setAlignment(QtCore.Qt.AlignCenter)
        self.le_collection_x_min.setObjectName("le_collection_x_min")
        self.label_127 = QtWidgets.QLabel(self.groupBox_14)
        self.label_127.setGeometry(QtCore.QRect(112, 60, 16, 21))
        self.label_127.setObjectName("label_127")
        self.label_128 = QtWidgets.QLabel(self.groupBox_14)
        self.label_128.setGeometry(QtCore.QRect(180, 60, 71, 21))
        self.label_128.setAlignment(QtCore.Qt.AlignCenter)
        self.label_128.setObjectName("label_128")
        self.groupBox = QtWidgets.QGroupBox(self.tab_FDEM)
        self.groupBox.setGeometry(QtCore.QRect(10, 345, 536, 126))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 25, 516, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_139 = QtWidgets.QLabel(self.groupBox_2)
        self.label_139.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.label_139.setAlignment(QtCore.Qt.AlignCenter)
        self.label_139.setObjectName("label_139")
        self.cb_optimization_algorithm = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_optimization_algorithm.setGeometry(QtCore.QRect(85, 30, 161, 21))
        self.cb_optimization_algorithm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_optimization_algorithm.setObjectName("cb_optimization_algorithm")
        self.cb_optimization_algorithm.addItem("")
        self.cb_optimization_algorithm.addItem("")
        self.cb_optimization_algorithm.addItem("")
        self.cb_optimization_algorithm.addItem("")
        self.label_140 = QtWidgets.QLabel(self.groupBox_2)
        self.label_140.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.label_140.setAlignment(QtCore.Qt.AlignCenter)
        self.label_140.setObjectName("label_140")
        self.le_optimization_iterations = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_optimization_iterations.setGeometry(QtCore.QRect(85, 60, 61, 21))
        self.le_optimization_iterations.setAlignment(QtCore.Qt.AlignCenter)
        self.le_optimization_iterations.setObjectName("le_optimization_iterations")
        self.label_141 = QtWidgets.QLabel(self.groupBox_2)
        self.label_141.setGeometry(QtCore.QRect(270, 30, 146, 21))
        self.label_141.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_141.setObjectName("label_141")
        self.le_optimization_tol = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_optimization_tol.setGeometry(QtCore.QRect(425, 30, 61, 21))
        self.le_optimization_tol.setAlignment(QtCore.Qt.AlignCenter)
        self.le_optimization_tol.setObjectName("le_optimization_tol")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_FDEM)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 490, 536, 86))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cb_func_save_data = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_func_save_data.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.cb_func_save_data.setObjectName("cb_func_save_data")
        self.cb_func_save_result = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_func_save_result.setGeometry(QtCore.QRect(180, 30, 151, 21))
        self.cb_func_save_result.setObjectName("cb_func_save_result")
        self.tab_signal_type.addTab(self.tab_FDEM, "")
        self.tab_TDEM = QtWidgets.QWidget()
        self.tab_TDEM.setAutoFillBackground(True)
        self.tab_TDEM.setObjectName("tab_TDEM")
        self.tab_signal_type.addTab(self.tab_TDEM, "")
        self.tab_show = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_show.setEnabled(True)
        self.tab_show.setGeometry(QtCore.QRect(580, 5, 421, 411))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.tab_show.setFont(font)
        self.tab_show.setAutoFillBackground(False)
        self.tab_show.setObjectName("tab_show")
        self.tab_detection_scenario = QtWidgets.QWidget()
        self.tab_detection_scenario.setEnabled(True)
        self.tab_detection_scenario.setAutoFillBackground(False)
        self.tab_detection_scenario.setObjectName("tab_detection_scenario")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_detection_scenario)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-5, -5, 426, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gl_detection_scenario = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gl_detection_scenario.setContentsMargins(0, 0, 0, 0)
        self.gl_detection_scenario.setObjectName("gl_detection_scenario")
        self.tab_show.addTab(self.tab_detection_scenario, "")
        self.tab_discretize = QtWidgets.QWidget()
        self.tab_discretize.setObjectName("tab_discretize")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_discretize)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-5, -5, 426, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gl_discretize = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gl_discretize.setContentsMargins(0, 0, 0, 0)
        self.gl_discretize.setObjectName("gl_discretize")
        self.tab_show.addTab(self.tab_discretize, "")
        self.tab_magnetic_field_data = QtWidgets.QWidget()
        self.tab_magnetic_field_data.setObjectName("tab_magnetic_field_data")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_magnetic_field_data)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-5, -5, 426, 391))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gl_magnetic_field_data = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gl_magnetic_field_data.setContentsMargins(0, 0, 0, 0)
        self.gl_magnetic_field_data.setObjectName("gl_magnetic_field_data")
        self.tab_show.addTab(self.tab_magnetic_field_data, "")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(580, 420, 421, 166))
        self.groupBox_10.setObjectName("groupBox_10")
        self.tb_output_box = QtWidgets.QTextBrowser(self.groupBox_10)
        self.tb_output_box.setGeometry(QtCore.QRect(0, 15, 421, 151))
        self.tb_output_box.setAutoFillBackground(False)
        self.tb_output_box.setObjectName("tb_output_box")
        self.pb_run_fdem_forward_simulation = QtWidgets.QPushButton(self.centralwidget)
        self.pb_run_fdem_forward_simulation.setGeometry(QtCore.QRect(580, 590, 206, 31))
        self.pb_run_fdem_forward_simulation.setObjectName("pb_run_fdem_forward_simulation")
        self.pb_run_fdem_inversion = QtWidgets.QPushButton(self.centralwidget)
        self.pb_run_fdem_inversion.setGeometry(QtCore.QRect(795, 590, 206, 31))
        self.pb_run_fdem_inversion.setObjectName("pb_run_fdem_inversion")
        self.pb_run_tdem_classification = QtWidgets.QPushButton(self.centralwidget)
        self.pb_run_tdem_classification.setGeometry(QtCore.QRect(795, 590, 206, 31))
        self.pb_run_tdem_classification.setObjectName("pb_run_tdem_classification")
        self.pb_run_tdem_forward_simulation = QtWidgets.QPushButton(self.centralwidget)
        self.pb_run_tdem_forward_simulation.setGeometry(QtCore.QRect(580, 590, 206, 31))
        self.pb_run_tdem_forward_simulation.setObjectName("pb_run_tdem_forward_simulation")
        self.pb_run_tdem_classification.raise_()
        self.pb_run_tdem_forward_simulation.raise_()
        self.tab_signal_type.raise_()
        self.tab_show.raise_()
        self.groupBox_10.raise_()
        self.pb_run_fdem_forward_simulation.raise_()
        self.pb_run_fdem_inversion.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuLanguage = QtWidgets.QMenu(self.menubar)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionChinese = QtWidgets.QAction(MainWindow)
        self.actionChinese.setObjectName("actionChinese")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuHelp.addAction(self.actionTutorial)
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_signal_type.setCurrentIndex(0)
        self.tab_show.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Forward simulation"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Detector parameters"))
        self.label_96.setText(_translate("MainWindow", "Hz"))
        self.le_detector_current.setText(_translate("MainWindow", "20"))
        self.le_detector_roll.setText(_translate("MainWindow", "0"))
        self.le_detector_radius.setText(_translate("MainWindow", "0.4"))
        self.label_97.setText(_translate("MainWindow", "Current"))
        self.label_98.setText(_translate("MainWindow", "Frequency"))
        self.label_99.setText(_translate("MainWindow", "Radius"))
        self.label_100.setText(_translate("MainWindow", "A"))
        self.le_detector_pitch.setText(_translate("MainWindow", "0"))
        self.label_101.setText(_translate("MainWindow", "°"))
        self.label_102.setText(_translate("MainWindow", "°"))
        self.label_103.setText(_translate("MainWindow", "Pitch"))
        self.label_104.setText(_translate("MainWindow", "m"))
        self.le_detector_frequency.setText(_translate("MainWindow", "1000"))
        self.label_105.setText(_translate("MainWindow", "Roll"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Target parameters (cylinder)"))
        self.le_target_length.setText(_translate("MainWindow", "1"))
        self.label_115.setText(_translate("MainWindow", "m"))
        self.label_116.setText(_translate("MainWindow", "Roll"))
        self.le_target_roll.setText(_translate("MainWindow", "0"))
        self.label_117.setText(_translate("MainWindow", "°"))
        self.label_112.setText(_translate("MainWindow", "Permeability"))
        self.le_target_permeability.setText(_translate("MainWindow", "1.26e-6"))
        self.label_113.setText(_translate("MainWindow", "H/m"))
        self.label_114.setText(_translate("MainWindow", "Length"))
        self.label_120.setText(_translate("MainWindow", "Radius"))
        self.le_target_radius.setText(_translate("MainWindow", "0.2"))
        self.label_121.setText(_translate("MainWindow", "m"))
        self.label_122.setText(_translate("MainWindow", "Pitch"))
        self.le_target_pitch.setText(_translate("MainWindow", "0"))
        self.label_123.setText(_translate("MainWindow", "°"))
        self.label_118.setText(_translate("MainWindow", "Conductivity"))
        self.le_target_conductivity.setText(_translate("MainWindow", "5.71e7"))
        self.label_119.setText(_translate("MainWindow", "S/m"))
        self.label_124.setText(_translate("MainWindow", "Position"))
        self.le_target_position_z.setText(_translate("MainWindow", "-3"))
        self.label_111.setText(_translate("MainWindow", "m"))
        self.le_target_position_y.setText(_translate("MainWindow", "0"))
        self.le_target_position_x.setText(_translate("MainWindow", "0"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Collection parameters"))
        self.le_collection_SNR.setText(_translate("MainWindow", "30"))
        self.label_133.setText(_translate("MainWindow", "Height"))
        self.le_collection_height.setText(_translate("MainWindow", "0.1"))
        self.label_132.setText(_translate("MainWindow", "m"))
        self.le_collection_spacing.setText(_translate("MainWindow", "0.4"))
        self.label_135.setText(_translate("MainWindow", "SNR"))
        self.label_134.setText(_translate("MainWindow", "m"))
        self.label_131.setText(_translate("MainWindow", "Spacing"))
        self.label_136.setText(_translate("MainWindow", "dB"))
        self.le_collection_x_max.setText(_translate("MainWindow", "2"))
        self.cb_collection_direction.setItemText(0, _translate("MainWindow", "z-axis"))
        self.cb_collection_direction.setItemText(1, _translate("MainWindow", "x-axis"))
        self.cb_collection_direction.setItemText(2, _translate("MainWindow", "y-axis"))
        self.cb_collection_direction.setItemText(3, _translate("MainWindow", "Total"))
        self.label_130.setText(_translate("MainWindow", "m"))
        self.label_138.setText(_translate("MainWindow", "Field"))
        self.label_126.setText(_translate("MainWindow", "x direction"))
        self.label_129.setText(_translate("MainWindow", "-"))
        self.le_collection_y_min.setText(_translate("MainWindow", "-2"))
        self.label_137.setText(_translate("MainWindow", "m"))
        self.le_collection_y_max.setText(_translate("MainWindow", "2"))
        self.le_collection_x_min.setText(_translate("MainWindow", "-2"))
        self.label_127.setText(_translate("MainWindow", "-"))
        self.label_128.setText(_translate("MainWindow", "y direction"))
        self.groupBox.setTitle(_translate("MainWindow", "Inversion"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Optimization algorithm parameters"))
        self.label_139.setText(_translate("MainWindow", "Algorithm"))
        self.cb_optimization_algorithm.setItemText(0, _translate("MainWindow", "Levenberg-Marquardt"))
        self.cb_optimization_algorithm.setItemText(1, _translate("MainWindow", "BFGS"))
        self.cb_optimization_algorithm.setItemText(2, _translate("MainWindow", "Conjugate gradient"))
        self.cb_optimization_algorithm.setItemText(3, _translate("MainWindow", "Steepest descent"))
        self.label_140.setText(_translate("MainWindow", "Iterations"))
        self.le_optimization_iterations.setText(_translate("MainWindow", "1000"))
        self.label_141.setText(_translate("MainWindow", "Tolerance:    gradient  < "))
        self.le_optimization_tol.setText(_translate("MainWindow", "1e-9"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Other functions"))
        self.cb_func_save_data.setText(_translate("MainWindow", "Save field data"))
        self.cb_func_save_result.setText(_translate("MainWindow", "Save inversion results"))
        self.tab_signal_type.setTabText(self.tab_signal_type.indexOf(self.tab_FDEM), _translate("MainWindow", "FDEM detection"))
        self.tab_signal_type.setTabText(self.tab_signal_type.indexOf(self.tab_TDEM), _translate("MainWindow", "TDEM detection"))
        self.tab_show.setTabText(self.tab_show.indexOf(self.tab_detection_scenario), _translate("MainWindow", "Detection scenario"))
        self.tab_show.setTabText(self.tab_show.indexOf(self.tab_discretize), _translate("MainWindow", "Discretize"))
        self.tab_show.setTabText(self.tab_show.indexOf(self.tab_magnetic_field_data), _translate("MainWindow", "Magnetic field data"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Output"))
        self.pb_run_fdem_forward_simulation.setText(_translate("MainWindow", "Run forward simulation"))
        self.pb_run_fdem_inversion.setText(_translate("MainWindow", "Run FDEM inversion"))
        self.pb_run_tdem_classification.setText(_translate("MainWindow", "Run TDEM classification"))
        self.pb_run_tdem_forward_simulation.setText(_translate("MainWindow", "Run forward simulation"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionChinese.setText(_translate("MainWindow", "Chinese"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
