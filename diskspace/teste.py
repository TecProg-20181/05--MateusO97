from diskspace import *
import unitttest
import os
import StringIO
import subprocess
import mock
import io
import sys

class DiskspaceTests(unnittest.TestCase):
    
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
        capt = StringIO.StringIO()
        sys.stdout = capt

        print_tree(self.file_tree, self.file_tree_node, self.path,
           self.largest_size, self.total_size)

        result = "6,00Kb 100% /home/mateus/05--MateusO97/diskspace"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, capt.getvalue())


    def test_show_space_list(self):
        capt = StringIO.StringIO()
        sys.stdout = capt

        print_space_list(self.largest_size, self.file_tree, self.path,
           self.total_size)

         result = "  Size   (%)  File\n6,00Kb 100% /home/mateus/05--MateusO97/diskspace"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, capt.getvalue())
