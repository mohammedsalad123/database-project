# SQLAlchemy Models for Sales Database

This project defines three SQLAlchemy models for a sales database: `Vendor`, `Buyer`, and `Admin`. These models represent vendors, buyers, and administrators, and establish relationships between them.

## Vendor Model

The `Vendor` model represents vendors who provide products for sale.

### Attributes

- **id**: Integer, primary key
- **name**: String, the name of the vendor
- **product**: Integer, the product ID (assuming it represents a product)
- **price**: Integer, the price of the product

### Relationships

- **admin**: One-to-Many relationship with the `Admin` model via the backref 'vendor'.

### Representation

The `__repr__` method provides a string representation of a Vendor instance.

Example:
```python
vendor1 = Vendor(name='Example Vendor', product=1, price=100)
print(repr(vendor1))
