CREATE TABLE IF NOT EXISTS energy_snapshots (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    total_watts DECIMAL(10,4) NOT NULL DEFAULT 0,
    daily_kwh DECIMAL(10,4) NOT NULL DEFAULT 0,
    monthly_kwh DECIMAL(10,4) NOT NULL DEFAULT 0,
    monthly_cost_eur DECIMAL(10,4) NOT NULL DEFAULT 0,
    monthly_co2_kg DECIMAL(10,4) NOT NULL DEFAULT 0,
    efficiency_percent DECIMAL(5,2) NOT NULL DEFAULT 0,
    highest_consumer VARCHAR(160) DEFAULT NULL,
    sustainability_status VARCHAR(60) DEFAULT NULL,
    source VARCHAR(40) NOT NULL DEFAULT 'estimated',
    breakdown_json JSON DEFAULT NULL,
    PRIMARY KEY (id),
    KEY idx_energy_snapshots_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
