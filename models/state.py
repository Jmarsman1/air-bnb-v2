#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
import sqlalchemy


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    id = sqlalchemy.orm.column_property(Column(Integer, primary_key=True, nullable=False))
    
