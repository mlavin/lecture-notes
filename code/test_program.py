import os
import program
import unittest


class GetInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'test.csv'
        self.test_data = [
            ('A', 'Foo', 'Bar'),
            ('B', 'Foo', 'Bar'),
            ('C', 'Foo', 'Bar')
        ]
        self.write_test_file(self.test_data)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def write_test_file(self, data):
        with open(self.test_filename, 'w') as test_file:
            test_file.write('"Symbol","Sector","Industry",\n')
            for row in data:
                cols = ','.join([str(x) for x in row])
                test_file.write(cols + '\n')

    def test_data_read(self):
        result = program.get_symbol_info(self.test_filename)
        self.assertEqual(result, self.test_data)

    def test_handle_invalid(self):
        invalid_data = [
            ('A', 'Foo', 'Bar'),
            ('B', program.INVALID_STRING, 'Bar'),
            ('C', 'Foo', 'Bar')
        ]
        self.write_test_file(invalid_data)
        result = program.get_symbol_info(self.test_filename)
        self.assertTrue(invalid_data[1] not in result)

    def test_missing_file(self):
        os.remove(self.test_filename)
        result = program.get_symbol_info(self.test_filename)
        self.assertEqual(result, [])


class IndustryFilterTestCase(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            ('A', 'Foo', 'Industry 1'),
            ('B', 'Foo', 'Industry 2'),
            ('C', 'Foo', 'Industry 1')
        ]

    def test_simple_filter(self):
        result = program.filter_by_industry(self.test_data, 'Industry 1')
        self.assertEqual(len(result), 2)

    def test_case_insensitive(self):
        result = program.filter_by_industry(self.test_data, 'industry 1')
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()
