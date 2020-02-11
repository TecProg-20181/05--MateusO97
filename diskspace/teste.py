#import diskspace
from diskspace.diskspace import subprocess_check_output, print_tree, show_space_list , bytes_to_readable
import unittest
import os
import subprocess
from unittest import mock
import io
import sys

class DiskspaceTests(unittest.TestCase):
    
    def test_subprocess_check_output(self):
        command = 'du'
        du_result = subprocess.check_output(command)
        result = subprocess_check_output(command)
        self.assertEqual(du_result, result)

    def test_bytes_to_readable(self):
        blocks = 0
        result = bytes_to_readable(blocks)
        self.assertEqual('0.00B', result)

    def test_print_tree(self):
        capt = io.StringIO()
        sys.stdout = capt

        print_tree(self.file_tree, self.file_tree_node, self.path,
           self.largest_size, self.total_size)

        result = "6,00Kb 100% /home/mateus/05--MateusO97/diskspace"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, capt.getvalue())


    def test_show_space_list(self):
        capt = io.StringIO()
        sys.stdout = capt

        print_space_list(self.largest_size, self.file_tree, self.path,
           self.total_size)

        result = "  Size   (%)  File\n6,00Kb 100% /home/mateus/05--MateusO97/diskspace"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, capt.getvalue())
