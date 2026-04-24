import sqlite3

DB_FILE = "fitness.db"


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY,
        name TEXT DEFAULT 'User',
        age INTEGER DEFAULT 25,
        gender TEXT DEFAULT 'male',
        weight_kg REAL DEFAULT 70.0,
        height_cm REAL DEFAULT 170.0,
        calorie_goal INTEGER DEFAULT 2000,
        step_goal INTEGER DEFAULT 8000,
        water_goal REAL DEFAULT 2.0,
        xp INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        title TEXT DEFAULT 'Rookie'
    )
    """)

    # Check if new columns exist, if not add them (for existing databases)
    try:
        c.execute("ALTER TABLE user_profile ADD COLUMN xp INTEGER DEFAULT 0")
        c.execute("ALTER TABLE user_profile ADD COLUMN level INTEGER DEFAULT 1")
        c.execute("ALTER TABLE user_profile ADD COLUMN title TEXT DEFAULT 'Rookie'")
    except:
        pass

    c.execute("""
    CREATE TABLE IF NOT EXISTS fasting_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time TEXT NOT NULL,
        end_time TEXT,
        protocol TEXT DEFAULT '16:8',
        is_active BOOLEAN DEFAULT 1,
        date TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        badge_type TEXT NOT NULL,
        unlocked_at TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS food_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL,
        meal_type TEXT DEFAULT 'snack',
        calories REAL DEFAULT 0,
        protein_g REAL DEFAULT 0,
        carbs_g REAL DEFAULT 0,
        fat_g REAL DEFAULT 0,
        date TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS activity_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_type TEXT NOT NULL,
        duration_min REAL DEFAULT 0,
        calories_burned REAL DEFAULT 0,
        steps INTEGER DEFAULT 0,
        distance_km REAL DEFAULT 0,
        date TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS water_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount_ml REAL DEFAULT 250,
        date TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS sleep_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hours REAL NOT NULL,
        quality INTEGER DEFAULT 3,
        bedtime TEXT,
        wake_time TEXT,
        notes TEXT,
        date TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS heartrate_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bpm INTEGER NOT NULL,
        context TEXT DEFAULT 'resting',
        date TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS measurements_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight_kg REAL,
        chest_cm REAL,
        waist_cm REAL,
        arms_cm REAL,
        hips_cm REAL,
        date TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)

    # Insert default profile if none exists
    c.execute("SELECT COUNT(*) FROM user_profile")
    if c.fetchone()[0] == 0:
        c.execute("""
        INSERT INTO user_profile
        (id, name, age, gender, weight_kg, height_cm, calorie_goal, step_goal, water_goal)
        VALUES (1, 'User', 25, 'male', 70.0, 170.0, 2000, 8000, 2.0)
        """)

    conn.commit()
    conn.close()
    print("Database ready")