from typing import Any, Type, TypeVar

from dataclasses import dataclass
from enum import Enum

from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.types import TypeEngine
from sqlalchemy.orm import DeclarativeBase, Mapped

from hashlib import sha256

_ColType = TypeVar("_ColType")

class TruthBase(DeclarativeBase):
    pass

def truth_table_factory(table_name: str):

    def mapper_args_factory():
        self.color = color
  
    def getColor(self):
        return self.color
  
    return type(f'T_{table_name}', (TruthBase,), {
        '__tablename__': f"t_{table_name}",
        
        'getColor': getColor,
    })
  
  
Apple = create_apple_class()
appleObj = Apple('red')
print(appleObj.getColor())

class TruthTable(TruthBase):
    __tablename__ = "TruthTable"
    id = M

class GlobalColumn(Column[_ColType]):

    def __init__(self, col_name: str, col_type: _ColType) -> None:
        


class ColumnType(Enum):
    STRING = 0
    TIMESTAMP = 1


class TableId:
    pass



class TruthTable:
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
        self.table = TruthTable()

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

