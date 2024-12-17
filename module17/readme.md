# Module17: SQLAlchemy - Set of tools to manipulate SQL

![image_01](./pics/1.jpg)

Welcome to the seventeenth bootcamp class!

Object-Relational Mapping (ORM) is a technique that allows you to query and manipulate data from a database using an object-oriented paradigm. When talking about ORM, most people are referring to a library that implements the Object-Relational Mapping technique, hence the phrase "an ORM".

[Excalidraw:](https://link.excalidraw.com/l/8pvW6zbNUnD/3tmGeQYjxeG)

## Introduction to SQL Alchemy

An ORM library is a completely common library written in the language of your choice that encapsulates the code needed to manipulate data, so you no longer use SQL; you interact directly with an object in the same language you are using.

### Why should we use ORM?

- DRY: You write your data model in just one place, and it's easier to update, maintain and reuse the code.

- You don't need to write your mock SQL (most programmers are not good at this, because SQL is treated as a "sub" language, when in reality it is a very powerful and complex language).

- Sanitization; Using prepared statements or transactions is as easy as calling a method.

- It fits naturally into your Python code.

- It abstracts the DB system, so you can change it whenever you want.

### Installation

First, make sure SQLAlchemy is installed. If not, you can install it using pip:

```bash
pip install sqlalchemy
```

### Connecting to SQLite (Hello world!)

SQLite is a lightweight database that is great for learning the basics of SQLAlchemy. Here is a basic example of how to create a connection engine for an in-memory SQLite database:

```python
from sqlalchemy import create_engine

# Connect to SQLite in memory
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Connection to SQLite established.")
```

![engine](./pics/engine.png)

[Serves different "Dialect"](https://docs.sqlalchemy.org/en/20/core/engines.html)  

### Creating our MAPPING

![engine](./pics/mapping.png)


Before inserting or querying data, we need to define the models and create corresponding tables in the database:

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create tables in the database
Base.metadata.create_all(engine)
```

### Creating Sessions and Entering Data

Sessions in SQLAlchemy are used to maintain a 'workspace' of all object operations that you want to synchronize with the database:

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='João', age=28)
session.add(new_user)
session.commit()

print("User entered successfully.")
```

### Querying Data

Now, let's query the data to verify the insertion:

```python
user = session.query(User).filter_by(name='João').first()
print(f"User found: {user.name}, Age: {user.age}")
```

### Using Session with With

The `with` context manager in Python, especially when used with SQLAlchemy, is an elegant and secure way to ensure that resources such as database connections and sessions are properly managed. When using `with`, you benefit from automatic context entry and exit, which means that at the end of the `with` block, SQLAlchemy automatically closes the session or commits/rollbacks, depending on the result of the operation. This helps prevent connection leaks and ensures that transactions are properly managed.

### Advantages of Using `with` with SQLAlchemy

* **Automatic transaction management**: Transactions are automatically committed or rolled back depending on whether exceptions were thrown within the block.
* **Automatic closing of sessions**: This ensures that resources are released in a timely manner, preventing connection leaks.

### Example Without Using `with`

Without using the context manager, you need to manually manage the session, including commits, rollbacks, and closing the session:

```python
from sqlalchemy.orm import sessionmaker
# assuming that engine has already been created

Session = sessionmaker(bind=engine)
session = Session()

try:
    new_user = User(name='Ana', age=25)
    session.add(new_user)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
```

In this example, all the steps to ensure that the session is properly managed are explicit: committing changes, handling exceptions, rolling back if something goes wrong, and, finally, closing the session.

### Example Using `with`

When you use the `with` context manager, many of these steps are automated:

```python
from sqlalchemy.orm import sessionmaker, Session
# assuming that engine has already been created

Session = sessionmaker(bind=engine)

with Session() as session:
    new_user = User(name='Ana', age=25)
    session.add(new_user)
    # Commit is automatically done here if there are no exceptions
    # Rollback is automatically called if an exception occurs
    # The session is automatically closed when leaving the with block
```

In the example above, SQLAlchemy handles the commit, rollback and session closure automatically. If an exception occurs within the `with` block, a rollback is called. When the `with` block completes without errors, the commit is performed, and in both cases, the session is automatically closed at the end.

### Conclusion

The main advantage of using the `with` context manager with SQLAlchemy (or any other feature that requires state management and resource release) is to reduce code verbosity and minimize the chance of errors, such as forgetting to close a session or roll back a failed transaction. It promotes cleaner, safer, and more readable code.

### SQLAlchemy Intermediate Challenge: Product and Supplier Tables

This challenge will focus on creating two related tables, `Product` and `Supplier`, using SQLAlchemy. Each product will have an associated supplier, demonstrating the use of foreign keys to establish relationships between tables. Additionally, you will perform insertions into these tables to practice data manipulation.

#### Step 1: Initial Setup

First, make sure you have SQLAlchemy installed. If not, install it using pip:

```bash
pip install sqlalchemy
```

#### Step 2: Defining Models

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20))
    email = Column(String(50))
    address = Column(String(100))

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    price = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    
    # Establishes the relationship between Product and Supplier
    supplier = relationship("Supplier")
