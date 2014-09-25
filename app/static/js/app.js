var main = function() {
  
  $(".container-radius").hover(function(event) {  	
    $('.image',this).addClass('active-slide').animate({
      height: "140px"
    });
  },function(event) {
    $('.image',this).removeClass('active-slide').animate({
      height: "67px"
    });
  });

 
}


//$(document).ready(main);


// or with jQuery
var $container = $('.masonry');
// initialize Masonry after all images have loaded  
$container.imagesLoaded( function() {
  $container.masonry();
});


var msnry = new Masonry('.masonry');

function onLayout() {
  console.log('layout done');
}
// bind event listener
msnry.on( 'layoutComplete', onLayout );
// un-bind event listener
msnry.off( 'layoutComplete', onLayout );
// return true to trigger an event listener just once
msnry.on( 'layoutComplete', function() {
  console.log('layout done, just this one time');
  return true;
});


$(document).ready(function () {  
  var top = $('.sticky').offset().top;
  $(window).scroll(function (event) {
    var y = $(this).scrollTop();
    if (y >= top)
      $('.sticky').addClass('fixed');
    else
      $('.sticky').removeClass('fixed');
    $('.sticky').width($('.sticky').parent().width());
  });
});
