import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Publisher, Shop, Stock, Sale

DSN = 'postgresql://postgres:215047Qq@localhost:5432/netology_db'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()

publisher1=Publisher(id=1, name='Кинг')
publisher2=Publisher(id=2, name='Булгаков')
publisher3=Publisher(id=3, name='Пушкин')

book1 = Book(id=1, title='Мгла', id_publisher=1)
book2 = Book(id=2, title='Оно', id_publisher=1)
book3 = Book(id=3, title='Сияние', id_publisher=1)
book4 = Book(id=4, title='Противостояние', id_publisher=1)
book5 = Book(id=5, title='Бег', id_publisher=2)
book6 = Book(id=6, title='Кабала святош', id_publisher=2)
book7 = Book(id=7, title='Дни Турбининых', id_publisher=2)
book8 = Book(id=8, title='Евгений Онегин', id_publisher=3)

shop1=Shop(id=1, name='Буковед')
shop2=Shop(id=2, name='Лабиринт')
shop3=Shop(id=3, name='Книжный дом')

stock1=Stock(id_book=1, id_shop=1, count=110)
stock2=Stock(id_book=2, id_shop=1, count=120)
stock3=Stock(id_book=3, id_shop=1, count=130)
stock4=Stock(id_book=4, id_shop=1, count=140)
stock5=Stock(id_book=5, id_shop=2, count=150)
stock6=Stock(id_book=6, id_shop=2, count=160)
stock7=Stock(id_book=7, id_shop=2, count=170)
stock8=Stock(id_book=8, id_shop=2, count=180)
stock9=Stock(id_book=1, id_shop=2, count=190)
stock10=Stock(id_book=2, id_shop=3, count=200)
stock11=Stock(id_book=3, id_shop=3, count=400)
stock12=Stock(id_book=4, id_shop=3, count=300)
stock13=Stock(id_book=5, id_shop=3, count=500)

sale1=Sale(price=200, date_sale='21.07.2020', id_stock=1, count=1)
sale2=Sale(price=300, date_sale='12.08.2021', id_stock=2, count=2)
sale3=Sale(price=140, date_sale='11.09.2022', id_stock=3, count=3)
sale4=Sale(price=120, date_sale='30.07.2023', id_stock=4, count=1)
sale5=Sale(price=100, date_sale='29.06.2021', id_stock=5, count=2)
sale6=Sale(price=150, date_sale='27.02.2020', id_stock=6, count=1)
sale7=Sale(price=110, date_sale='01.03.2022', id_stock=7, count=3)
sale8=Sale(price=210, date_sale='02.03.2021', id_stock=8, count=1)
sale9=Sale(price=230, date_sale='02.11.2021', id_stock=9, count=4)
sale10=Sale(price=300, date_sale='06.10.2023', id_stock=10, count=1)
sale11=Sale(price=450, date_sale='07.01.2021', id_stock=11, count=5)
sale12=Sale(price=120, date_sale='09.01.2020', id_stock=12, count=1)
sale13=Sale(price=160, date_sale='19.12.2021', id_stock=13, count=2)
sale14=Sale(price=170, date_sale='16.10.2021', id_stock=1, count=1)
sale15=Sale(price=100, date_sale='15.08.2022', id_stock=2, count=2)
sale16=Sale(price=110, date_sale='19.09.2021', id_stock=4, count=1)


session.commit()


session.add_all([publisher1, publisher2, publisher3, book1, book2, book3, book4,
book5, book6, book7, book8, shop1, shop2, shop3, stock1, stock2, stock3, stock4, stock5, 
stock6, stock7, stock8, stock9, stock10, stock11, stock12, stock13, sale1, sale2, sale3,
sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12, sale13, sale14, sale15, sale16])


session.commit()

q = session.query(Publisher).join(Book.publisher).join(Stock.book).join(Sale.stock).filter(Sale.price>200)
print (q)