# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_FormularioMatricula(object):
    def setupUi(self, FormularioMatricula):
        if not FormularioMatricula.objectName():
            FormularioMatricula.setObjectName(u"FormularioMatricula")
        FormularioMatricula.resize(789, 721)
        self.verticalLayout = QVBoxLayout(FormularioMatricula)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(FormularioMatricula)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(24)
        font.setBold(True)
        self.lblTitulo.setFont(font)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.lblSubtitulo = QLabel(FormularioMatricula)
        self.lblSubtitulo.setObjectName(u"lblSubtitulo")

        self.verticalLayout.addWidget(self.lblSubtitulo)

        self.formLayoutDatos = QFormLayout()
        self.formLayoutDatos.setObjectName(u"formLayoutDatos")
        self.lblNombre = QLabel(FormularioMatricula)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formLayoutDatos.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(FormularioMatricula)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayoutDatos.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblCorreo = QLabel(FormularioMatricula)
        self.lblCorreo.setObjectName(u"lblCorreo")

        self.formLayoutDatos.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCorreo)

        self.txtCorreo = QLineEdit(FormularioMatricula)
        self.txtCorreo.setObjectName(u"txtCorreo")

        self.formLayoutDatos.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtCorreo)

        self.cmbActividad = QComboBox(FormularioMatricula)
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.setObjectName(u"cmbActividad")

        self.formLayoutDatos.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbActividad)

        self.lblActividad = QLabel(FormularioMatricula)
        self.lblActividad.setObjectName(u"lblActividad")

        self.formLayoutDatos.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblActividad)


        self.verticalLayout.addLayout(self.formLayoutDatos)

        self.lblEstado = QLabel(FormularioMatricula)
        self.lblEstado.setObjectName(u"lblEstado")

        self.verticalLayout.addWidget(self.lblEstado)

        self.chkCondiciones = QCheckBox(FormularioMatricula)
        self.chkCondiciones.setObjectName(u"chkCondiciones")

        self.verticalLayout.addWidget(self.chkCondiciones)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnGuardar = QPushButton(FormularioMatricula)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setEnabled(False)

        self.layoutBotones.addWidget(self.btnGuardar)

        self.btnLimpiar = QPushButton(FormularioMatricula)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.layoutBotones.addWidget(self.btnLimpiar)


        self.verticalLayout.addLayout(self.layoutBotones)


        self.retranslateUi(FormularioMatricula)

        QMetaObject.connectSlotsByName(FormularioMatricula)
    # setupUi

    def retranslateUi(self, FormularioMatricula):
        FormularioMatricula.setWindowTitle(QCoreApplication.translate("FormularioMatricula", u"FormularioMatricula", None))
        self.lblTitulo.setText(QCoreApplication.translate("FormularioMatricula", u"Formulario de matr\u00edcula", None))
        self.lblSubtitulo.setText(QCoreApplication.translate("FormularioMatricula", u"Completa los datos para continuar", None))
        self.lblNombre.setText(QCoreApplication.translate("FormularioMatricula", u"Nombre", None))
        self.txtNombre.setText("")
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("FormularioMatricula", u"Nombre completo", None))
        self.lblCorreo.setText(QCoreApplication.translate("FormularioMatricula", u"Correo", None))
        self.txtCorreo.setText("")
        self.txtCorreo.setPlaceholderText(QCoreApplication.translate("FormularioMatricula", u"correo@ejemplo.com", None))
        self.cmbActividad.setItemText(0, QCoreApplication.translate("FormularioMatricula", u"Selecciona una actividad", None))
        self.cmbActividad.setItemText(1, QCoreApplication.translate("FormularioMatricula", u"Desarrollo de interfaces", None))
        self.cmbActividad.setItemText(2, QCoreApplication.translate("FormularioMatricula", u"Programaci\u00f3n con Python", None))
        self.cmbActividad.setItemText(3, QCoreApplication.translate("FormularioMatricula", u"Bases de datos", None))

        self.lblActividad.setText(QCoreApplication.translate("FormularioMatricula", u"Actividad", None))
        self.lblEstado.setText(QCoreApplication.translate("FormularioMatricula", u"Completa los datos obligatorios", None))
        self.chkCondiciones.setText(QCoreApplication.translate("FormularioMatricula", u"Aceptas los t\u00e9rminos y condiciones", None))
#if QT_CONFIG(tooltip)
        self.btnGuardar.setToolTip(QCoreApplication.translate("FormularioMatricula", u"Guarda la matr\u00edcula", None))
#endif // QT_CONFIG(tooltip)
        self.btnGuardar.setText(QCoreApplication.translate("FormularioMatricula", u"Guardar", None))
#if QT_CONFIG(tooltip)
        self.btnLimpiar.setToolTip(QCoreApplication.translate("FormularioMatricula", u"Borra todos los campos", None))
#endif // QT_CONFIG(tooltip)
        self.btnLimpiar.setText(QCoreApplication.translate("FormularioMatricula", u"Limpiar", None))
    # retranslateUi

