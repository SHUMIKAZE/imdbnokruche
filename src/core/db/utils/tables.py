CREATE_WORKS_SQL = """
    CREATE TABLE IF NOT EXISTS works (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_title TEXT NOT NULL,
        title TEXT DEFAULT NULL,
        native_title TEXT DEFAULT NULL,
        year INTEGER,
        format TEXT NOT NULL,
        consumption_type TEXT NOT NULL,
        industry TEXT NOT NULL
    );
"""
