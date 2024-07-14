-- creating index for faster filtering
-- create index on the first char of name column on the names table
CREATE INDEX idx_name_first_score ON names (name(1), score);
