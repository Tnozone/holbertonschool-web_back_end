-- 9. Optimize search and score
-- creates an index
CREATE INDEX idx_name_first
ON names (name(1), score);