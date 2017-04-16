/*price range*/

(function () {
  var rangeInput = $('#sl2');
  var rangeSlider = rangeInput.slider();
  // rangeSlider.on("slideStop", function (e) {
  //   changeRange();
  // });
  function changeRange() {
    var newVal = rangeInput.data('slider').getValue();
    var url = window.location;
    window.location.href = `${url.origin+url.pathname}?min=${newVal[0]}&max=${newVal[1]}`
  }
  $("#change-range").on("click", function (e) {
    e.preventDefault();
    changeRange();
  })
}());
/* Quantity changein cart */
(function () {
  if($(".cart_quantity")){
    var quantityInput = $(".cart_quantity_input");
    $(".cart_quantity_up").on("click", function (e) {
      e.preventDefault();
      var val = parseInt(quantityInput.val());
      quantityInput.val(++val);
    });
    $(".cart_quantity_down").on("click", function (e) {
      e.preventDefault();
      var val = parseInt(quantityInput.val());
      if(val > 0){
        quantityInput.val(--val);
      }
    });
  }
}());
	var RGBChange = function() {
	  $('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};

/*scroll to top*/

$(document).ready(function(){
	$(function () {
		$.scrollUp({
	        scrollName: 'scrollUp', // Element ID
	        scrollDistance: 300, // Distance from top/bottom before showing element (px)
	        scrollFrom: 'top', // 'top' or 'bottom'
	        scrollSpeed: 300, // Speed back to top (ms)
	        easingType: 'linear', // Scroll to top easing (see http://easings.net/)
	        animation: 'fade', // Fade, slide, none
	        animationSpeed: 200, // Animation in speed (ms)
	        scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
					//scrollTarget: false, // Set a custom target element for scrolling to the top
	        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
	        scrollTitle: false, // Set a custom <a> title if required.
	        scrollImg: false, // Set true to use image
	        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	        zIndex: 2147483647 // Z-Index for the overlay
		});
	});
});
