"""
ActorDirector 表：

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp 是这张表的主键.
 

写一条SQL查询语句获取合作过至少三次的演员和导演的 id 对 (actor_id, director_id)

示例：

ActorDirector 表：
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+

Result 表：
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
唯一的 id 对是 (1, 1)，他们恰好合作了 3 次。
"""

import unittest
import pandas as pd
import logging

from .db_base_testcase  import DbBaseTestCase
from .db_1050 import mysql_method, pd_method

logging.basicConfig(level=logging.DEBUG)

class TestLeetCodeDb1050(DbBaseTestCase):

    def fill_data(self):
        sqls = [
            "Create table If Not Exists ActorDirector (actor_id int, director_id int, timestamp int)",
            "Truncate table ActorDirector",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '0')",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '1')",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '2')",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '3')",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '4')",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '5')",
            "insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '6')"]
        with self.engine.begin() as conn:
            for sql in sqls:
                conn.execute(sql)

    def test_pd_1(self):
        self.fill_data()
        df = pd.read_sql_table('ActorDirector'.lower(), con=self.engine)
        logging.debug('df %s', df)
        pd_result = pd_method(df)
        print(pd_result)
        logging.debug('pd_result %s', pd_result)
        sql_result = pd.read_sql_query(mysql_method, con=self.engine)
        logging.debug('sql_result %s', sql_result)


        self.assertListEqual(list(pd_result.columns), list(sql_result.columns))
        self.assertListEqual(list(pd_result.index), list(sql_result.index))
        self.assertListEqual(list(pd_result.values), list(sql_result.values))

if __name__ == '__main__':
    unittest.main()
