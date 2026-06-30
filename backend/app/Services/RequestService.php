<?php

declare(strict_types=1);

namespace App\Services;

use App\Database\Database;
use PDO;

final class RequestService
{
    private PDO $db;

    public function __construct()
    {
        $this->db = Database::connection();
    }

    public function create(array $data): int
    {
        $sql = "
            INSERT INTO requests
            (
                full_name,
                phone,
                email,
                request_source,
                client_ip
            )
            VALUES
            (
                :full_name,
                :phone,
                :email,
                :request_source,
                :client_ip
            )
        ";

        $stmt = $this->db->prepare($sql);

        $stmt->execute([

            'full_name' => trim($data['full_name']),

            'phone' => trim($data['phone']),

            'email' => $data['email'] ?: null,

            'request_source' => 'website',

            'client_ip' => $_SERVER['REMOTE_ADDR'] ?? null

        ]);

        return (int)$this->db->lastInsertId();
    }
}