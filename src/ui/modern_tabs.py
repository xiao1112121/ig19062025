"""
Modern Tab Widget với icons theo mẫu MKT INSTA
"""

from PySide6.QtWidgets import QTabWidget, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont

class ModernTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_modern_style()
    
    def setup_modern_style(self):
        """Setup modern styling cho tabs"""
        # Set tab position
        self.setTabPosition(QTabWidget.TabPosition.North)
        
        # Set tab shape
        self.setTabShape(QTabWidget.TabShape.Rounded)
        
        # Enable tab close buttons if needed
        self.setTabsClosable(False)
        self.setMovable(False)
        
        # Set modern font
        font = QFont("Segoe UI", 11)
        font.setBold(True)
        self.setFont(font)
    
    def add_tab_with_icon(self, widget: QWidget, icon_text: str, title: str):
        """Thêm tab với icon emoji"""
        tab_title = f"{icon_text} {title}"
        return self.addTab(widget, tab_title)
    
    def setup_instagram_tabs(self, tabs_data):
        """Setup tabs theo mẫu Instagram tool"""
        tab_configs = [
            ("👥", "QUẢN LÝ TÀI KHOẢN"),
            ("💬", "QUẢN LÝ NỘI DUNG"), 
            ("📱", "QUẢN LÝ TIN NHẮN"),
            ("📊", "TƯƠNG TÁC INSTAGRAM"),
            ("👁️", "CHỨC NĂNG THEO DÕI"),
            ("🎬", "CHỨC NĂNG REELS"),
            ("🔍", "QUÉT DỮ LIỆU"),
            ("⚙️", "CẬP NHẬT THÔNG TIN")
        ]
        
        for i, (widget, (icon, title)) in enumerate(zip(tabs_data, tab_configs)):
            if widget:
                self.add_tab_with_icon(widget, icon, title)
    
    def set_tab_colors(self):
        """Set màu sắc cho tabs theo theme"""
        # Được handle bởi CSS
        pass 