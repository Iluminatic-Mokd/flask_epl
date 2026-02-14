from epl import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Club(db.Model):
    __tablename__ = 'clubs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    stadium: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[str] = mapped_column(String(200), nullable=True)
    players: Mapped[List["Player"]] = relationship(back_populates="club")
    
    def __repr__ (self) -> str:
        return f'<Club: {self.name}>'

class Player(db.Model):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    nationality: Mapped[str] = mapped_column(String(50), nullable=False)
    goal: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
    img: Mapped[str] = mapped_column(String(200), nullable=True)
    club_id: Mapped[int] = mapped_column(Integer, ForeignKey('clubs.id'))
    
    club: Mapped["Club"] = relationship(back_populates="players")
    
    def __repr__(self) -> str:
        return f'<Player: {self.name}>'
        