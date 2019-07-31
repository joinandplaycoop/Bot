# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BanRule(Base):
    __tablename__ = 'BanRules'

    Id = Column(INTEGER(255), primary_key=True)
    RuleName = Column(String(200), nullable=False)
    Description = Column(String(200))
    Source = Column(String(200))
    Notes = Column(String(2000))


class Material(Base):
    __tablename__ = 'Material'

    Id = Column(INTEGER(255), primary_key=True)
    MaterialName = Column(String(50), nullable=False)
    InGameName = Column(String(100), nullable=False)


class Player(Base):
    __tablename__ = 'Players'

    Id = Column(INTEGER(255), primary_key=True)
    PlayerName = Column(String(50))
    IsAdmin = Column(TINYINT(1), server_default=text("'0'"))


class Server(Base):
    __tablename__ = 'Server'

    Id = Column(INTEGER(255), primary_key=True)
    ServerName = Column(String(50))
    Status = Column(String(50))
    Version = Column(String(50))
    IP = Column(String(50))
    IsReseting = Column(TINYINT(1), server_default=text("'0'"))


class Ban(Base):
    __tablename__ = 'Ban'

    Id = Column(INTEGER(255), primary_key=True)
    FKPlayerId = Column(ForeignKey('Players.Id'), nullable=False, index=True)
    FKBanRuleId = Column(ForeignKey('BanRules.Id'), index=True)
    Reason = Column(String(600))

    BanRule = relationship('BanRule')
    Player = relationship('Player')


class ConnectedServer(Base):
    __tablename__ = 'ConnectedServer'

    Id = Column(INTEGER(255), primary_key=True)
    FKPlayerId = Column(ForeignKey('Players.Id'), index=True)
    FKServerId = Column(ForeignKey('Server.Id'), index=True)

    Player = relationship('Player')
    Server = relationship('Server')


class PlayerPlaytime(Base):
    __tablename__ = 'PlayerPlaytime'

    Id = Column(INTEGER(255), primary_key=True)
    FKPlayerId = Column(ForeignKey('Players.Id'), nullable=False, index=True)
    CreatedDate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    Ticks = Column(INTEGER(255), nullable=False)

    Player = relationship('Player')


class PlayersOnline(Base):
    __tablename__ = 'PlayersOnline'

    Id = Column(INTEGER(255), primary_key=True)
    FKPlayerId = Column(ForeignKey('Players.Id'), index=True)
    FKServerId = Column(ForeignKey('Server.Id'), index=True)

    Player = relationship('Player')
    Server = relationship('Server')


class Production(Base):
    __tablename__ = 'Production'

    Id = Column(INTEGER(255), primary_key=True)
    FKMaterialId = Column(ForeignKey('Material.Id'), nullable=False, index=True)
    FKServerId = Column(ForeignKey('Server.Id'), nullable=False, index=True)
    CreatedDate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    NumberProduced = Column(BIGINT(20), nullable=False)

    Material = relationship('Material')
    Server = relationship('Server')


class Tick(Base):
    __tablename__ = 'Ticks'

    Id = Column(INTEGER(255), primary_key=True)
    FKServerId = Column(ForeignKey('Server.Id'), nullable=False, index=True)
    CreatedDate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CurrentTicks = Column(INTEGER(255))
    OldTicks = Column(INTEGER(255))

    Server = relationship('Server')


class Log(Base):
    __tablename__ = 'Log'

    Id = Column(BIGINT(255), primary_key=True)
    FKServerId = Column(ForeignKey('Server.Id'), index=True)
    FKTicksId = Column(ForeignKey('Ticks.Id'), index=True)
    CreatedDate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    TotalPlayersOnline = Column(INTEGER(255))
    TotalPlayers = Column(INTEGER(255))
    RocketCount = Column(INTEGER(11))
    AlienEvolution = Column(Float)

    Server = relationship('Server')
    Tick = relationship('Tick')
