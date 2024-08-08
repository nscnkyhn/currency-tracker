import sqlite3

class Database():
    """
        Database connection interface.
    """

    __database_filepath: str = "./assets/database.db"
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self):
        self.connection = sqlite3.connect(self.__database_filepath)
        self.cursor = self.connection.cursor()

    def find(self, tableName: str, fetchColumns: list = [], filter: dict = {}, limit: str = "", orderBy: dict = {}, groupBy: list = []):
        """
            Finds database records

            Args:
                1. table (str, required): Table name to fetch data from. Can not be empty.
                2. fetchColumns (list, optional): Column names to fetch in result. If not provided, all columns will be fetched. Can not be empty if groupBy is used.
                3. filter (dict, optional): Filtering parameters. All of the filter parameters will be connected with "AND" operator. (key = value). If not given, filter will not be applied.
                    Example: filter = {"id":"123", "name":"Jon"} => " id = 123 AND name = 'Jon' "
                4. limit (int, optional): Limit the fetched results with given amount. If not given, limit will not be applied.
                5. orderBy (dict, optional): Order the result by given orderBy keys with ascending or descending order (values)
                    Example: orderBy = {"id":"ASC", "date":"DESC"} => " ORDER BY id ASC, date DESC "
                6. groupBy (list, optional): Grouping the result with the given parameters. If used, fetchColumns must contains at least one appropriate aggregate function.
                    Example: fetchColumns = ["name", "count(likes)"] / groupBy = ["name"] => "SELECT name, count(likes) ... GROUP BY name"
        """
        assert tableName != "", "Table name can not be empty"

        selectColumns: str = "*"
        if (len(fetchColumns) != 0):
            selectColumns = fetchColumns.join(", ")

        filterList: list = []
        filterText: str = ""
        if (len(filter) != 0):
            for key, value in filter:
                filterList.append(f"{key} = {value}") 
            filterText = filterList.join(" AND ")

        if (len(limit) == 0):
            limit = ""
        else:
            limit = f"LIMIT {limit}"

        orderByList: list = []
        orderByText: str = ""
        if (len(orderBy) != 0):
            for key, value in filter:
                orderByList.append(f"{key} {value.upper()}") 
            orderByText = orderByList.join(", ")

        groupByText: str = ""
        if (len(groupBy) != 0):
            groupByText = groupBy.join(", ")

        query = f"SELECT {selectColumns} FROM {tableName} {filterText} {orderByText} {groupByText} {limit}"
        print(query)
        return db.cursor.execute(query).fetchall()
    
    def findOne(self, tableName: str, fetchColumns: list = [], filter: dict = {}):
        """
            Find a database record

            Args:
                1. table (str, required): Table name to fetch data from. Can not be empty.
                2. fetchColumns (list, optional): Column names to fetch in result. If not provided, all columns will be fetched. Can not be empty if groupBy is used.
                3. filter (dict, optional): Filtering parameters. All of the filter parameters will be connected with "AND" operator. (key = value). If not given, filter will not be applied.
                    Example: filter = {"id":"123", "name":"Jon"} => " id = 123 AND name = 'Jon' "
        """
        return self.find(tableName, fetchColumns, filter, "1")
    
    def runCustomQuery(self, query: str):
        """
            Run a custom query

            Args:
                1. query (str, required): Query to run. Can not be empty.
        """
        assert query != "", "query can not be empty."

        return db.cursor.execute(query).fetchall()




db = Database()
#dbCursor.execute("CREATE TABLE IF NOT EXISTS banks(name)")
#dbCursor.execute("INSERT INTO banks VALUES ('iş bankası'), ('akbank')")
#res = db.cursor.execute("SELECT * FROM banks")

res = db.find("banks")
print(res)
res = db.findOne("banks")
print(res)
#db.commit()