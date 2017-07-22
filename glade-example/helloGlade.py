import sys

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit()


class HelloGTK:
    """
    This is a PyGTK/Glade test application.
    """
    def __init__(self):
        # Set the glade file
        self.gladefile = "helloGlade.glade"
        self.wTree = gtk.glade.XML(self.gladefile)

        # Handle connectors
        dic = {"on_main_button_clicked" : self.main_button_clicked,
               "on_main_button_destroy" : gtk.main_quit}
        self.wTree.signal_autoconnect(dic)

        # Set the Main Window and connect the "destroy" event
        self.window = self.wTree.get_widget("MainWindow")
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)

    def main_button_clicked(self, widget):
            print "Hello, World!"

if __name__ == '__main__':
    program = HelloGTK()
    gtk.main()

