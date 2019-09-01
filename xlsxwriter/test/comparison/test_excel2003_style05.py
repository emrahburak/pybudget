###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2019, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('excel2003_style05.xlsx')

        self.ignore_elements = {'xl/drawings/drawing1.xml':
                                ['<xdr:cNvPr', '<a:picLocks',
                                 '<a:srcRect/>', '<xdr:spPr',
                                 '<a:noFill/>']}

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file."""

        workbook = Workbook(self.got_filename, {'excel2003_style': True})

        worksheet = workbook.add_worksheet()

        worksheet.insert_image('B3', self.image_dir + 'red.jpg')

        workbook.close()

        self.assertExcelEqual()
