$(document).ready(function(){
 $(window).scroll(function(){
 if ($(window).scrollTop() > 100) {
  $('#scrollToTop').fadeIn();
 } else {
  $('#scrollToTop').fadeOut();
 }
 });
});

function scrolltop()
{
 $('html, body').animate({scrollTop : 0},500);
}