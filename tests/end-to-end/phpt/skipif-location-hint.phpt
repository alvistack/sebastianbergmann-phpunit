--TEST--
PHPT skip condition results in correct code location hint
--FILE--
<?php declare(strict_types=1);
$_SERVER['argv'][] = '--do-not-cache-result';
$_SERVER['argv'][] = '--display-skipped';
$_SERVER['argv'][] = '--no-configuration';
$_SERVER['argv'][] = \realpath(__DIR__ . '/../_files/phpt-skipif-location-hint-example.phpt');

require_once __DIR__ . '/../../bootstrap.php';

PHPUnit\TextUI\Application::main();
--EXPECTF--
PHPUnit %s by Sebastian Bergmann and contributors.

Runtime:       %s

S                                                                   1 / 1 (100%)

Time: %s, Memory: %s

There was 1 skipped test:

1) %stests%eend-to-end%e_files%ephpt-skipif-location-hint-example.phpt
something terrible happened

%stests%eend-to-end%e_files%ephpt-skipif-location-hint-example.phpt:8

OK, but incomplete, skipped, or risky tests!
Tests: 1, Assertions: 0, Skipped: 1.
