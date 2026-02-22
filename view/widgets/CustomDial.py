from PySide6.QtWidgets import QDial
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtCore import Qt

class CustomDial(QDial):
    __instances = 0
    
    def __init__(self, parent=None):
        
        # * AFAIK we can't specify icon from designer's auto generated
        # * files, so I'm patching this up for now
        image_path = [":/icons/volDial.png", ":/icons/tuneDial.png"][CustomDial.__instances]
        CustomDial.__instances += 1

        super().__init__(parent)
        self.setMinimumSize(100, 100)
        self.original_image = QPixmap(image_path)
        if self.original_image.isNull():
            print(f"ERROR: Could not load image {image_path}")
        self.scaled_image = self.original_image
        self.setWrapping(False)
        
        size = min(self.width(), self.height())
        self.scaled_image = self.original_image.scaled(
            size, size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.update()

    def resizeEvent(self, event):
        size = min(self.width(), self.height())
        self.scaled_image = self.original_image.scaled(
            size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        
        w, h = self.width(), self.height()
        painter.translate(w / 2, h / 2)

        if self.maximum() != self.minimum():
            angle = (self.value() - self.minimum()) * 270.0 / (self.maximum() - self.minimum()) - 135.0
        else:
            angle = -135.0
        painter.rotate(angle)

        img_w = self.scaled_image.width()
        img_h = self.scaled_image.height()
        painter.translate(-img_w / 2, -img_h / 2)
        painter.drawPixmap(0, 0, self.scaled_image)

        painter.end()
