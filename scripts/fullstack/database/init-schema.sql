-- COSMOS Database Schema
-- PostgreSQL schema for COSMOS framework

-- Create database (run as postgres user)
-- CREATE DATABASE cosmos_db;
-- \c cosmos_db

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Fibonacci sequences table
CREATE TABLE IF NOT EXISTS fibonacci_sequences (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    terms INTEGER NOT NULL,
    modifier DECIMAL(10, 6) DEFAULT 1.618034,
    sequence JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_fibonacci_user ON fibonacci_sequences(user_id);
CREATE INDEX idx_fibonacci_terms ON fibonacci_sequences(terms);

-- Galaxy data table
CREATE TABLE IF NOT EXISTS galaxy_data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) UNIQUE NOT NULL,
    galaxy_type VARCHAR(100),
    distance_ly DECIMAL(15, 2),
    spiral_arms INTEGER,
    fibonacci_correlation VARCHAR(50),
    description TEXT,
    analysis_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_galaxy_name ON galaxy_data(name);

-- Energy simulations table
CREATE TABLE IF NOT EXISTS energy_simulations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    input_mass_kg DECIMAL(15, 6) NOT NULL,
    wavelength_nm DECIMAL(10, 2) DEFAULT 550,
    duration_seconds DECIMAL(15, 2) DEFAULT 1,
    total_energy_j DECIMAL(30, 6),
    usable_energy_j DECIMAL(30, 6),
    power_watts DECIMAL(30, 6),
    efficiency DECIMAL(5, 4) DEFAULT 0.15,
    simulation_params JSONB,
    results JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_energy_user ON energy_simulations(user_id);
CREATE INDEX idx_energy_created ON energy_simulations(created_at);

-- Pattern analysis table
CREATE TABLE IF NOT EXISTS pattern_analysis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    pattern_type VARCHAR(50) NOT NULL,
    input_data JSONB NOT NULL,
    detected_patterns JSONB,
    confidence_score DECIMAL(5, 4),
    analysis_results JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_pattern_type ON pattern_analysis(pattern_type);
CREATE INDEX idx_pattern_user ON pattern_analysis(user_id);

-- API logs table
CREATE TABLE IF NOT EXISTS api_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    endpoint VARCHAR(255) NOT NULL,
    method VARCHAR(10) NOT NULL,
    status_code INTEGER,
    request_data JSONB,
    response_data JSONB,
    duration_ms INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_api_logs_endpoint ON api_logs(endpoint);
CREATE INDEX idx_api_logs_created ON api_logs(created_at);
CREATE INDEX idx_api_logs_user ON api_logs(user_id);

-- Research projects table
CREATE TABLE IF NOT EXISTS research_projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    owner_id UUID REFERENCES users(id),
    technology_area VARCHAR(100),
    status VARCHAR(50) DEFAULT 'active',
    trl_level INTEGER CHECK (trl_level >= 1 AND trl_level <= 9),
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_research_owner ON research_projects(owner_id);
CREATE INDEX idx_research_area ON research_projects(technology_area);

-- Documentation table
CREATE TABLE IF NOT EXISTS documentation (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    content TEXT,
    metadata JSONB,
    version VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_doc_category ON documentation(category);
CREATE INDEX idx_doc_version ON documentation(version);

-- Create views for common queries

-- View: Recent Fibonacci calculations
CREATE OR REPLACE VIEW recent_fibonacci AS
SELECT 
    f.id,
    f.terms,
    f.modifier,
    f.created_at,
    u.username
FROM fibonacci_sequences f
LEFT JOIN users u ON f.user_id = u.id
ORDER BY f.created_at DESC
LIMIT 100;

-- View: Galaxy analysis summary
CREATE OR REPLACE VIEW galaxy_summary AS
SELECT 
    name,
    galaxy_type,
    distance_ly,
    spiral_arms,
    fibonacci_correlation,
    created_at
FROM galaxy_data
ORDER BY name;

-- View: Energy simulation statistics
CREATE OR REPLACE VIEW energy_stats AS
SELECT 
    COUNT(*) as total_simulations,
    AVG(power_watts) as avg_power_watts,
    MAX(power_watts) as max_power_watts,
    AVG(efficiency) as avg_efficiency
FROM energy_simulations;

-- Functions

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers
CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_galaxy_updated_at
    BEFORE UPDATE ON galaxy_data
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_research_updated_at
    BEFORE UPDATE ON research_projects
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_doc_updated_at
    BEFORE UPDATE ON documentation
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Comments
COMMENT ON TABLE users IS 'User accounts for COSMOS platform';
COMMENT ON TABLE fibonacci_sequences IS 'Stored Fibonacci sequence calculations';
COMMENT ON TABLE galaxy_data IS 'Galaxy pattern analysis data';
COMMENT ON TABLE energy_simulations IS 'ATOMIC_EX_LIGHT energy conversion simulations';
COMMENT ON TABLE pattern_analysis IS 'Pattern recognition analysis results';
COMMENT ON TABLE api_logs IS 'API request and response logs';
COMMENT ON TABLE research_projects IS 'Research projects and innovations';
COMMENT ON TABLE documentation IS 'COSMOS framework documentation';

-- Grant permissions (adjust as needed)
-- For production, use principle of least privilege:
-- GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA public TO cosmos_read_write;
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO cosmos_read_only;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO cosmos_read_write;
-- Example minimal grants:
-- GRANT CONNECT ON DATABASE cosmos_db TO cosmos;
-- GRANT USAGE ON SCHEMA public TO cosmos;
-- GRANT SELECT, INSERT, UPDATE ON users TO cosmos;
-- GRANT SELECT ON fibonacci_sequences, galaxy_data TO cosmos;
