
$a = 123;

$b = function () use($a as $another) {
  return $another + 123;
}

var_dump($b());

