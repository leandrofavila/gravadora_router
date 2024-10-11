import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from ConDB import DB


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.db = DB()

    def keyPressEvent(self, event):
        # Verificar se o usuário pressionou Enter ou Tab
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter or event.key() == Qt.Key_Tab:
            self.updateFields()  # Chamar a função de atualização diretamente em vez de usar self.parent()
        else:
            # Continuar o comportamento normal
            super().keyPressEvent(event)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Ordem label and input
        ordem_label = QLabel('Ordem:')
        self.ordem_input = QLineEdit()
        grid.addWidget(ordem_label, 0, 0)# nome, posição linha, posição coluna
        grid.addWidget(self.ordem_input, 0, 1, 1, 3)

        # Tag label and input
        tag_label = QLabel('Tag:')
        self.tag_input = QLineEdit()
        grid.addWidget(tag_label, 1, 0)
        grid.addWidget(self.tag_input, 1, 1)

        # Ped label and auto-updating field
        ped_label = QLabel('Ped:')
        self.ped_output = QLabel('-')
        grid.addWidget(ped_label, 1, 2)
        grid.addWidget(self.ped_output, 1, 3)

        # Cod label and auto-updating field
        cod_label = QLabel('Cod:')
        self.cod_output = QLineEdit()
        grid.addWidget(cod_label, 2, 0)
        grid.addWidget(self.cod_output, 2, 1)

        # ID label and auto-updating field
        id_label = QLabel('ID:')
        self.id_output = QLineEdit()
        grid.addWidget(id_label, 2, 2)
        grid.addWidget(self.id_output, 2, 3)

        # Gravar button
        self.gravar_button = QPushButton('GRAVAR')
        grid.addWidget(self.gravar_button, 3, 3)
        # Conectar o botão à função que será chamada ao clicar no botão


        # Apply CSS-like styling
        self.setStyleSheet("""
            QWidget {
                background-color: #2C2C2C;
                color: #FFFFFF;
                font-family: 'Arial';
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #FFFFFF;
            }
            QLineEdit {
                padding: 5px;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                font-size: 14px;
                color: #000000;
                background-color: #FFFFFF;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                text-align: center;
                font-size: 14px;
                border-radius: 5px;
                margin: 5px 0;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def acao_gravar(self):
        # Aqui você coloca a lógica que deseja executar quando o botão for clicado 1177662
        ordem_value = self.ordem_input.text()
        if ordem_value:
            ped_value = self.db.pedido(ordem_value)
            print(str(self.tag_input.text()), ped_value, str(self.cod_output.text()), str(self.id_output.text()))

            # Atualizar os labels
            self.tag_input.setText(str(self.tag_input.text()))
            self.ped_output.setText(str(ped_value))
            self.cod_output.setText(str(self.cod_output.text()))
            self.id_output.setText(str(self.id_output.text()))

        else:
            print("Nenhuma ordem foi inserida.")


    def updateFields(self):
        ordem_value = self.ordem_input.text()
        if ordem_value:
            ped_value = self.db.pedido(ordem_value)
            print(ped_value, self.cod_output.text())
            #cod_value = "Query result for Cod"
            #id_value = "Query result for ID"

            # Atualizar os labels
            self.ped_output.setText(str(ped_value))
            #self.cod_output.setText(cod_value)
            #self.id_output.setText(id_value)

            self.gravar_button.clicked.connect(self.acao_gravar)
        else:
            # Limpar os campos se nenhum valor for inserido em Ordem
            self.ped_output.setText('-')
            #self.cod_output.setText('-')
            #self.id_output.setText('-')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Gravadora Router')
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec_())
