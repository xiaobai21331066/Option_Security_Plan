from sqlalchemy import create_engine
from unittest import TestCase

class DbBaseTestCase(TestCase):
    def setUp(self):
        self.engine = create_engine('mysql://root:b00377837@localhost/leetcode',
                                    encoding='utf-8',
                                    echo=False)

    def tearDown(self):
        pass