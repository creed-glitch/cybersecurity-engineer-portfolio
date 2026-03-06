CREATE TABLE Orders (
	OrderNumber TEXT PRIMARY KEY,
	UserID INTEGER, 
	Quantity INTEGER,
	Cost REAL,
	Date TEXT
);

CREATE TABLE OrderItems (
	OrderNumber TEXT,
	ISBN TEXT,
	Quantity INTEGER
);

CREATE TABLE Cart (
	UserID INTEGER,
	ISBN TEXT,
	Quantity INTEGER
);

CREATE TABLE Inventory (
	ISBN TEXT PRIMARY KEY,
	Title TEXT, 
	Author Text,
	Genre TEXT,
	Pages INTEGER,
	ReleaseDate TEXT,
	Price REAL
);

