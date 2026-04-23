CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount INTEGER NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
    description TEXT,
    category_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);

-- Insert some default categories
INSERT INTO categories (name, type) VALUES ('薪水', 'income');
INSERT INTO categories (name, type) VALUES ('投資', 'income');
INSERT INTO categories (name, type) VALUES ('餐飲', 'expense');
INSERT INTO categories (name, type) VALUES ('交通', 'expense');
INSERT INTO categories (name, type) VALUES ('娛樂', 'expense');
INSERT INTO categories (name, type) VALUES ('生活用品', 'expense');
