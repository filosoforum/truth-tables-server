from dataclasses import dataclass
from typing import List
from enum import Enum

AddressType = Enum("AddressType", ["Coords", "Network", "MagicWord"])

@dataclass
class Location:
    name: str # PK
    address_type: AddressType
    address: str
    meta: dict

def new_location(addr_type: AddressType, location: str):

def table_from_location_and_purpose() -> PurposedTable:

    return PurposedTable(schema: SchemaTemplate(), location, relationship, tags)


@dataclass
class Purpose:
    description: str # Human readable description to be propagated
    tags: set[str] # Tags that allow to group purposes
    relationship: str # the name of the relationship to the external world that it describes
    location: Location

@dataclass
class Relationship:
     

@dataclass
class RelationshipGroup:
    relationships: set[str] # a set of relationships
    group_name: str
    group_description: str
    group_tags: set[str]
    
@dataclass
class 

    


class PurposedTable:

    def __init__(self) -> None:
        self.Purpose = Purpose()
    
    def insert_element():
