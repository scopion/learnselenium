# -*- coding:utf-8 -*-
# @File    : utils.py

import os
import Config

from sqlite3worker.sqlite3worker import Sqlite3Worker

def task_result(insert_sql=None):
    # 保存任务结果，使用sqlite3数据库

    if not os.path.exists(Config.TASK_RESULT):
        sql_worker = Sqlite3Worker(Config.TASK_RESULT, max_queue_size=160)
        task_result_table = """
        CREATE TABLE "task_result" (
                          "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                          "task_field" TEXT UNIQUE NOT NULL,
                          "flag" INTEGER
                        );
        """
        add_idx_task_result = """
        CREATE UNIQUE INDEX "index_task"
                            ON "task_result" (
                              "task_field" ASC
                        );
        """

        sql_worker.execute(task_result_table)
        sql_worker.close()
        sql_worker.execute(add_idx_task_result)
        sql_worker.close()

    if insert_sql:
        sql_worker = Sqlite3Worker(Config.TASK_RESULT, max_queue_size=160)
        sql_worker.execute(insert_sql)
        sql_worker.close()
