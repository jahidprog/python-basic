-- 00_schema.sql
-- Re-create the practice schema from scratch.
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS predictions;
DROP TABLE IF EXISTS model_experiments;
DROP TABLE IF EXISTS support_tickets;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id       INTEGER PRIMARY KEY,
    full_name     TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    country       TEXT,
    signup_date   TEXT NOT NULL, -- ISO format: YYYY-MM-DD
    signup_source TEXT,
    age           INTEGER CHECK (age IS NULL OR age BETWEEN 13 AND 110)
);

CREATE TABLE courses (
    course_id   INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    category    TEXT NOT NULL,
    difficulty  TEXT CHECK (difficulty IN ('Beginner','Intermediate','Advanced')),
    price       REAL NOT NULL CHECK (price >= 0)
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    user_id       INTEGER NOT NULL REFERENCES users(user_id),
    course_id     INTEGER NOT NULL REFERENCES courses(course_id),
    enrolled_at   TEXT NOT NULL,
    completed_at  TEXT,
    score         REAL CHECK (score IS NULL OR score BETWEEN 0 AND 100),
    status        TEXT NOT NULL CHECK (status IN ('enrolled','in_progress','completed','dropped')),
    amount_paid   REAL NOT NULL DEFAULT 0 CHECK (amount_paid >= 0)
);

CREATE TABLE projects (
    project_id   INTEGER PRIMARY KEY,
    user_id      INTEGER NOT NULL REFERENCES users(user_id),
    project_name TEXT NOT NULL,
    domain       TEXT NOT NULL,
    tech_stack   TEXT,
    started_at   TEXT,
    deployed     INTEGER NOT NULL DEFAULT 0 CHECK (deployed IN (0,1)),
    stars        INTEGER NOT NULL DEFAULT 0 CHECK (stars >= 0)
);

CREATE TABLE model_experiments (
    experiment_id INTEGER PRIMARY KEY,
    model_name    TEXT NOT NULL,
    task_type     TEXT NOT NULL,
    dataset_name  TEXT NOT NULL,
    algorithm     TEXT NOT NULL,
    accuracy      REAL,
    precision_score REAL,
    recall_score  REAL,
    f1_score      REAL,
    train_minutes REAL,
    experiment_date TEXT NOT NULL,
    environment   TEXT
);

CREATE TABLE predictions (
    prediction_id INTEGER PRIMARY KEY,
    user_id       INTEGER REFERENCES users(user_id),
    model_name    TEXT NOT NULL,
    predicted_label TEXT,
    confidence    REAL CHECK (confidence IS NULL OR confidence BETWEEN 0 AND 1),
    latency_ms    REAL CHECK (latency_ms IS NULL OR latency_ms >= 0),
    was_correct   INTEGER CHECK (was_correct IS NULL OR was_correct IN (0,1)),
    requested_at  TEXT NOT NULL
);

CREATE TABLE support_tickets (
    ticket_id     INTEGER PRIMARY KEY,
    user_id       INTEGER NOT NULL REFERENCES users(user_id),
    category      TEXT NOT NULL,
    priority      TEXT NOT NULL CHECK (priority IN ('low','medium','high','urgent')),
    created_at    TEXT NOT NULL,
    resolved_at   TEXT,
    status        TEXT NOT NULL CHECK (status IN ('open','in_progress','resolved','closed'))
);

-- Helpful indexes to explore in the optimization lesson.
CREATE INDEX idx_users_signup_date ON users(signup_date);
CREATE INDEX idx_enrollments_user_id ON enrollments(user_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
CREATE INDEX idx_predictions_model_requested ON predictions(model_name, requested_at);
