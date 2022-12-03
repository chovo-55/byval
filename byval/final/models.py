from sqladmin import ModelView
from sqlmodel import SQLModel, Field


class Property(SQLModel, table=True):
    title: str
    id: int | None = Field(default=None, primary_key=True)
    street: str
    street_number: int
    floor: int
    longitude: int
    latitude: int
    number_of_rooms: int
    flag_migrant: int
    flag_low_budget: int
    flag_pensioner: int
    flag_newlyweds: int
    flag_handicap: int
    flag_orphanage: int
    flag_single_parent: int
    flag_regular: int


class Users(SQLModel, table=True):
    # __tablename__ = "Property"
    name: int
    surname: str
    id: int | None = Field(default=None, primary_key=True)
    age: str
    mail: int
    flag_migrant: int
    flag_low_budget: int
    flag_pensioner: int
    flag_newlyweds: int
    flag_handicap: int
    flag_orphanage: int
    flag_single_parent: int
    flag_regular: int


class PropertyAdmin(ModelView, model=Property):
    column_searchable_list = [Property.title]
    column_sortable_list = [Property.title, Property.id]
    column_list = [
        Property.title,
        Property.id,
        Property.street,
        Property.street_number,
        Property.longitude,
        Property.latitude,
        Property.number_of_rooms,
        Property.flag_migrant,
        Property.flag_low_budget,
        Property.flag_pensioner,
        Property.flag_newlyweds,
        Property.flag_handicap,
        Property.flag_orphanage,
        Property.flag_single_parent,
        Property.flag_regular
    ]

class UsersAdmin(ModelView, model=Users):
    column_searchable_list = [Users.name]
    column_sortable_list = [Users.name]
    column_list = [
        Users.name,
        Users.surname,
        Users.flag_migrant,
        Users.flag_low_budget,
        Users.flag_pensioner,
        Users.flag_newlyweds,
        Users.flag_handicap,
        Users.flag_orphanage,
        Users.flag_single_parent,
        Users.flag_regular
    ]
