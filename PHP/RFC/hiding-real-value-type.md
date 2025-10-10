
function aa(string $value) {

}


function bb(string $value) {

}


function cc(string $value) {

}

// ....

function zz(string $value) {

}


type_alias('AlmostValueObject', 'string');

function aa(AlmostValueObject $value) {
  
}

// works just fine if 
aa('string');


// later we remove type_alias and create real value object


class AlmostValueObject
{
  public static function __fromString(string $value) {
    // ...
  }
}


