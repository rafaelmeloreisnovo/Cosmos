# Database Scripts

Database management, schema, and query scripts for COSMOS framework.

## Available Scripts

### Schema Management
- `init-schema.sql` - Initialize database schema
- `migrations/` - Database migration scripts
- `seed-data.sql` - Seed initial data

### Setup Scripts
- `init-database.sh` - Initialize database
- `backup-database.sh` - Backup database
- `restore-database.sh` - Restore from backup

### Query Scripts
- `queries/fibonacci-sequences.sql` - Fibonacci data queries
- `queries/galaxy-analysis.sql` - Galaxy data queries
- `queries/energy-simulations.sql` - Simulation result queries

## Database Schema

### Tables

- `fibonacci_sequences` - Stored Fibonacci calculations
- `galaxy_data` - Galaxy pattern analysis results
- `energy_simulations` - Energy conversion simulation results
- `users` - User accounts
- `api_logs` - API request logs

## Usage

```bash
# Initialize database
./init-database.sh

# Seed data
psql -U cosmos -d cosmos_db -f seed-data.sql

# Backup
./backup-database.sh

# Restore
./restore-database.sh backup_file.sql
```

## Requirements

- PostgreSQL 13+
- psql command-line tool

## Configuration

Database connection settings in `config.env`:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cosmos_db
DB_USER=cosmos
DB_PASSWORD=secure_password
```
