$(function() {
 let header = $('.header');

 $(window).scroll(function() {
   if($(this).scrollTop() > 40) {
    header.addClass('hd-bs');
    header.addClass('hd-bs-bg-bl');
    header.removeClass('hd-bs-bg-tr');
   } else {
    header.removeClass('hd-bs');
    header.removeClass('hd-bs-bg-bl');
    header.addClass('hd-bs-bg-tr');
   }
 });
});