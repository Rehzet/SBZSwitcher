import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sbz_data

MARGIN = 15

class GridWindow(Gtk.Window):
    def getEmptySquare(self, border=False):

        if border:
            empty_square = Gtk.Frame()
        else:
            empty_square = Gtk.Box()
        empty_square.set_hexpand(True)
        empty_square.set_vexpand(True)
        return empty_square

    def __init__(self):

        super().__init__(title="Sound Blaster Z Switcher")

        self.grid = Gtk.Grid()
        self.grid.set_row_homogeneous(False)
        self.grid.set_column_homogeneous(False)
        # self.grid.set_hexpand(True)

        self.grid.attach(self.getEmptySquare(True), 0, 0, 3, 1)

        # Headset volume bar
        headset_label = Gtk.Label("Headphones volume")
        headset_label.set_margin_left(MARGIN)
        headset_label.set_margin_right(MARGIN)
        self.grid.attach(headset_label, 0, 1, 1, 1)

        headset_volume = Gtk.Scale().new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1.0)
        headset_volume.set_value(sbz_data.get_headphones_volume())
        headset_volume.set_draw_value(True)
        headset_volume.set_value_pos(1)
        headset_volume.set_hexpand(True)
        headset_volume.set_margin_right(MARGIN)
        headset_volume.connect("value-changed", self.on_headphones_volume_value_changed)
        self.grid.attach_next_to(headset_volume, headset_label, Gtk.PositionType.RIGHT, 1, 1)

        self.grid.attach_next_to(self.getEmptySquare(True), headset_volume, Gtk.PositionType.RIGHT, 1, 1)


        # Speakers volume bar
        speakers_label = Gtk.Label("Speakers volume")
        speakers_label.set_margin_left(MARGIN)
        speakers_label.set_margin_right(MARGIN)
        self.grid.attach(speakers_label, 0, 2, 1, 1)

        speakers_volume = Gtk.Scale().new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1.0)
        speakers_volume.set_value(sbz_data.get_speakers_volume())
        speakers_volume.set_draw_value(True)
        speakers_volume.set_value_pos(1)
        speakers_volume.set_hexpand(True)
        speakers_volume.set_margin_right(MARGIN)
        speakers_volume.connect("value-changed", self.on_speakers_volume_value_changed)
        self.grid.attach_next_to(speakers_volume, speakers_label, Gtk.PositionType.RIGHT, 1, 1)

        self.grid.attach_next_to(self.getEmptySquare(True), speakers_volume, Gtk.PositionType.RIGHT, 1, 1)


        self.add(self.grid)

        self.set_default_size(700, 600)


    def on_headphones_volume_value_changed(self, range):
        sbz_data.set_headphones_volume(range.get_value())
        print(range.get_value())

    def on_speakers_volume_value_changed(self, range):
        sbz_data.set_speakers_volume(range.get_value())
        print(range.get_value())


def create_window():
    win = GridWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()



