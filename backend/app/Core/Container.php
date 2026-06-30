<?php

declare(strict_types=1);

namespace App\Core;

use ReflectionClass;
use ReflectionNamedType;
use ReflectionParameter;
use Exception;

final class Container
{
    private array $instances = [];

    public function set(string $id, object $instance): void
    {
        $this->instances[$id] = $instance;
    }

    public function get(string $class): object
    {
        if (isset($this->instances[$class])) {
            return $this->instances[$class];
        }

        $reflection = new ReflectionClass($class);

        if (!$reflection->isInstantiable()) {
            throw new Exception("Class {$class} is not instantiable.");
        }

        $constructor = $reflection->getConstructor();

        if ($constructor === null) {
            return $this->instances[$class] = new $class();
        }

        $dependencies = array_map(
            fn (ReflectionParameter $parameter) => $this->resolve($parameter),
            $constructor->getParameters()
        );

        return $this->instances[$class] = $reflection->newInstanceArgs($dependencies);
    }

    private function resolve(ReflectionParameter $parameter): object
    {
        $type = $parameter->getType();

        if (!$type instanceof ReflectionNamedType || $type->isBuiltin()) {
            throw new Exception(
                "Cannot resolve dependency {$parameter->getName()}"
            );
        }

        return $this->get($type->getName());
    }
}