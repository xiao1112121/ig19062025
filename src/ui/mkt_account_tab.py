from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, 
                             QPushButton, QTableWidget, QTableWidgetItem, QComboBox,
                             QSpinBox, QLineEdit, QGroupBox, QCheckBox, QRadioButton,
                             QTextEdit, QProgressBar, QHeaderView, QSplitter)
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QFont
import json
import os

class MKTAccountTab(QWidget):
    """Tab Quản lý Tài khoản theo thiết kế MKT INSTA"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_sample_data()
        
    def init_ui(self):
        """Khởi tạo giao diện theo mẫu MKT"""
        # Layout chính
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Tạo splitter để có thể resize
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 1. Panel trái - Cấu hình
        left_panel = self.create_left_panel()
        splitter.addWidget(left_panel)
        
        # 2. Panel phải - Bảng dữ liệu
        right_panel = self.create_right_panel()
        splitter.addWidget(right_panel)
        
        # Thiết lập tỷ lệ: 30% trái, 70% phải
        splitter.setSizes([400, 800])
        
        main_layout.addWidget(splitter)
        
    def create_left_panel(self):
        """Tạo panel cấu hình bên trái"""
        panel = QFrame()
        panel.setObjectName("left_panel")
        panel.setMinimumWidth(350)
        panel.setMaximumWidth(450)
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)
        
        # Tiêu đề
        title = QLabel("Cấu Hình Nhận Tin")
        title.setStyleSheet("font-size: 16pt; font-weight: bold; color: #333; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Group 1: Cài đặt cơ bản
        basic_group = self.create_basic_settings()
        layout.addWidget(basic_group)
        
        # Group 2: Nhận tin theo danh sách username
        username_group = self.create_username_settings()
        layout.addWidget(username_group)
        
        # Buttons
        button_layout = self.create_action_buttons()
        layout.addLayout(button_layout)
        
        layout.addStretch()
        
        return panel
        
    def create_basic_settings(self):
        """Tạo group cài đặt cơ bản"""
        group = QGroupBox("Cài Đặt Cơ Bản")
        layout = QVBoxLayout(group)
        layout.setSpacing(10)
        
        # Hàng 1: Số lượng chạy đồng thời, Chuyển tài khoản sau
        row1 = QHBoxLayout()
        
        row1.addWidget(QLabel("Số lượng chạy đồng thời:"))
        self.concurrent_spin = QSpinBox()
        self.concurrent_spin.setRange(1, 10)
        self.concurrent_spin.setValue(5)
        self.concurrent_spin.setMinimumWidth(60)
        row1.addWidget(self.concurrent_spin)
        row1.addWidget(QLabel("lượng"))
        
        row1.addStretch()
        
        row1.addWidget(QLabel("Chuyển tài khoản sau:"))
        self.switch_spin = QSpinBox()
        self.switch_spin.setRange(1, 100)
        self.switch_spin.setValue(3)
        self.switch_spin.setMinimumWidth(60)
        row1.addWidget(self.switch_spin)
        row1.addWidget(QLabel("lần"))
        
        layout.addLayout(row1)
        
        return group
        
    def create_username_settings(self):
        """Tạo group cài đặt username"""
        group = QGroupBox()
        layout = QVBoxLayout(group)
        
        # Radio buttons
        self.username_radio = QRadioButton("Nhận tin theo danh sách username")
        self.username_radio.setChecked(True)
        layout.addWidget(self.username_radio)
        
        # Checkbox options
        self.avoid_duplicate_cb = QCheckBox("Các tài khoản không nhận trùng username")
        layout.addWidget(self.avoid_duplicate_cb)
        
        return group
        
    def create_action_buttons(self):
        """Tạo các nút hành động"""
        layout = QHBoxLayout()
        
        # START button
        self.start_btn = QPushButton("START")
        self.start_btn.setProperty("action", "start")
        self.start_btn.setMinimumHeight(40)
        self.start_btn.setMinimumWidth(100)
        layout.addWidget(self.start_btn)
        
        # STOP button  
        self.stop_btn = QPushButton("STOP")
        self.stop_btn.setProperty("action", "stop")
        self.stop_btn.setMinimumHeight(40)
        self.stop_btn.setMinimumWidth(100)
        layout.addWidget(self.stop_btn)
        
        layout.addStretch()
        
        return layout
        
    def create_right_panel(self):
        """Tạo panel bảng dữ liệu bên phải"""
        panel = QFrame()
        panel.setObjectName("right_panel")
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Header với dropdown và LOAD button
        header_layout = QHBoxLayout()
        
        # Dropdown chọn danh mục
        header_layout.addWidget(QLabel("Danh Sách Tài Khoản"))
        
        self.account_combo = QComboBox()
        self.account_combo.addItems(["Chọn danh mục tài khoản", "TK 1", "TK 2", "TK 3"])
        self.account_combo.setMinimumWidth(200)
        header_layout.addWidget(self.account_combo)
        
        self.load_btn = QPushButton("LOAD")
        self.load_btn.setProperty("action", "load")
        self.load_btn.setMinimumHeight(35)
        header_layout.addWidget(self.load_btn)
        
        header_layout.addStretch()
        
        # Thống kê
        stats_layout = QHBoxLayout()
        stats_layout.addWidget(QLabel("Tổng:"))
        self.total_label = QLabel("5")
        self.total_label.setStyleSheet("font-weight: bold; color: #333;")
        stats_layout.addWidget(self.total_label)
        
        stats_layout.addWidget(QLabel("Live:"))
        self.live_label = QLabel("4")
        self.live_label.setStyleSheet("font-weight: bold; color: #28a745;")
        stats_layout.addWidget(self.live_label)
        
        stats_layout.addWidget(QLabel("Die:"))
        self.die_label = QLabel("1")
        self.die_label.setStyleSheet("font-weight: bold; color: #dc3545;")
        stats_layout.addWidget(self.die_label)
        
        stats_layout.addStretch()
        
        header_layout.addLayout(stats_layout)
        layout.addLayout(header_layout)
        
        # Bảng dữ liệu
        self.account_table = QTableWidget()
        self.setup_table()
        layout.addWidget(self.account_table)
        
        return panel
        
    def setup_table(self):
        """Thiết lập bảng dữ liệu"""
        # Cột
        columns = ["STT", "Tên đăng nhập", "Mật khẩu", "Họ tên", "Trạng thái", 
                  "Giới tính", "Follower", "Following", "Proxy", "Hành động cuối"]
        
        self.account_table.setColumnCount(len(columns))
        self.account_table.setHorizontalHeaderLabels(columns)
        
        # Thiết lập header
        header = self.account_table.horizontalHeader()
        header.setStretchLastSection(True)
        
        # Thiết lập chiều rộng cột
        self.account_table.setColumnWidth(0, 50)   # STT
        self.account_table.setColumnWidth(1, 120)  # Username
        self.account_table.setColumnWidth(2, 100)  # Password
        self.account_table.setColumnWidth(3, 120)  # Họ tên
        self.account_table.setColumnWidth(4, 80)   # Trạng thái
        
        # Thiết lập alternating row colors
        self.account_table.setAlternatingRowColors(True)
        
        # Thiết lập selection behavior
        self.account_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
    def load_sample_data(self):
        """Load dữ liệu mẫu"""
        sample_data = [
            ["1", "isulieuhphuong", "xhYGYTInwlZd4", "", "Live", "", "=0", "=0", "", ""],
            ["2", "isumanahy", "RlnzTKIkdLQ", "", "Die", "", "=0", "=0", "", ""],
            ["3", "lychichen", "BQRshNczMekR", "", "Live", "", "=0", "=0", "", ""],
            ["4", "hasonnet4", "LLYKSpTgzUa", "", "Live", "", "=0", "=0", "", ""],
            ["5", "jacqueochad4", "KCLym3ZS50k", "", "Live", "", "=0", "=0", "", ""]
        ]
        
        self.account_table.setRowCount(len(sample_data))
        
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                
                # Màu sắc cho trạng thái
                if col == 4:  # Cột trạng thái
                    if value == "Live":
                        item.setForeground(Qt.GlobalColor.darkGreen)
                    elif value == "Die":
                        item.setForeground(Qt.GlobalColor.red)
                
                # Highlight hàng đầu tiên
                if row == 0:
                    item.setBackground(Qt.GlobalColor.cyan)
                
                self.account_table.setItem(row, col, item) 