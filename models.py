import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50))

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, nullable=False ) 
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))
    
    publisher = relationship(Publisher, backref='books')
    
    def __str__(self):
        return f'{self.id}: {self.title}, {self.id_publisher}'

class Shop(Base):
    __tablename__='shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)

    

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='shop')
    # saless = relationship('Sale', back_populates='stock')
    def __str__(self):
            return f'{self.id}: {self.id_book}, {self.id_shop}, {self.count}'


class Sale(Base):
    __tablename__='sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='saless')

    def __str__(self):
        return f'{self.id}: {self.price}, {self.date_sale}, {self.id_stock}, {self.count}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
