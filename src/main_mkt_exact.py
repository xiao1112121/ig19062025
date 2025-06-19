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

class MKTWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MKT INSTA")
        self.setGeometry(100, 100, 1400, 900)
        self.setup_ui()
        
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(80)
        header_layout = QHBoxLayout(header)
        
        logo = QLabel("🔥 MKT INSTA")
        logo.setObjectName("logo") 
        version = QLabel("Version 1.2 - Update 19/06/2025")
        version.setObjectName("version")
        
        header_layout.addWidget(logo)
        header_layout.addWidget(version)
        header_layout.addStretch()
        
        # Tabs
        self.tabs = QTabWidget()
        
        # Create tabs with sidebars
        self.create_account_tab()
        self.create_content_tab() 
        self.create_scanner_tab()
        self.create_settings_tab()
        
        # Footer
        footer = QFrame()
        footer.setObjectName("footer")
        footer.setFixedHeight(40)
        footer_layout = QHBoxLayout(footer)
        
        footer_text = QLabel("🚀 Hiệu quả - Nhanh - Dễ dùng | 🌐 phanmemmkt.vn")
        footer_text.setObjectName("footer_text")
        footer_layout.addWidget(footer_text)
        
        layout.addWidget(header)
        layout.addWidget(self.tabs)
        layout.addWidget(footer)
        
    def create_tab_with_sidebar(self, content_widget, sidebar_items):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Sidebar
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)
        
        for item in sidebar_items:
            btn = QPushButton(item)
            btn.setProperty("role", "sidebar")
            sidebar_layout.addWidget(btn)
        sidebar_layout.addStretch()
        
        layout.addWidget(sidebar)
        layout.addWidget(content_widget)
        return tab
        
    def create_account_tab(self):
        try:
            content = AccountManagementTab()
            sidebar_items = ["📋 Thêm Danh Mục", "👤 Thêm Tài Khoản", "🎯 Chọn Cột Hiển Thị"]
            tab = self.create_tab_with_sidebar(content, sidebar_items)
            self.tabs.addTab(tab, "📊 QUẢN LÝ TÀI KHOẢN")
        except Exception as e:
            print(f"Error creating account tab: {e}")
            
    def create_content_tab(self):
        try:
            content = MessagingTab(None)
            sidebar_items = ["📋 Thêm Danh Mục", "📝 Thêm Bài Viết"]  
            tab = self.create_tab_with_sidebar(content, sidebar_items)
            self.tabs.addTab(tab, "📝 QUẢN LÝ NỘI DUNG")
        except Exception as e:
            print(f"Error creating content tab: {e}")
            
    def create_scanner_tab(self):
        try:
            content = DataScannerTab()
            sidebar_items = ["🔍 Quét Tài Khoản Theo Dõi", "👥 Quét Tài Khoản Theo Từ Khóa"]
            tab = self.create_tab_with_sidebar(content, sidebar_items)  
            self.tabs.addTab(tab, "🔍 QUÉT DỮ LIỆU")
        except Exception as e:
            print(f"Error creating scanner tab: {e}")
            
    def create_settings_tab(self):
        try:
            content = ProxyManagementTab()
            sidebar_items = ["🌐 Cài đặt hệ thống", "❓ Phiên bản có gì mới?"]
            tab = self.create_tab_with_sidebar(content, sidebar_items)
            self.tabs.addTab(tab, "⚙️ CẬP NHẬT THÔNG TIN") 
        except Exception as e:
            print(f"Error creating settings tab: {e}")

def main():
    app = QApplication(sys.argv)
    
    # Load CSS
    try:
        with open("src/style_mkt_exact.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except:
        pass
        
    window = MKTWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 