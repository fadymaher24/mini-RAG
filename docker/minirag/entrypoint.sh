#!/bin/bash
set -e

DB_HOST="${POSTGRES_HOST:-pgvector}"
DB_PORT="${POSTGRES_PORT:-5432}"

echo "Waiting for database DNS: ${DB_HOST}"
for i in $(seq 1 30); do
	if getent hosts "${DB_HOST}" >/dev/null 2>&1; then
		break
	fi
	sleep 1
done

echo "Waiting for database readiness: ${DB_HOST}:${DB_PORT}"
for i in $(seq 1 30); do
	if (echo >"/dev/tcp/${DB_HOST}/${DB_PORT}") >/dev/null 2>&1; then
		break
	fi
	sleep 1
done

echo "Running database migrations..."
cd /app/models/db_schemes/minirag/
alembic upgrade head
cd /app

# Start the container command (uvicorn from Dockerfile CMD)
exec "$@"
