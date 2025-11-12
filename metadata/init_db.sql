CREATE TABLE IF NOT EXISTS datasets (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  path TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT now(),
  version TEXT,
  checksum TEXT
);

CREATE TABLE IF NOT EXISTS runs (
  id SERIAL PRIMARY KEY,
  dataset_id INT REFERENCES datasets(id),
  status TEXT,
  started_at TIMESTAMP,
  finished_at TIMESTAMP,
  details TEXT
);
