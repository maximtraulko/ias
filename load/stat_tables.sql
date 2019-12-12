# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class LdStatDatum(Base):
    __tablename__ = 'ld_stat_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_stat_data_id_seq'::regclass)"))
    region = Column(String(1000))
    okved = Column(String(1000))
    year_for = Column(Integer)
    e = Column(Numeric(12, 2))
    f = Column(Numeric(12, 2))
    g = Column(Numeric(12, 2))
    h = Column(Numeric(12, 2))
    i = Column(Numeric(12, 2))
    j = Column(Numeric(12, 2))
    k = Column(Numeric(12, 2))
    l = Column(Numeric(12, 2))
    m = Column(Numeric(12, 2))
    n = Column(Numeric(12, 2))
    o = Column(Numeric(12, 2))
    p = Column(Numeric(12, 2))
    q = Column(Numeric(12, 2))
    r = Column(Numeric(12, 2))
    s = Column(Numeric(12, 2))
    t = Column(Numeric(12, 2))
    u = Column(Numeric(12, 2))
    v = Column(Numeric(12, 2))
    w = Column(Numeric(12, 2))
    x = Column(Numeric(12, 2))
    y = Column(Numeric(12, 2))
    z = Column(Numeric(12, 2))
    aa = Column(Numeric(12, 2))
    ab = Column(Numeric(12, 2))
    ac = Column(Numeric(12, 2))
    ad = Column(Numeric(12, 2))
    ae = Column(Numeric(12, 2))
    af = Column(Numeric(12, 2))
    ag = Column(Numeric(12, 2))
    ah = Column(Numeric(12, 2))
    ai = Column(Numeric(12, 2))
    aj = Column(Numeric(12, 2))
    ak = Column(Numeric(12, 2))
    al = Column(Numeric(12, 2))
    am = Column(Numeric(12, 2))
    an = Column(Numeric(12, 2))
    ao = Column(Numeric(12, 2))
    ap = Column(Numeric(12, 2))
    aq = Column(Numeric(12, 2))
    ar = Column(Numeric(12, 2))
    AS = Column(Numeric(12, 2))
    at = Column(Numeric(12, 2))
    au = Column(Numeric(12, 2))
    av = Column(Numeric(12, 2))
    aw = Column(Numeric(12, 2))
    ax = Column(Numeric(12, 2))
    ay = Column(Numeric(12, 2))
    az = Column(Numeric(12, 2))
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class StatParamName(Base):
    __tablename__ = 'stat_param_name'

    id = Column(Integer, primary_key=True, server_default=text("nextval('stat_param_name_id_seq'::regclass)"))
    ord_num = Column(Integer, nullable=False, unique=True)
    col_name = Column(String(3))
    name = Column(String(512), nullable=False, unique=True)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class LdStatData2(Base):
    __tablename__ = 'ld_stat_data2'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_stat_data2_id_seq'::regclass)"))
    region = Column(String(1000))
    year_for = Column(Integer)
    az = Column(Numeric(12, 2))
    ba = Column(Numeric(12, 2))
    bb = Column(Numeric(12, 2))
    bc = Column(Numeric(12, 2))
    bd = Column(Numeric(12, 2))
    be = Column(Numeric(12, 2))
    bf = Column(Numeric(12, 2))
    bg = Column(Numeric(12, 2))
    bh = Column(Numeric(12, 2))
    bi = Column(Numeric(12, 2))
    bj = Column(Numeric(12, 2))
    bk = Column(Numeric(12, 2))
    bl = Column(Numeric(12, 2))
    bm = Column(Numeric(12, 2))
    bn = Column(Numeric(12, 2))
    bo = Column(Numeric(12, 2))
    bp = Column(Numeric(12, 2))
    bq = Column(Numeric(12, 2))
    br = Column(Numeric(12, 2))
    bs = Column(Numeric(12, 2))
    bt = Column(Numeric(12, 2))
    bu = Column(Numeric(12, 2))
    bv = Column(Numeric(12, 2))
    bw = Column(Numeric(12, 2))
    bx = Column(Numeric(12, 2))
    by = Column(Numeric(12, 2))
    bz = Column(Numeric(12, 2))
    ca = Column(Numeric(12, 2))
    cb = Column(Numeric(12, 2))
    cc = Column(Numeric(12, 2))
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class LdStatData3(Base):
    __tablename__ = 'ld_stat_data3'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_stat_data3_id_seq'::regclass)"))
    region = Column(String(1000))
    type_migration = Column(String(1000))
    year_for = Column(Integer)
    d = Column(Integer)
    e = Column(Integer)
    f = Column(Integer)
    g = Column(Integer)
    h = Column(Integer)
    i = Column(Integer)
    j = Column(Integer)
    k = Column(Integer)
    l = Column(Integer)
    m = Column(Integer)
    n = Column(Integer)
    o = Column(Integer)
    p = Column(Integer)
    q = Column(Integer)
    r = Column(Integer)
    s = Column(Integer)
    t = Column(Integer)
    u = Column(Integer)
    v = Column(Integer)
    w = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
    aa = Column(Integer)
    ab = Column(Integer)
    ac = Column(Integer)
    ad = Column(Integer)
    ae = Column(Integer)
    af = Column(Integer)
    ag = Column(Integer)
    ah = Column(Integer)
    ai = Column(Integer)
    aj = Column(Integer)
    ak = Column(Integer)
    al = Column(Integer)
    am = Column(Integer)
    an = Column(Integer)
    ao = Column(Integer)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class StatParamName3(Base):
    __tablename__ = 'stat_param_name3'

    id = Column(Integer, primary_key=True, server_default=text("nextval('stat_param_name3_id_seq'::regclass)"))
    ord_num = Column(Integer, nullable=False, unique=True)
    col_name = Column(String(3))
    name = Column(String(512), nullable=False, unique=True)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class StatParamName4(Base):
    __tablename__ = 'stat_param_name4'

    id = Column(Integer, primary_key=True, server_default=text("nextval('stat_param_name4_id_seq'::regclass)"))
    ord_num = Column(Integer, nullable=False, unique=True)
    col_name = Column(String(3))
    name = Column(String(512), nullable=False, unique=True)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class StatParamName4(Base):
    __tablename__ = 'stat_param_name4'

    id = Column(Integer, primary_key=True, server_default=text("nextval('stat_param_name4_id_seq'::regclass)"))
    ord_num = Column(Integer, nullable=False, unique=True)
    col_name = Column(String(3))
    name = Column(String(512), nullable=False, unique=True)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class LdStatData4(Base):
    __tablename__ = 'ld_stat_data4'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_stat_data4_id_seq'::regclass)"))
    region = Column(String(1000))
    type_age = Column(String(1000))
    year_for = Column(Integer)
    d = Column(Integer)
    e = Column(Integer)
    f = Column(Integer)
    g = Column(Integer)
    h = Column(Integer)
    i = Column(Integer)
    j = Column(Integer)
    k = Column(Integer)
    l = Column(Integer)
    m = Column(Integer)
    n = Column(Integer)
    o = Column(Integer)
    p = Column(Integer)
    q = Column(Integer)
    r = Column(Integer)
    s = Column(Integer)
    t = Column(Integer)
    u = Column(Integer)
    v = Column(Integer)
    w = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
    aa = Column(Integer)
    ab = Column(Integer)
    ac = Column(Integer)
    ad = Column(Integer)
    ae = Column(Integer)
    af = Column(Integer)
    ag = Column(Integer)
    ah = Column(Integer)
    ai = Column(Integer)
    aj = Column(Integer)
    ak = Column(Integer)
    al = Column(Integer)
    am = Column(Integer)
    an = Column(Integer)
    ao = Column(Integer)
    ap = Column(Integer)
    ar = Column(Integer)
    a_s = Column(Integer)
    at = Column(Integer)
    au = Column(Integer)
    av = Column(Integer)
    aw = Column(Integer)
    ax = Column(Integer)
    ay = Column(Integer)
    az = Column(Integer)
    ba = Column(Integer)
    bb = Column(Integer)
    bc = Column(Integer)
    bd = Column(Integer)
    be = Column(Integer)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class StatAgeDeath(Base):
    __tablename__ = 'stat_age_death'

    id = Column(Integer, primary_key=True, server_default=text("nextval('stat_age_death_id_seq'::regclass)"))
    age = Column(Integer, nullable=False)
    prob = Column(Float(53))
    date_add = Column(DateTime, nullable=False, server_default=text("now()"))
