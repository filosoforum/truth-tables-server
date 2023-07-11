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

type Name = str
type Identifier = UUID | Name

# metaclass
@dataclass
class Tradeable(): # base class
    _id: Identifier

# exemplos de propriedades interessantes
class Fungible(ABC, Tradeable):
    def __init__(self) -> None: pass

    ???


# definir a estrutura de dados mais apropriada para lidar com os fungibles
# a ideia da bag é criar um contexto para que os fungibles se comportem como tal
# ou seja, por exemplo... se eu faço o stash de dinheiro em uma bag que já contém
# dinheiro, essas diferentes instancias de dinheiro, como objetos do python, deveriam
# se tornar apenas uma coisa só.

# e o UUID? o que acontece?
@dataclass
class Bag():
    def __init__(self) -> None:
        self._fungible_contents = {}
        self._non_fungible_contents = {}

    @property
    def contents(self) -> set[Tradeable]:
        bag = {}
        bag.add(self._fungible_contents).add(self._non_fungible_contents)
        return bag

    def stash(self, new_tradeable: Tradeable) -> Self:
        if not isinstance(new_tradeable, Fungible):
            self.contents.add(new_tradeable)
            return self

        fungibles = [fungible.__class__ for fungible in self._fungible_contents]
        
        
        if not self._does_fungible_exists(new_tradeable.__class__):
            self.contents.add(new_tradeable)
            return self

        for content in self.contents:
            if isinstance(new_tradeable, content.__class__):
                content.aggregate(new_tradeable)
                return self
            else:
                self.contents.add(new_tradeable)

    def _does_fungible_exists(fungible_class) -> bool:
        # verifica se a fungible class já está presente na bag
        pass

class Ticket(Tradeable):
    ticket_id

class Durable(Tradeable): pass


class TruthTable:
    def __init__(self) -> None:
        self.columns = set({
            Column("given", ColumnType(0)),    # sets of tradeables
            Column("received", ColumnType(0)), # sets of tradeables
            Column("when", ColumnType(1)),
            Column("where", ColumnType(0))
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