```

#### Step 3: Creating the Database and Tables

```python
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

#### Step 4: Insertions in Tables

First, let's enter some suppliers:

```python
suppliers = [
    Supplier(name="Supplier A", phone="12345678", email="contato@a.com", address="Address A"),
    Supplier(name="Supplier B", phone="87654321", email="contato@b.com", address="Address B"),
    Supplier(name="Supplier C", phone="12348765", email="contato@c.com", address="Address C"),
    Supplier(name="Supplier D", phone="56781234", email="contato@d.com", address="Address D"),
    Supplier(name="Supplier E", phone="43217865", email="contato@e.com", address="Address E")
]

session.add_all(suppliers)
session.commit()
```

Next, we insert some products, each linked to a supplier:

```python
products = [
    Product(name="Product 1", description="Product Description 1", price=100, supplier_id=1),
    Product(name="Product 2", description="Product Description 2", price=200, supplier_id=2),
    Product(name="Product 3", description="Product Description 3", price=300, supplier_id=3),
    Product(name="Product 4", description="Product Description 4", price=400, supplier_id=4),
    Product(name="Product 5", description="Product Description 5", price=500, supplier_id=5)
]

session.add_all(products)
session.commit()
```

#### Step 5: Data Query

To check if everything went as expected, you can do a simple query to list all products and their suppliers:

```python
for product in session.query(Produto).all():
    print(f"Product: {product.name}, Supplier: {product.supplier.name}")
```

This challenge covers intermediate concepts such as creating related tables, inserting data with foreign keys, and basic queries in SQLAlchemy. It offers good practice for anyone learning how to manipulate relationships between tables in a relational database context using ORM.

Let's create a practical example that demonstrates the use of `JOIN` and `GROUP BY` both in pure SQL and using SQLAlchemy (ORM). The objective is to obtain the sum of product prices grouped by supplier.

### Scenario

We have two tables: `suppliers` and `products`. Each product has a `supplier_id` that links it to a specific supplier in the `suppliers` table.

### Pure SQL

To perform this operation in pure SQL, you can use the following query:

```sql
SELECT suppliers.name, SUM(products.price) AS total_price
FROM products
JOIN suppliers ON product.supplier_id = suppliers.id
GROUP BY suppliers.name;
```

This query joins the `products` and `suppliers` tables using `supplier_id`, groups the results by the name of the supplier and, for each group, calculates the sum of the prices of the products associated with that supplier.

### SQLAlchemy (ORM)

To perform the same operation using SQLAlchemy, you would follow these steps:

```python
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
# Assuming that the engine has already been defined previously and the Product and Supplier models have been defined as in the previous example.

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(
    Supplier.name,
    func.sum(Produto.price).label('total_price')
).join(Product, Supplier.id == Product.supplier_id
).group_by(Supplier.name).all()

for name, total_price in result:
    print(f"Supplier: {name}, Total Price: {total_price}")
```

In the example above with SQLAlchemy, we used the `query()` method to build a query that selects the name of the supplier and the sum of product prices. We use `join()` to join the `Product` and `Supplier` tables based on the foreign key. `group_by()` is used to group results by supplier name, and `func.sum()` calculates the sum of product prices for each group.

### Conclusion

Both methods, pure SQL and SQLAlchemy, achieve the same result: they group products by supplier and calculate the sum of product prices for each supplier. The main difference is in the approach: while pure SQL is more direct and requires you to write the query explicitly, SQLAlchemy abstracts the construction of the query, allowing you to use Python methods and relationships between models to define the query. Choosing one or the other will depend on your specific needs, development preferences and the context of your project.