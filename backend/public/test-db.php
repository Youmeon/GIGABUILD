<?php

require __DIR__ . '/../vendor/autoload.php';

use App\Database\Database;

try {

    $pdo = Database::connection();

    echo 'DB CONNECTED';

} catch (Throwable $e) {

    echo $e->getMessage();
}

