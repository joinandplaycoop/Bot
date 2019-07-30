# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class FactorioCommunityBanSync(Base):
    __tablename__ = 'Factorio_Community_Ban_Sync'

    Id_Factorio_Community_Ban_Sync = Column(INTEGER(255), primary_key=True)
    Rule = Column(String(200), nullable=False)
    Description = Column(String(200))
    Source_Credit = Column(String(200))
    Notes = Column(String(2000))


class Material(Base):
    __tablename__ = 'Material'

    Id_Material = Column(INTEGER(255), primary_key=True)
    Material_Name = Column(String(50), nullable=False)
    In_Game_Name = Column(String(100), nullable=False)


class Player(Base):
    __tablename__ = 'Players'

    Id_Players = Column(INTEGER(255), primary_key=True)
    Player = Column(String(50))
    Admin = Column(TINYINT(1), server_default=text("'0'"))


class Server(Base):
    __tablename__ = 'Server'

    Id_Server = Column(INTEGER(255), primary_key=True)
    Server = Column(String(50))
    Status = Column(String(50))
    Reseting = Column(TINYINT(4), server_default=text("'0'"))


class Ban(Base):
    __tablename__ = 'Ban'

    Id_Ban = Column(INTEGER(255), primary_key=True)
    FK_Player = Column(ForeignKey('Players.Id_Players'), nullable=False, index=True)
    FK_Ban_Sync = Column(ForeignKey('Factorio_Community_Ban_Sync.Id_Factorio_Community_Ban_Sync'), index=True)
    Reason = Column(String(600))

    Factorio_Community_Ban_Sync = relationship('FactorioCommunityBanSync')
    Player = relationship('Player')


class ConnectedServer(Base):
    __tablename__ = 'Connected_Server'

    Id_Connected_Server = Column(INTEGER(255), primary_key=True)
    FK_Player = Column(ForeignKey('Players.Id_Players'), index=True)
    FK_Server = Column(ForeignKey('Server.Id_Server'), index=True)

    Player = relationship('Player')
    Server = relationship('Server')


class PlayerPlaytime(Base):
    __tablename__ = 'Player_Playtime'

    Id_Player_Playtime = Column(INTEGER(255), primary_key=True)
    FK_Player = Column(ForeignKey('Players.Id_Players'), nullable=False, index=True)
    Date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    Ticks = Column(INTEGER(255), nullable=False)

    Player = relationship('Player')


class PlayersOnline(Base):
    __tablename__ = 'Players_Online'

    Id_Players_Online = Column(INTEGER(255), primary_key=True)
    FK_Player = Column(ForeignKey('Players.Id_Players'), index=True)
    FK_Server = Column(ForeignKey('Server.Id_Server'), index=True)

    Player = relationship('Player')
    Server = relationship('Server')


class Production(Base):
    __tablename__ = 'Production'

    Id_Production = Column(INTEGER(255), primary_key=True)
    FK_Material = Column(ForeignKey('Material.Id_Material'), nullable=False, index=True)
    FK_Server = Column(ForeignKey('Server.Id_Server'), nullable=False, index=True)
    Date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    Number_Produced = Column(BIGINT(20), nullable=False)

    Material = relationship('Material')
    Server = relationship('Server')


class Tick(Base):
    __tablename__ = 'Ticks'

    Id_Ticks = Column(INTEGER(255), primary_key=True)
    FK_Server = Column(ForeignKey('Server.Id_Server'), nullable=False, index=True)
    Date = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    Ticks = Column(INTEGER(255))
    Old_Ticks = Column(INTEGER(255))

    Server = relationship('Server')


class Log(Base):
    __tablename__ = 'Log'

    Id_Log = Column(BIGINT(255), primary_key=True)
    FK_Server = Column(ForeignKey('Server.Id_Server'), index=True)
    FK_Ticks = Column(ForeignKey('Ticks.Id_Ticks'), index=True)
    Date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    Number_Of_Players_Connected = Column(INTEGER(255))
    Number_Of_Total_Players = Column(INTEGER(255))
    Rockets_sended = Column(INTEGER(11))
    Alien_Evolution = Column(Float)

    Server = relationship('Server')
    Tick = relationship('Tick')
