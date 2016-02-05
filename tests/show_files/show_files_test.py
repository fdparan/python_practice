import os
import unittest

from show_files import show


class ShowFilesTest(unittest.TestCase):

    FILES = ['samp{}'.format(x) for x in range(5)]
    PARENT = os.path.abspath('.')

    @classmethod
    def setUpClass(cls):

        print 'Creating samp files...'

        cls.__change_files(cls.__create)

    @classmethod
    def __create(cls, f):
        with open(f, 'w'):
            pass
            # print '{} created'.format(f)

    def test_canonical_returns_absolute_path(self):

        self.assertEquals(show.canonical('.'), self.PARENT)

        for f in self.FILES:
            self.assertEquals(show.canonical(f), os.path.join(self.PARENT, f))

        os.chdir('/Users/francisparan/Dropbox/Programming/python/python_practice')
        self.assertEquals(show.canonical('/tests/show_files/samp0'), os.path.join(self.PARENT, 'samp0'))
        os.chdir(self.PARENT)

    def test_show_files_prints_out_files_in_order(self):
        expected_files = '\n'.join(os.path.join(self.PARENT, f) for f in self.FILES)

        self.assertIn(expected_files, show.show_files(self.PARENT))

    def test_subdirs_returns_all_files_as_dirs(self):
        home = '/Users/francisparan'

        expected = [os.path.join(home, f) for f in os.listdir(home) if os.path.isdir(os.path.join(home, f))]

        self.assertEquals(expected, list(show.subdirs(home)))

    @classmethod
    def tearDownClass(cls):

        print 'Cleaning up samp files...'

        cls.__change_files(os.remove)

    @classmethod
    def __change_files(cls, func):

        for f in cls.FILES:
            func(f)

if __name__ == '__main__':
    unittest.main()
