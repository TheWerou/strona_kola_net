var header = $('h1');
var range = 100;

$(window).on('scroll', function () {
  
  var scrollTop = $(this).scrollTop(),
      calc = 1 - (((scrollTop) / range)*0.2);

  header.css({ 'opacity': calc });

  if (calc > '1') {
    header.css({ 'opacity': 1 });
  } else if ( calc < '0' ) {
    header.css({ 'opacity': 0 });
  }
  
});