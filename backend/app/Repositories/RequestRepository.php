<?php

declare(strict_types=1);

namespace App\Repositories;

use App\Database\Database;
use PDO;
use Exception;

final class RequestRepository
{
    private PDO $db;

    public function __construct()
    {
        $this->db = Database::connection();
    }

    public function create(array $data): void
    {
        $sql = "INSERT INTO requests 
                (full_name, phone, email, request_source, client_ip, status, created_at, updated_at) 
                VALUES 
                (:full_name, :phone, :email, :request_source, :client_ip, 'new', NOW(), NOW())";

        $stmt = $this->db->prepare($sql);

        $success = $stmt->execute([
            'full_name'      => $data['full_name'],
            'phone'          => $data['phone'],
            'email'          => $data['email'] ?? null,
            'request_source' => $data['request_source'] ?? 'website',
            'client_ip'      => $_SERVER['REMOTE_ADDR'] ?? null,
        ]);

        if (!$success) {
            throw new Exception("Не удалось сохранить заявку в базу данных");
        }
    }
}