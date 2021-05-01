from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction

from logic import main

if __name__ == "__main__":
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # Create the icon
    icon = QIcon("icon.svg")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    def quit():
        main()

    # Create the menu
    menu = QMenu()

    action = QAction("Start Audio Listening") 
    action.triggered.connect(main)
    menu.addAction(action)

    # Add a Quit option to the menu.
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    app.exec_()