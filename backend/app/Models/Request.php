<?php

declare(strict_types=1);

namespace App\Models;

final class Request
{
    public function __construct(

        public readonly ?int $id,

        public readonly string $fullName,

        public readonly string $phone,

        public readonly ?string $email,

        public readonly string $status = 'new'

    ) {
    }
}
