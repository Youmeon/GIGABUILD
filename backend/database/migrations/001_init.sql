CREATE DATABASE skdionis
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE skdionis;

CREATE TABLE requests (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    full_name VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    email VARCHAR(255) NULL,

    request_source VARCHAR(100) NULL,

    status ENUM(
        'new',
        'processing',
        'completed',
        'rejected'
    ) DEFAULT 'new',

    manager_comment TEXT NULL,

    client_ip VARCHAR(45) NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE admin_users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(100) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    role ENUM(
        'super_admin',
        'manager'
    ) DEFAULT 'manager',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notification_logs (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    request_id BIGINT UNSIGNED NULL,

    notification_type ENUM(
        'email',
        'whatsapp'
    ) NOT NULL,

    status ENUM(
        'success',
        'failed'
    ) NOT NULL,

    error_message TEXT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_notification_request
    FOREIGN KEY (request_id)
    REFERENCES requests(id)
    ON DELETE SET NULL
);

CREATE INDEX idx_requests_status
ON requests(status);

CREATE INDEX idx_requests_created
ON requests(created_at);

CREATE INDEX idx_notifications_type
ON notification_logs(notification_type);

CREATE INDEX idx_notifications_status
ON notification_logs(status);
