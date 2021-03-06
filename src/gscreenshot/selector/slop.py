import subprocess
from gscreenshot.selector import SelectionParseError, SelectionExecError


class Slop(object):

    """
    Python class wrapper for the slop region selection tool

    All methods return a tuple of; the x, y coordinates
    of both corners of the selection.
    """

    def __init__(self):
        """
        constructor
        """
        pass

    def region_select(self):
        """
        Select an arbitrary region of the screen

        Returns:
           (x top left, y top left, x bottom right, y bottom right)
        """
        return self._get_boundary_interactive()

    def window_select(self):
        """
        Selects a window from the screen

        Returns:
           (x top left, y top left, x bottom right, y bottom right)
        """
        return self._get_boundary_interactive()

    def grab_window(self, delay=0):
        """
        Takes an interactive screenshot of a selected window with a
        given delay

        Parameters:
            int delay: seconds
        """
        self.grab_selection(delay)

    def _get_boundary_interactive(self):
        """
        Calls slop and returns the boundary produced by
        slop
        """
        try:
            # nodecorations=0 - this is the slop default, but there's a bug
            # so skipping the "=0" causes a segfault.
            proc_output = subprocess.check_output(['slop', '--nodecorations=0', '-f', 'X=%x,Y=%y,W=%w,H=%h'])
        except subprocess.CalledProcessError:
            raise SelectionExecError("Slop failed to return a selection")

        slop_output = proc_output.decode("UTF-8").strip().split(",")

        slop_parsed = {}
        # We iterate through the output so we're not reliant
        # on the order or number of lines in slop's output
        for l in slop_output:
            spl = l.split("=")
            slop_parsed[spl[0]] = spl[1]

        # (left, upper, right, lower)
        try:
            crop_box = (
                int(slop_parsed['X']),
                int(slop_parsed['Y']),
                int(slop_parsed['X']) + int(slop_parsed['W']),
                int(slop_parsed['Y']) + int(slop_parsed['H'])
            )
        except KeyError:
            raise SelectionParseError("Unexpected slop output")

        return crop_box
