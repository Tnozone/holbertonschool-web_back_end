-- 8. Optimize simple search
-- creates an index
CREATE INDEX idx_name_first
ON names (name(1));