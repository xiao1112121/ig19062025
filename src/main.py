#!/usr/bin/env python3
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Import tabs
from src.ui.account_management import AccountManagementTab
from src.ui.messaging import MessagingTab  
from src.ui.data_scanner import DataScannerTab
from src.ui.proxy_management import ProxyManagementTab

class MKTCorrectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ABCDBET")
        self.resize(1200, 850)
        
        # Căn giữa màn hình
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - 1200) // 2
        y = (screen_geometry.height() - 850) // 2
        self.move(x, y)
        
        self.setup_ui()
        
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header - ĐÚNG theo mẫu
        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(80)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        # Logo và version info
        logo_section = QWidget()
        logo_layout = QVBoxLayout(logo_section)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        
        logo = QLabel("🔥 ABCDBET")
        logo.setObjectName("logo")
        logo.setStyleSheet("color: white; font-size: 22pt; font-weight: bold;")
        
        version = QLabel("Version 1.2 - Update 19/06/2025")
        version.setObjectName("version")
        version.setStyleSheet("color: rgba(255, 255, 255, 0.9); font-size: 9pt;")
        
        logo_layout.addWidget(logo)
        logo_layout.addWidget(version)
        
        header_layout.addWidget(logo_section)
        header_layout.addStretch()
        
        # Tabs - ĐÚNG theo mẫu (chỉ tabs ngang, KHÔNG có sidebar)
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        
        # Tạo các tabs ĐÚNG theo mẫu
        self.create_account_tab()
        self.create_messaging_tab() 
        self.create_scanner_tab()
        self.create_proxy_tab()
        
        # Thêm vào layout chính - BỎ FOOTER
        layout.addWidget(header)
        layout.addWidget(self.tabs)
        
    def create_account_tab(self):
        """Tab Quản lý tài khoản - KHÔNG có sidebar"""
        try:
            content = AccountManagementTab()
            self.tabs.addTab(content, "👥 QUẢN LÝ TÀI KHOẢN")
        except Exception as e:
            print(f"Error creating account tab: {e}")
            
    def create_messaging_tab(self):
        """Tab Tin nhắn - KHÔNG có sidebar"""
        try:
            content = MessagingTab(None)
            self.tabs.addTab(content, "📝 TIN NHẮN")
        except Exception as e:
            print(f"Error creating messaging tab: {e}")
            
    def create_scanner_tab(self):
        """Tab Quét dữ liệu - KHÔNG có sidebar"""
        try:
            content = DataScannerTab()
            self.tabs.addTab(content, "🔍 QUÉT DỮ LIỆU")
        except Exception as e:
            print(f"Error creating scanner tab: {e}")
            
    def create_proxy_tab(self):
        """Tab Quản lý proxy - KHÔNG có sidebar"""
        try:
            content = ProxyManagementTab()
            self.tabs.addTab(content, "🌐 QUẢN LÝ PROXY")
        except Exception as e:
            print(f"Error creating proxy tab: {e}")

def main():
    app = QApplication(sys.argv)
    
    # Load CSS
    try:
        with open("src/style_mkt_exact.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except:
        pass
        
    window = MKTCorrectWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 