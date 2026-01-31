WORKS_TABLE = """
    CREATE TABLE IF NOT EXISTS works (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_title TEXT NOT NULL,
        title TEXT DEFAULT NULL,
        native_title TEXT DEFAULT NULL,
        year INTEGER NOT NULL,
        format TEXT NOT NULL,
        consumption_type TEXT NOT NULL,
        industry TEXT NOT NULL
    );
"""

GENRES_TABLE = """
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
"""

COMPLETED_TABLE = """
    CREATE TABLE IF NOT EXISTS completed (
        work_id INTEGER PRIMARY KEY,
        score REAL CHECK(score BETWEEN 0 AND 10),
        notes TEXT DEFAULT NULL,
        FOREIGN KEY(work_id) REFERENCES works(id) ON DELETE CASCADE
    );
"""
