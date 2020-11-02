from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LogRecord(Base):
    __tablename__ = 'access_log'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(18), nullable=False)
    datetime = Column(DATETIME, nullable=False)
    timezone = Column(String(6), nullable=False)
    method = Column(String(8), nullable=False)
    url = Column(String(500), nullable=False)
    http_version = Column(String(10), nullable=False)
    status_code = Column(String(5), nullable=False)
    size = Column(Integer)
    referer = Column(String(1500))
    user_agent = Column(String(10000))

    def __repr__(self):
        return f"<LogRecord(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}'," \
               f"datetime='{self.datetime}'," \
               f"timezone='{self.timezone}'," \
               f"method='{self.method}'," \
               f"url='{self.url}'," \
               f"http_version='{self.http_version}'," \
               f"status_code='{self.status_code}'," \
               f"size='{self.size}'," \
               f"referer='{self.referer}'," \
               f"user-agent='{self.user_agent}'," \
               f")>"
