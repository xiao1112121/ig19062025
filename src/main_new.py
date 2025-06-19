import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFrame, QLabel, QPushButton, QSplitter,
                             QStackedWidget, QButtonGroup)
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

class MKTInstaMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Khởi tạo giao diện theo mẫu MKT INSTA"""
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
        
        # 1. Tạo Header
        self.create_header(main_layout)
        
        # 2. Tạo Content (Sidebar + Main Content)
        self.create_content(main_layout)
        
        # 3. Tạo Footer
        self.create_footer(main_layout)
        
    def create_header(self, parent_layout):
        """Tạo header gradient với logo"""
        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(80)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        # Logo và tên ứng dụng
        logo_layout = QVBoxLayout()
        
        app_name = QLabel("MKT INSTA")
        app_name.setObjectName("logo")
        app_name.setStyleSheet("color: white; font-size: 24pt; font-weight: bold;")
        
        version_info = QLabel("Version 2.0 - Update 19/06/2025")
        version_info.setObjectName("version")
        version_info.setStyleSheet("color: white; font-size: 10pt;")
        
        logo_layout.addWidget(app_name)
        logo_layout.addWidget(version_info)
        logo_layout.addStretch()
        
        header_layout.addLayout(logo_layout)
        header_layout.addStretch()
        
        # Logo MKT (nếu có file)
        try:
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
        except:
            pass
            
        parent_layout.addWidget(header)
        
    def create_content(self, parent_layout):
        """Tạo phần content với sidebar và main area"""
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Sidebar
        self.create_sidebar(content_layout)
        
        # Main content area
        self.create_main_area(content_layout)
        
        parent_layout.addWidget(content_widget)
        
    def create_sidebar(self, parent_layout):
        """Tạo sidebar với menu dọc"""
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 10)
        sidebar_layout.setSpacing(5)
        
        # Button group để quản lý selection
        self.sidebar_group = QButtonGroup()
        self.sidebar_group.setExclusive(True)
        
        # Danh sách menu items
        menu_items = [
            ("📊 Quản Lý Tài Khoản", "account"),
            ("📝 Quản Lý Nội Dung", "content"),
            ("💬 Quản Lý Tin Nhắn", "message"),
            ("🔍 Tương Tác Instagram", "interact"),
            ("👥 Chức Năng Follow", "follow"),
            ("🎬 Chức Năng Reels", "reels"),
            ("📈 Quét Dữ Liệu", "scanner"),
            ("🌐 Cập Nhật Thông Tin", "update")
        ]
        
        self.sidebar_buttons = {}
        
        for i, (text, key) in enumerate(menu_items):
            btn = QPushButton(text)
            btn.setProperty("sidebar", True)
            btn.setCheckable(True)
            btn.setMinimumHeight(45)
            btn.clicked.connect(lambda checked, k=key: self.switch_tab(k))
            
            self.sidebar_group.addButton(btn, i)
            self.sidebar_buttons[key] = btn
            sidebar_layout.addWidget(btn)
            
        sidebar_layout.addStretch()
        
        # Thông tin phiên bản
        info_layout = QVBoxLayout()
        
        status_items = [
            "📊 Cài đặt hệ thống",
            "📄 Phiên bản có gì mới?",
            "🔧 Hỗ trợ kỹ thuật hàng"
        ]
        
        for item in status_items:
            label = QLabel(item)
            label.setStyleSheet("color: #666; font-size: 9pt; padding: 3px;")
            info_layout.addWidget(label)
            
        sidebar_layout.addLayout(info_layout)
        
        # Buttons ở cuối sidebar
        button_layout = QHBoxLayout()
        
        status_btn = QPushButton("STATUS")
        status_btn.setStyleSheet("""
            QPushButton {
                background: #007bff;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 9pt;
                font-weight: bold;
            }
        """)
        
        privacy_btn = QPushButton("PRIVACY")
        privacy_btn.setStyleSheet("""
            QPushButton {
                background: #6c757d;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 9pt;
                font-weight: bold;
            }
        """)
        
        terms_btn = QPushButton("TERMS")
        terms_btn.setStyleSheet("""
            QPushButton {
                background: #17a2b8;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 9pt;
                font-weight: bold;
            }
        """)
        
        button_layout.addWidget(status_btn)
        button_layout.addWidget(privacy_btn)
        button_layout.addWidget(terms_btn)
        
        sidebar_layout.addLayout(button_layout)
        
        parent_layout.addWidget(sidebar)
        
    def create_main_area(self, parent_layout):
        """Tạo khu vực chính với stacked widget"""
        self.main_stack = QStackedWidget()
        self.main_stack.setObjectName("main_content")
        
        # Tạo các tab
        self.create_tabs()
        
        parent_layout.addWidget(self.main_stack)
        
        # Chọn tab đầu tiên
        self.sidebar_buttons["account"].setChecked(True)
        self.switch_tab("account")
        
    def create_tabs(self):
        """Tạo các tab content"""
        try:
            # Account Management Tab
            self.account_tab = MKTAccountTab()
            self.main_stack.addWidget(self.account_tab)
            
            # Messaging Tab  
            self.messaging_tab = MessagingTab(self.account_tab)
            self.main_stack.addWidget(self.messaging_tab)
            
            # Data Scanner Tab
            self.scanner_tab = DataScannerTab()
            self.main_stack.addWidget(self.scanner_tab)
            
            # Proxy Management Tab
            self.proxy_tab = ProxyManagementTab()
            self.main_stack.addWidget(self.proxy_tab)
            
            # Placeholder tabs cho các chức năng khác
            for i in range(4):
                placeholder = QWidget()
                placeholder_layout = QVBoxLayout(placeholder)
                
                title = QLabel("Chức năng đang phát triển...")
                title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                title.setStyleSheet("font-size: 18pt; color: #666; margin: 50px;")
                
                placeholder_layout.addWidget(title)
                self.main_stack.addWidget(placeholder)
                
        except Exception as e:
            print(f"Error creating tabs: {e}")
            traceback.print_exc()
            
    def create_footer(self, parent_layout):
        """Tạo footer"""
        footer = QFrame()
        footer.setObjectName("footer")
        footer.setFixedHeight(50)
        
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(20, 10, 20, 10)
        
        # Text bên trái
        footer_text = QLabel("Hiệu quả - Nhanh - Dễ dùng")
        footer_text.setObjectName("footer_text")
        footer_text.setStyleSheet("color: white; font-size: 14pt; font-weight: bold;")
        
        footer_layout.addWidget(footer_text)
        footer_layout.addStretch()
        
        # Website bên phải
        website_label = QLabel("🌐 phanmemmkt.vn")
        website_label.setObjectName("footer_url")
        website_label.setStyleSheet("color: #80c0ff; font-size: 12pt;")
        
        footer_layout.addWidget(website_label)
        
        parent_layout.addWidget(footer)
        
    def switch_tab(self, tab_key):
        """Chuyển đổi tab"""
        tab_mapping = {
            "account": 0,
            "content": 4,  # placeholder
            "message": 1,
            "interact": 5,  # placeholder
            "follow": 6,   # placeholder
            "reels": 7,    # placeholder
            "scanner": 2,
            "update": 3    # proxy tab
        }
        
        if tab_key in tab_mapping:
            self.main_stack.setCurrentIndex(tab_mapping[tab_key])

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
    window = MKTInstaMainWindow()
    window.show()
    
    sys.exit(app.exec()) 