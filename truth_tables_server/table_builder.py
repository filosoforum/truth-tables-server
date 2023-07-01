from typing import Any

from dataclasses import dataclass
from enum import Enum


class ColumnType(Enum):
    STRING = 0
    TIMESTAMP = 1


class TableId:
    pass


@dataclass
class Column:
    name: str
    data_type: ColumnType


@dataclass
class FKColumn(Column):
    associated_table_id: TableId


class Table:
    def __init__(self) -> None:
        self.columns = set({
            Column("name", ColumnType(0)), # eu
            Column("cost", ColumnType(0)), # o mundo
            Column("datetime", ColumnType(1)) # e o tempo
        }) 
        self.fk_columns = set()
        pass

    def setColumn(self, column_name: str, data_type: ColumnType):
        self.columns.add(Column(column_name, data_type))
        return self

    def setFKColumn(
        self, column_name: str, data_type: ColumnType, table_id: TableId
    ) -> None:
        self.fk_columns.add(FKColumn(column_name, data_type, table_id))

    def update_table(self, linha: Any): pass


class TableBuilder:
    def __init__(self) -> None:
        self.table = Table()

    def addColumn(self, *args):
        self.table.setColumn(*args)

    def addFKColumn(self, *args): pass

    def build(self):
        # cria o schema da table
        return self

table = TableBuilder() \
        .addColumn("coluna X", "enfim") \
        .addColumn("coluna Y", "blabla") \
        .addFKColumn("a outra table", "nome da colune", "bla bla bla") \
        .build()

