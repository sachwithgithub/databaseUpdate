import MySQLdb,json
from logFile import my_log

class db_operations():
    def __init__(self):
        self.log = my_log()
        self.db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="capital")
        self.log.info("connetion to database successful")
        self.cur = self.db.cursor()


    def query(self):
        rows_count = 0
        try:
           cmd = "select * from employees"
           self.log.debug("command to be excuted:%s" %cmd)
           self.cur.execute(cmd)
           self.db.commit()
           self.log.debug("query from table successful")
           rows_count = self.cur.rowcount
           print("fetched rows:%s"%rows_count)
           self.log.info("%s rows fetched from table" %rows_count)
        except self.db.DatabaseError as db_error :
           print("Error in query")
           self.log.error(db_error)
           #self.db.rollback()
        except :
           self.log.error("Error in query")
           self.db.rollback()
        return json.dumps({'row':rows_count})


    def insert(self, request):
        req_data = request.get_json()
        self.log.debug("fetched id:%s"%req_data ['id'])
        id1 = req_data.get('id')
        first_name = req_data.get('first_name')
        last_name = req_data.get('last_name')
        rows_count = 0
        try:
           cmd = "insert into employees values(%s,'%s','%s')" %(id1,first_name,last_name)
           self.log.debug("command to be excuted:%s" %cmd)
           self.cur.execute(cmd)
           self.db.commit()
           self.log.debug("table updated successfully")
           rows_count = self.cur.rowcount
           print("inserted rows:%s"%rows_count)
           self.log.info("%s rows inserted from table" %rows_count)
        except self.db.DatabaseError as db_error :
           print("Error in insert")
           self.log.error(db_error)
           self.db.rollback()
        except :
           self.log.error("Error in insert")
           self.db.rollback()
        return json.dumps({'row':rows_count})


    def update(self, request):
        req_data = request.get_json()
        self.log.debug("update request for id:%s" %req_data ['id'])
        id1 = req_data.get('id')
        key = req_data.get('key')
        value = req_data.get('value')
        rows_count = 0
        try:
           cmd = "update employees set %s='%s' where id=%s" %(key,value,id1)
           self.log.debug("command to be executed:%s"%cmd)
           self.cur.execute(cmd)
           self.db.commit()
           rows_count = self.cur.rowcount
           self.log.debug("table updated successfully")
           print("updated rows:%s"%rows_count)
           self.log.info("%s rows updated from table" %rows_count)
        except self.db.DatabaseError as db_error :
           print("Error: in updating table")
           self.log.error(db_error)
           self.db.rollback()
        except :
           self.log.error("Error: in update")
           self.db.rollback()
        return json.dumps({'row':rows_count})


    def delete(self, request):
        req_data = request.get_json()
        self.log.debug("delete request for id:%s" %req_data ['id'])
        id1 = req_data.get('id')
        first_name = req_data.get('first_name')
        last_name = req_data.get('last_name')
        rows_count = 0
        try:
           cmd = "delete from employees where id=%s" %(id1)
           self.log.debug("command to be executed:%s"%cmd)
           self.cur.execute(cmd)
           self.db.commit()
           self.log.debug("table updated successfully")
           rows_count = self.cur.rowcount
           print("deleted rows:%s"%rows_count)
           self.log.info("%s rows deleted from table" %rows_count)
        except self.db.DatabaseError as db_error :
           print("Error in delete")
           self.log.error(db_error)
           self.db.rollback()
        except:
           self.log.error("Error in delete operation")
           self.db.rollback()
        return json.dumps({'row':rows_count})
