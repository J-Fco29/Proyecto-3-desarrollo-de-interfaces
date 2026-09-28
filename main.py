import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_formulario import Ui_FormularioMatricula


class VentanaMatricula(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormularioMatricula()
        self.ui.setupUi(self)
        self.conectar_eventos()
        self.actualizar_estado()

    def conectar_eventos(self):
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.txtNombre.textChanged.connect(self.actualizar_estado)
        self.ui.txtCorreo.textChanged.connect(self.actualizar_estado)
        self.ui.cmbActividad.currentIndexChanged.connect(self.actualizar_estado)
        self.ui.chkCondiciones.checkStateChanged.connect(self.actualizar_estado)

    def formulario_valido(self):
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        nombre_valido = len(nombre) >= 3
        correo_valido = "@" in correo and "." in correo.split("@")[-1]
        actividad_valida = self.ui.cmbActividad.currentIndex() != 0
        condiciones_aceptadas = self.ui.chkCondiciones.isChecked()

        return nombre_valido and correo_valido and actividad_valida and condiciones_aceptadas

    def actualizar_estado(self):
        valido = self.formulario_valido()
        self.ui.btnGuardar.setEnabled(valido)

        if valido:
            self.ui.lblEstado.setText("Formulario preparado para guardar")
        else:
            self.ui.lblEstado.setText("Revisa los datos obligatorios")

    def limpiar(self):
        self.ui.txtNombre.clear()
        self.ui.txtCorreo.clear()
        self.ui.cmbActividad.setCurrentIndex(0)
        self.ui.chkCondiciones.setChecked(False)
        self.ui.txtNombre.setFocus()
        self.actualizar_estado()

    def guardar(self):
        if not self.formulario_valido():
            QMessageBox.warning(self, "Formulario incompleto", "Revisa los datos antes de continuar")
            return

        nombre = self.ui.txtNombre.text().strip()
        actividad = self.ui.cmbActividad.currentText()

        respuesta = QMessageBox.question(
            self,
            "Confirmar matrícula",
            f"¿Deseas registrar a {nombre} en {actividad}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Matrícula completada", f"{nombre} ha sido registrado correctamente")
            self.limpiar()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaMatricula()
    ventana.show()
    sys.exit(app.exec())