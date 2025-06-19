import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFrame, QLabel, QPushButton, QTabWidget,
                             QSplitter)
from PySide6.QtGui import QFont, QPixmap, QPalette, QLinearGradient, QBrush, QColor
from PySide6.QtCore import Qt, QSize
import os
import traceback
import logging

# Thêm thư mục gốc của dự án vào sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import các tab
try:
    from src.ui.mkt_account_tab import MKTAccountTab
    from src.ui.proxy_management import ProxyManagementTab
    from src.ui.messaging import MessagingTab
    from src.ui.data_scanner import DataScannerTab
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

class MKTInstaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Khởi tạo giao diện đúng theo mẫu MKT INSTA"""
        self.setWindowTitle("MKT INSTA - Instagram Automation Tool")
        self.setGeometry(100, 100, 1400, 900)
        self.setMinimumSize(1200, 800)
        
        # Widget chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout chính (dọc)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # 1. Header gradient
        self.create_header(main_layout)
        
        # 2. Tab Widget (navigation ngang)
        self.create_tab_widget(main_layout)
        
        # 3. Footer
        self.create_footer(main_layout)
        
    def create_header(self, parent_layout):
        """Tạo header gradient với logo và version"""
        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(80)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        # Logo và version bên trái
        logo_layout = QVBoxLayout()
        
        app_name = QLabel("MKT INSTA")
        app_name.setStyleSheet("color: white; font-size: 24pt; font-weight: bold;")
        
        version_info = QLabel("Version 2.0 - Update 19/06/2025")
        version_info.setStyleSheet("color: white; font-size: 10pt;")
        
        logo_layout.addWidget(app_name)
        logo_layout.addWidget(version_info)
        
        header_layout.addLayout(logo_layout)
        header_layout.addStretch()
        
        # Logo MKT bên phải
        mkt_logo = QLabel("MKT")
        mkt_logo.setStyleSheet("""
            color: white; 
            font-size: 32pt; 
            font-weight: bold;
            background: rgba(255,255,255,0.2);
            border-radius: 10px;
            padding: 5px 15px;
        """)
        header_layout.addWidget(mkt_logo)
            
        parent_layout.addWidget(header)
        
    def create_tab_widget(self, parent_layout):
        """Tạo tab widget với navigation ngang (đúng theo mẫu)"""
        self.tab_widget = QTabWidget()
        
        # Tạo các tab
        try:
            # Tab 1: Quản lý Tài khoản
            account_tab = MKTAccountTab()
            self.tab_widget.addTab(account_tab, "QUẢN LÝ TÀI KHOẢN")
            
            # Tab 2: Quản lý Nội dung  
            content_tab = QWidget()
            content_layout = QVBoxLayout(content_tab)
            content_layout.addWidget(QLabel("Quản lý Nội dung - Đang phát triển"))
            self.tab_widget.addTab(content_tab, "QUẢN LÝ NỘI DUNG")
            
            # Tab 3: Quản lý Tin nhắn
            messaging_tab = MessagingTab(None)
            self.tab_widget.addTab(messaging_tab, "QUẢN LÝ TIN NHẮN")
            
            # Tab 4: Tương tác Instagram
            interact_tab = QWidget()
            interact_layout = QVBoxLayout(interact_tab)
            interact_layout.addWidget(QLabel("Tương tác Instagram - Đang phát triển"))
            self.tab_widget.addTab(interact_tab, "TƯƠNG TÁC INSTAGRAM")
            
            # Tab 5: Chức năng Follow
            follow_tab = QWidget()
            follow_layout = QVBoxLayout(follow_tab)
            follow_layout.addWidget(QLabel("Chức năng Follow - Đang phát triển"))
            self.tab_widget.addTab(follow_tab, "CHỨC NĂNG FOLLOW")
            
            # Tab 6: Chức năng Reels
            reels_tab = QWidget()
            reels_layout = QVBoxLayout(reels_tab)
            reels_layout.addWidget(QLabel("Chức năng Reels - Đang phát triển"))
            self.tab_widget.addTab(reels_tab, "CHỨC NĂNG REELS")
            
            # Tab 7: Quét dữ liệu
            scanner_tab = DataScannerTab()
            self.tab_widget.addTab(scanner_tab, "QUÉT DỮ LIỆU")
            
            # Tab 8: Cập nhật thông tin
            update_tab = ProxyManagementTab()
            self.tab_widget.addTab(update_tab, "CẬP NHẬT THÔNG TIN")
            
        except Exception as e:
            print(f"Error creating tabs: {e}")
            traceback.print_exc()
            
        parent_layout.addWidget(self.tab_widget)
        
    def create_footer(self, parent_layout):
        """Tạo footer"""
        footer = QFrame()
        footer.setObjectName("footer")
        footer.setFixedHeight(50)
        
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(20, 10, 20, 10)
        
        # Text bên trái
        footer_text = QLabel("Hiệu quả - Nhanh - Dễ dùng")
        footer_text.setStyleSheet("color: white; font-size: 14pt; font-weight: bold;")
        
        footer_layout.addWidget(footer_text)
        footer_layout.addStretch()
        
        # Website bên phải
        website_label = QLabel("🌐 phanmemmkt.vn")
        website_label.setStyleSheet("color: #80c0ff; font-size: 12pt;")
        
        footer_layout.addWidget(website_label)
        
        parent_layout.addWidget(footer)

def apply_mkt_style(app):
    """Áp dụng style MKT INSTA"""
    try:
        with open("src/style_new.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Style file not found, using default style")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Áp dụng style
    apply_mkt_style(app)
    
    # Tạo và hiển thị window
    window = MKTInstaWindow()
    window.show()
    
    sys.exit(app.exec()) 