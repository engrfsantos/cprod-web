from sqlalchemy import Boolean, Column, Double, Time, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import datetime, time

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base
 
class Status(Base):
    __tablename__ = "ts01_status"
    id: int = Column("ts01_status", Integer, primary_key=True, nullable=False)
    desc_breve: str = Column("ts01_desc_breve", String,nullable=False)
    descricao: str = Column("ts01_descricao", String,nullable=False)

class Processo(Base):
    __tablename__ = "td01_identificador"
    id: str = Column("td01_id",String, primary_key=True, nullable=False) #td01_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    desc_breve: str = Column("td01_desc_breve", String) #td01_desc_breve character varying(10) COLLATE pg_catalog."default" NOT NULL,
    descricao: str = Column("td01_descricao",String) #td01_descricao character varying(50) COLLATE pg_catalog."default",
    status_id: str = Column("td01_status",String) #td01_status character varying(2) COLLATE pg_catalog."default",
    local_id: str = Column("td01_local", String, primary_key=True, nullable=False ) #td01_local character varying(5) COLLATE pg_catalog."default" NOT NULL,
    reparo: bool = Column("td01_reparo",Boolean) #td01_reparo boolean,
    autoconfrede: bool = Column("td01_autoconfrede",Boolean) #td01_autoconfrede boolean,
    burnin: bool = Column("td01_burnin",Boolean) # td01_burnin boolean,
    fechaos: str = Column("td01_fechaos",String) # td01_fechaos character varying(1) COLLATE pg_catalog."default" DEFAULT 0,
    obrpn: bool = Column("td01_obrpn",Boolean) # td01_obrpn boolean,
    tipoid: str = Column("td01_tipoid",String) # td01_tipoid character varying(8) COLLATE pg_catalog."default" DEFAULT 0,

class Defeito(Base):
    __tablename__ = "td01_defeito"
    id: int = Column("td01_defeito_id", Integer, primary_key=True, nullable=False)
    descricao: str = Column("td01_descricao", String, nullable=False)
    ean: str = Column("td01_ean", String)
    grupo_id: str = Column("td01_grupo", String)
    codigo_id: str = Column("td01_codigo", String)
    agrupar: str = Column("td01_agrupar", String)
    categoria: str = Column("td01_categoria", String, nullable=False, default="Geral")
    

 
class Produto(Base):
    __tablename__ = 'ts01_produto'
    id: str = Column("ts01_codigo", String,  primary_key=True, nullable=False) 
    descricao: str = Column("ts01_descricao", String) 
    narrativa: str = Column("ts01_narrativa",String)
    unidade: str = Column("ts01_unidade",String)
    descricao_especifica: str = Column("ts01_desc_esp",String)
    grupo: str = Column("ts01_grupo",String)
    cod_barras: str = Column("ts01_cod_barras",String)
    tipo: str = Column("td01_tipo",String) 
 
# class Usuario(Base):   
#     __tablename__ = 'ts01_usuario'
#     re: str = Column("re", String,  primary_key=True,nullable=False)
#     usuario: str = Column("usuario", String)
#     senha: str = Column("senha", String)
#     nome: str = Column("nome", String)
#     status:str = Column("status", String, default="A")
#     perfil: str = Column("perfil", String)
#     local: str = Column("local", String)   
    
class Grupo(Base):
    __tablename__ = "ts01_grupo"
    grupo: str = Column("ts01_grupo", String, primary_key=True,nullable=False)
    desc_grupo: str = Column("ts01_descgrupo", String)
    desc_brev: str = Column("ts01_descbrevgrupo")
    nivel: float = Column("ts01_nivel")
    cmplx: str = Column("ts01_cmplx", String)
    tpad_cq: str = Column("ts01_tpad_cq", Double, default=0.25)
    tpad_lab : float = Column("ts01_tpad_lab", Double, default=0.25)
    tpad_prod : float = Column("ts01_tpad_prod", Double, default=0.25)
    nqa : float = Column("ts01_nqa", Double, default=0.25)   
    
class Post(Base):
    __tablename__ = 'posts'
    id =  Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content= Column(String, nullable=True)
    published = Column(Boolean, nullable=True, default=True)
    rate = Column(Integer, nullable=True)
    post_date = Column(DateTime, default=datetime.time, nullable=False)
    
class User(Base):
    __tablename__ = "users"
    id  = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active  = Column(Boolean, default=True)
    items = relationship("Item")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    description = Column(String)
       
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")