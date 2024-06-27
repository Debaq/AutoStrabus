import os
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, QHBoxLayout, QHeaderView, QMessageBox, QApplication
from PySide6.QtCore import Qt, Signal
import datetime

class FileTableWidget(QWidget):
    btn_action = Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Archivo", "Fecha de creación", "Numero de medidas"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Select entire row
        self.table.setShowGrid(False)  # Hide cell lines
        
        self.button_layout = QHBoxLayout()
        
        #self.refresh_button = QPushButton("Refresh List")
        #self.refresh_button.clicked.connect(self.populate_table)
        #self.button_layout.addWidget(self.refresh_button)
        
        self.open_button = QPushButton("Abrir")
        self.open_button.clicked.connect(self.open_file)
        self.button_layout.addWidget(self.open_button)
        
        self.new_button = QPushButton("Nuevo")
        self.new_button.clicked.connect(self.new_file)
        self.button_layout.addWidget(self.new_button)
        
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.button_layout)
        self.open = False
        self.table.itemDoubleClicked.connect(self.copy_cell)
        self.table.itemChanged.connect(self.handle_item_changed)
        self.cell_prev_old_text = None
        self.populate_table()

    def copy_cell(self, cell):
        self.cell_prev_old_text = cell.text()
        
    def populate_table(self):
        self.table.setRowCount(0)
        
        folder_path = 'record'
        if not os.path.exists(folder_path):
            return
        
        filenames_set = set()
        
        for filename in os.listdir(folder_path):
            if filename.endswith(".avi"):
                name_without_extension = filename.replace(".avi", "")
                if name_without_extension in filenames_set:
                    continue
                filenames_set.add(name_without_extension)
                
                file_path = os.path.join(folder_path, filename)
                creation_time = os.path.getctime(file_path)
                creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                
                json_file = filename.replace(".avi", ".json")
                json_path = os.path.join(folder_path, json_file)
                
                if os.path.exists(json_path):
                    with open(json_path, 'r') as f:
                        try:
                            data = json.load(f)
                            number_of_measures = len(data.get("marks", []))
                        except json.JSONDecodeError:
                            number_of_measures = 0
                else:
                    number_of_measures = 0
                
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                
                filename_item = QTableWidgetItem(name_without_extension)
                filename_item.setFlags(filename_item.flags() | Qt.ItemIsEditable)
                self.table.setItem(row_position, 0, filename_item)
                self.table.setItem(row_position, 1, QTableWidgetItem(creation_date))
                self.table.setItem(row_position, 2, QTableWidgetItem(str(number_of_measures)))
                
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)
        for i in range(self.table.columnCount() - 1):
            self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        
        self.open = True

    def open_file(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            file_name = selected_items[0].text()
            file_path = os.path.join('record', file_name + ".avi")
            # Aquí puedes implementar la lógica para abrir el archivo
            self.btn_action.emit(["open",file_path])

    def new_file(self):
        # Aquí puedes implementar la lógica para crear un nuevo archivo
        self.btn_action.emit(["new" ,True])

    
    def handle_item_changed(self, item):
        if item.column() == 0 and self.open:  # Only handle changes in the first column
            old_name = self.cell_prev_old_text
            new_name = item.text()
            row = item.row()
            #old_name = self.table.item(row, 0).text()
            
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setText(f"Estas seguro que deseas renombrar de {old_name} a {new_name}?")
            msg_box.setWindowTitle("Confirma el cambio de nombre")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result = msg_box.exec()
            
            if result == QMessageBox.Yes:
                if self.rename_files(old_name, new_name):
                    pass
                    #self.populate_table()
                else:
                    item.setText(old_name)
            else:
                item.setText(old_name)

    def rename_files(self, old_name, new_name):
        folder_path = 'record'
        old_avi_path = os.path.join(folder_path, old_name + ".avi")
        old_json_path = os.path.join(folder_path, old_name + ".json")
        new_avi_path = os.path.join(folder_path, new_name + ".avi")
        new_json_path = os.path.join(folder_path, new_name + ".json")
        
        base_new_name = new_name
        counter = 1
        while os.path.exists(new_avi_path) or os.path.exists(new_json_path):
            new_name = f"{base_new_name}_{counter}"
            new_avi_path = os.path.join(folder_path, new_name + ".avi")
            new_json_path = os.path.join(folder_path, new_name + ".json")
            counter += 1
            
        try:
            os.rename(old_avi_path, new_avi_path)
            if os.path.exists(old_json_path):
                os.rename(old_json_path, new_json_path)
            return True
        except Exception as e:
            print(f"Error renaming files: {e}")
            return False

# Ejemplo de uso:
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = QWidget()
    layout = QVBoxLayout(main_window)
    file_table_widget = FileTableWidget()
    layout.addWidget(file_table_widget)
    main_window.setLayout(layout)
    main_window.show()
    sys.exit(app.exec())
